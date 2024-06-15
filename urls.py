"""
URL configuration for notes project.

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
from akkinotes.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('Termsofuse', Termsofuse, name='Termsofuse'),
    path('faq', faq, name='faq'),
    path('refundpolicy', refundpolicy, name='refundpolicy'),
    path('privacypolicy', privacypolicy, name='privacypolicy'),
    path('copyright', copyright, name='copyright'),
    path('user_login', user_login, name='user_login'),
    path('admin_login', admin_login, name='admin_login'),
    path('signup1', signup1, name='signup1'),
    path('admin_home', admin_home, name='admin_home'),
    path('admin_logout', admin_logout, name='admin_logout'),
    path('profile', profile, name='profile'),
     path('viewusers', viewusers, name='viewusers'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('changepassword', changepassword, name='changepassword'),
    path('pending', pending, name='pending'),
    path('accepted', accepted, name='accepted'),
    path('rejected', rejected, name='rejected'),
    path('allnotes', allnotes, name='allnotes'),
    path('viewallnotes', viewallnotes, name='viewallnotes'),
    path('uploadnotes', uploadnotes, name='uploadnotes'),
    path('viewnotes', viewnotes, name='viewnotes'),
    path('delete_mynotes/<int:pid>', delete_mynotes, name='delete_mynotes'),
    path('delete_users/<int:pid>', delete_users, name='delete_users'),
    path('delete_notes/<int:pid>', delete_notes, name='delete_notes'),
     path('assignstatus/<int:pid>', assignstatus, name='assignstatus'),
    path('' ,index, name='index')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
