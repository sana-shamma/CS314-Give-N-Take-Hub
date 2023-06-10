from django.shortcuts import render,redirect
from . models import borrowedItem,swapedItem,giftItem
from django.shortcuts import render, get_object_or_404
from PIL import Image
from io import BytesIO

# Create your views here.

#-------------------------------Borrowed Items----------------------------------------#
def borrowItems(request):
    if request.session.get('email')== None:
        return redirect('signup')
    post = borrowedItem.objects.all()
    return render(request,'Services/borrowItems.html',{'post': post})

def borrowed_item_details(request, item_id):
    if request.session.get('email')== None:
        return redirect('signup')
    item = get_object_or_404(borrowedItem, id=item_id)
    context = {
        'item': item
    }
    return render(request, 'Services/Details_BorrowItem.html', context)
#-------------------------------------------------------------------------------------#


#---------------------------------Swaped Items----------------------------------------#
def swapItems(request):
    if request.session.get('email')== None:
        return redirect('signup')
    post = swapedItem.objects.all()
    return render(request,'Services/swapItems.html',{'post': post})

def swaped_item_details(request, item_id):
    if request.session.get('email')== None:
        return redirect('signup')
    item = get_object_or_404(swapedItem, id=item_id)
    context = {
        'item': item
    }
    return render(request, 'Services/Details_swapItem.html', context)
#-------------------------------------------------------------------------------------#


#-----------------------------------Gift Items----------------------------------------#
def giftItems(request):
    if request.session.get('email')== None:
        return redirect('signup')
    post = giftItem.objects.all()
    return render(request,'Services/giftItems.html',{'post': post})

def gift_item_details(request, item_id):
    if request.session.get('email')== None:
        return redirect('signup')
    item = get_object_or_404(giftItem, id=item_id)
    context = {
        'item': item
    }
    return render(request, 'Services/Details_giftItem.html', context)
#-------------------------------------------------------------------------------------#