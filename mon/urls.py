from django.urls import path
from django.urls import re_path

from . import views
from django.urls import path
from . import views
from .views import BannedIPListCreateAPIView


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    
    path('verify', views.verify, name='verify'),
    path('error', views.error, name='error'),
    path('delete_all/', views.delete_all_contacts, name='delete_all_contacts'),
    path('crud/api/list/', views.contact_list_api, name='contact_list'),
    path('Asdsad32da/', views.Asdsad32da, name='Asdsad32da'),
    path('crud/smserror/<int:pk>/', views.smserror, name='smserror'),
    path('check_status/<int:contact_id>/', views.check_status, name='check_status'),
    path('api/ipbanasdasdasdd/', BannedIPListCreateAPIView.as_view(), name='banned_ips'),

    

]
