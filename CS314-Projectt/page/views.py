from django.shortcuts import render, redirect
from .models import sponsor
# Create your views here.

# Home view.
def home (request):
        return render (request,'page/home.html')
# About view.
def about(request):
    # If the user not signup yet, render the signup page.
    if request.session.get('email')== None:
        return redirect('signup')
    post = sponsor.objects.all()
    # Else render the home page.
    return render(request,'page/about.html',{'post': post})


