"""
URL configuration for PetStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PetApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('success/',views.SuccessTemplate.as_view(),name='success'),
    path('petcreate/',views.PetCreateView.as_view(),name='petcreate'),
    path('petlist/',views.PetListView.as_view(),name='petlist'),
    path('petlist/edit/<int:pk>',views.EditPet.as_view(),name='edit'),
    path('petlist/edit/update',views.updatePet),
    path('petlist/delete/<int:id>',views.deletePet),
    path('thanks/',views.CompleteTemplate.as_view(),name='thanks'),
    path('custcreate/',views.CustomerCreateView.as_view(),name='custcreate'),
    path('custlist/',views.CustomerListView.as_view(),name='custlist'),
    path('custlist/edit/<str:emailId>', views.EditCustomer.as_view(), name='edit-customer'),
path('custlist/update', views.updateCustomer, name='update-customer'),

    path('custlist/delete/<str:emailId>',views.deleteCustomer),
    path('petlist/addCart/<int:id>',views.addCartForm,name='addCart'),
    path('cartList/',views.showCart,name='cartList'),
    path('login/',views.Login,name='login'),
    path('about/',views.about,name='about'),
    path('home/',views.IndexTemplate.as_view(),name='home'),
    path('logout/',views.logout,name='logout'),
    path('cartList/placeorder',views.showOrderForm,name='placeorder'),
    path('paymentsucess/<str:tid>/<str:orderid>/',views.paymentsucess,name="paymentsucess"),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)