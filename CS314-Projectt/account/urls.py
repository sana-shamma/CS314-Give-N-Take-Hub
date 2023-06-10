from . import views
from django.urls import path

urlpatterns = [
    path('',views.signup, name = 'signup'),
    path('login',views.loginTo,name = 'login'),
    path('request',views.request,name='request'),
    path('logout',views.logout,name='logout'),
]