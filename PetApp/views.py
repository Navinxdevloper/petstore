from django.forms import BaseModelForm
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from PetApp.models import Pet,Orders,Payment
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.hashers import make_password,check_password
from django.urls import reverse_lazy
from datetime import date
from django.conf import settings
from django.core.mail import send_mail

class SuccessTemplate(TemplateView):
    template_name='PetApp/Success.html'

class PetCreateView(CreateView):
    model=Pet
    fields=['name','gender','breed','age','price','species','description','pet_image']
    success_url='/success/'

class PetListView(ListView):
    model=Pet
    context_object_name='pets'
    template_name='PetApp/PetList.html'

class PetDetailView(DetailView):
    model=Pet
    context_object_name='pets'
    template_name='PetApp/UpdatePet.html'

class EditPet(DetailView):
    model=Pet
    context_object_name='pets'
    template_name='PetApp/UpdatePet.html'

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Pet

def updatePet(request):
    if request.method == 'POST':
        pid = request.POST.get('id')
        pname = request.POST.get('name')
        gen = request.POST.get('gender')
        brd = request.POST.get('breed')
        ag = request.POST.get('age')
        pr = request.POST.get('price')
        spc = request.POST.get('species')
        desc = request.POST.get('description')

        try:
            pet = Pet.objects.get(id=pid)
        except Pet.DoesNotExist:
            raise Http404("Pet does not exist")

        pet.name = pname
        pet.gender = gen
        pet.breed = brd
        pet.age = ag
        pet.price = pr
        pet.species = spc
        pet.description = desc
        pet.save()

        return HttpResponseRedirect(reverse("petlist"))

    else:
         return render(request,'UpdatePet.html')

    
def deletePet(request,id):
    data=Pet.objects.get(id=id)
    data.delete()
    return redirect("/petlist")


from PetApp.models import Customer

class CompleteTemplate(TemplateView):
    template_name='PetApp/Complete.html'

class CustomerCreateView(CreateView):
    model=Customer
    fields=['name','emailId','password','address','contactNo']
    success_url = '/login/'
    
class CustomerListView(ListView):
    model=Customer
    context_object_name='customers'
    template_name='PetApp/CustomerList.html'

class CustomerDetailView(DetailView):
    model=Customer
    context_object_name='customers'
    template_name='PetApp/UpdateCustomer.html'

from django.shortcuts import get_object_or_404

from django.views.generic.edit import UpdateView
from PetApp.models import Customer
from django.urls import reverse_lazy
from django.http import Http404

class EditCustomer(UpdateView):
    model = Customer
    fields = ['name', 'emailId', 'password', 'address', 'contactNo']  # Specify the fields to be editable
    template_name = 'PetApp/UpdateCustomer.html'
    success_url = reverse_lazy('custlist')  # Redirect URL after successful update

    def get_object(self, queryset=None):
        # Retrieve the customer object based on the emailId from URL
        emailId = self.kwargs.get('emailId')
        return Customer.objects.get(emailId=emailId)
    
    def get_object(self, queryset=None):
        emailId = self.kwargs.get('emailId')
        try:
            return Customer.objects.get(emailId=emailId)
        except Customer.DoesNotExist:
            raise Http404("Customer does not exist")
def updateCustomer(request):
    print("Inside updateCustomer function")
    if request.method == 'POST':
        print("Form data received:", request.POST)
        cname = request.POST['name']
        email = request.POST['emailId']
        paswrd = request.POST['password']
        adrs = request.POST['address']
        contact = request.POST['contactNo']
        cust = Customer.objects.filter(emailId=email)
        cust.update(name=cname, emailId=email, password=paswrd, address=adrs, contactNo=contact)
        
        # Print the updated customer to check if changes are reflected
        updated_customer = Customer.objects.get(emailId=email)
        print("Updated customer:", updated_customer)
        
        return redirect("custlist")
    else:
        return render(request, 'UpdateCustomer.html')

       
def deleteCustomer(request,emailId):
    data=Customer.objects.get(emailId=emailId)
    data.delete()
    return redirect("/custlist")

from django.shortcuts import redirect
from PetApp.models import CartModel

def addCartForm(request, id):
    if request.method == 'POST':
        pet = Pet.objects.get(id=id)
        email = request.POST.get('emailId')
        cust = Customer.objects.get(emailId=email)
        quantity = request.POST.get('quantity')
        totalPrice = request.POST.get('totalPrice')
        cart = CartModel.objects.create(pid=pet, emailId=cust, quantity=quantity, totalPrice=totalPrice)
        cart.save()
        return redirect("cartList")  # Redirect to the cart list URL name
    else:
        data = Pet.objects.get(id=id)
        quantity = range(101)
        return render(request, 'PetApp/AddCart.html', {'pet': data, 'quant': quantity})
def showCart(request):
    email= request.session['username']
    data=CartModel.objects.filter(emailId=email)
    return render(request,'PetApp/CartList.html',{'cart':data})


def showOrderForm(request):
    if request.method=='POST':
        emailId=request.session['username']
        data=CartModel.objects.filter(emailId=emailId)
        totalbill=0
        for i in data:
            totalbill=totalbill+i.totalPrice
        name=request.POST['name']
        add=request.POST['address']
        city=request.POST['city']
        st=request.POST['state']
        pin=request.POST['pincode']
        pno=request.POST['phoneno']
        data=Orders.objects.create(emailId=emailId,name=name,address=add,city=city,state=st,pincode=pin,phoneno=pno)
        data.save()
        dateobj=date.today()
        dateobj=str(dateobj).replace('-','')
        datedata=str(data.orderId)+dateobj
        data.ordernumber=datedata
        data.save()
        data=Orders.objects.get(emailId=emailId,ordernumber=datedata)
        total=data.totalbillamount
        return render(request,'PetApp/Payment_page.html',{'order':data,'total':totalbill})
    else:
        return render(request,'PetApp/Order.html')


from PetApp.models import AdminModel

from django.http import HttpResponse

def Login(request):
    if request.method == 'POST':
        emailId = request.POST['email']
        type = request.POST['type']
        
        if type == 'user':
            cust = Customer.objects.filter(emailId=emailId)
            if cust:
                custobj = Customer.objects.get(emailId=emailId)
                password = request.POST['password']
                if password == custobj.password:
                    request.session['username'] = emailId
                    return render(request, 'PetApp/index.html')
                else:
                    return HttpResponse("<h1>Wrong password for user</h1>")
            else:
                return HttpResponse("<h1>User not found</h1>")
        
        elif type == 'admin':
            admin = AdminModel.objects.filter(adminEmailId=emailId)
            if admin:
                adminobj = AdminModel.objects.get(adminEmailId=emailId)
                password = request.POST['password']
                if password == adminobj.adminpassword:
                    request.session['adminEmailId'] = emailId
                    return render(request, 'PetApp/index.html')
                else:
                    return HttpResponse("<h1>Wrong password for admin</h1>")
            else:
                return HttpResponse("<h1>Admin not found</h1>")
        
        else:
            return HttpResponse("<h1>Invalid user type</h1>")
       
    else:
        return render(request, 'PetApp/Login.html')
    
class IndexTemplate(TemplateView):
    template_name="petapp/index.html"


def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return render(request,'PetApp/index.html')

def emailDemo(request):
    subject="Subject here."
    email_body="Here is the message."
    from_email=settings.EMAIL_HOST_USER
    fail_silently=False
    send_mail(subject=subject,message=email_body,from_email=from_email,recipient_list=['trendygayatri.95@gmail.com'])
    return HttpResponse("email Successful")

def paymentsucess(request,tid,orderid):
    emailId=request.session["username"]
    data1=Orders.objects.get(ordernumber=orderid)
    payment=Payment.objects.create(emailId=emailId,amount_paid=data1.totalbillamount,payment_id=tid,status='completed')
    payment.save()
    subject="Thank You For Your Order"
    email_body="email:"+emailId +"tid :"+tid +"id: "+orderid+"message: order get placed"

    from_mail=settings.EMAIL_HOST_USER

    send_mail(subject=subject, message=email_body, from_email=from_mail, recipient_list=['trendygayatri.95@gmail.com'])
    return HttpResponse("<h1>Payment Sucessful</h1>")



from django.shortcuts import render

def about(request):
    # You can add any context data you want to pass to the template
    context = {
        'title': 'About Us',
        'description': 'We are a pet store specializing in providing high-quality pet products and services.',
        
        'image_url': '/static/images_1/th.jpeg', # Replace with the path to your image
        # Add more context data as needed
    }
    # Render the 'about.html' template with the given context
    return render(request, 'petapp/about.html', context)

