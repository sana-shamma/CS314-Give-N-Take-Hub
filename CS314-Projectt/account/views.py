from django.shortcuts import render, redirect
from .models import customer
from django.urls import reverse
from Service.models import giftItem, borrowedItem, swapedItem 
from django.core.files.storage import FileSystemStorage


def logout (request):
    #destory session
    del request.session['email']
    return redirect('signup')

def request (request):
    if request.session.get('email') == None :
        return redirect('signup')
    if request.method == 'POST':
        # get user inputs
        v_itemname=request.POST.get("ItemName")
        v_owner=request.POST.get("owner")
        v_PhoneNumber=request.POST.get("phoneNumber")
        v_sharingType=request.POST.get("sharingType")
        v_description=request.POST.get("description")
        v_image = request.FILES.get("image")
        v_email = request.session.get('email')
        v_customer = customer.objects.get(email=v_email)
        #check sharing type
        # store the inputs in DB
        if v_sharingType == "borrow":
            fs = FileSystemStorage()
            filename = fs.save(v_image.name, v_image)
            uploaded_file_url = fs.url(filename)
            uploaded_file_url = uploaded_file_url.replace('media/', '')
            v_borrowedItem = borrowedItem (name = v_itemname ,owner = v_owner , phone = v_PhoneNumber ,description= v_description ,  image= uploaded_file_url )
            v_borrowedItem.save()
            v_customer.points += 1
            v_customer.save()
            return redirect('borrowItems')
        if v_sharingType == "swap":
            fs = FileSystemStorage()
            filename = fs.save(v_image.name, v_image)
            uploaded_file_url = fs.url(filename)
            uploaded_file_url = uploaded_file_url.replace('media/', '')
            v_swapedItem = swapedItem (name = v_itemname ,owner = v_owner , phone = v_PhoneNumber ,description= v_description , image = v_image )
            v_swapedItem.save()
            v_customer.points += 1
            v_customer.save()
            #check home page link
            return redirect('swapItems')
        if v_sharingType == "gift":
            fs = FileSystemStorage()
            filename = fs.save(v_image.name, v_image)
            uploaded_file_url = fs.url(filename)
            uploaded_file_url = uploaded_file_url.replace('media/', '')
            v_giftItem = giftItem (name = v_itemname ,owner = v_owner , phone = v_PhoneNumber ,description= v_description , image = v_image )
            v_giftItem.save()
            v_customer.points += 1
            v_customer.save()
            #check home page link
            return redirect('giftItems')
    return render(request,'registration/request.html')

def loginTo(request):
    if request.method == 'POST':
        # get user inputs 
        v_email=request.POST.get("email")
        v_password=request.POST.get("password")
        try:
            # check if the customer is registered
            v_customer= customer.objects.get(email=v_email)
        except customer.DoesNotExist:
            email_error_message = 'This email address is not registered. Please sign up for a new account.'
            return render(request,'registration/login.html',{'email_error_message': email_error_message})
            # check if the customer email matches password
        if v_password == v_customer.password:
            request.session['email'] = v_email
            #check home page link
            return redirect(reverse('page:home'))
        else:
            error_message = 'Incorrect password or email. Please try again.'
            return render(request,'registration/login.html',  {'error_message': error_message})
    else:
        return render(request,'registration/login.html')

def signup(request):
    if request.method == 'POST':
        # get user inputs
        v_name=request.POST.get("userName") 
        v_email=request.POST.get("email")
        v_password=request.POST.get("password")
        # check if the email already exists in the database
        if customer.objects.filter(email=v_email).exists():
            email_error_message = 'This email address is already in use. Please enter a different email.'
            return render(request, 'registration/signup.html', {'email_error_message': email_error_message})
        v_customer = customer(userName=v_name, email=v_email, password=v_password)
        v_customer.save()
        return redirect('login')
    return render(request,'registration/signup.html')







