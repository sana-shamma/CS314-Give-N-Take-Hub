from . import views
from django.urls import path

urlpatterns = [
    path('borrowItems',views.borrowItems,name='borrowItems'),
    path('BorrowDetails/<int:item_id>/', views.borrowed_item_details, name='Details_BorrowItem'),

    path('swapItems',views.swapItems,name='swapItems'),
    path('SwapDetails/<int:item_id>/', views.swaped_item_details, name='Details_swapItem'),

    path('giftItems',views.giftItems,name='giftItems'),
    path('GiftDetails/<int:item_id>/', views.gift_item_details, name='Details_gifItem'),


]