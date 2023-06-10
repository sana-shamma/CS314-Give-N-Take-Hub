from django.urls import path
from . import views

app_name = 'reward'

urlpatterns = [
    path('', views.leaderboard, name='leaderboard'),
    path('redeem/', views.redeem, name='redeem'),
    path('redeem_coupon/<int:coupon_id>/', views.redeem_coupon, name='redeem_coupon'),

   
]