"""djangoInventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from django.urls import path
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('signup/',views.signup,name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/',views.signin,name='signin'),
    path('items/',views.items,name='items'),
    path('items/create', views.create_item, name='create_item'),
    path('items/<int:item_id>/', views.item_detail, name='item_detail'),
    path('items/<int:item_id>/delete', views.delete_item, name='delete_item'),
    path('locations/',views.locations,name='locations'),
    path('locations/create', views.create_location, name='create_location'),
    path('locations/<int:location_id>/', views.location_detail, name='location_detail'),
    path('locations/<int:location_id>/delete', views.delete_location, name='delete_location'),
    path('users/create', views.create_user, name='create_user')

]