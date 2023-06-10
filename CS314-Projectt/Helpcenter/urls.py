from .import views
from django.urls import path
urlpatterns = [
    
    path ('contact/', views.contact, name='contact'),
    path ('FAQs/', views.FAQ, name = 'FAQs'),  
    path('thank_you/', views.thankyou, name = 'thank')  
]