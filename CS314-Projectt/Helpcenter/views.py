from django.shortcuts import redirect, render
from .models import Contact
# Create your views here.

def contact (request):
   #This line must be delete
   if request.session.get('email') == None:
       return redirect('signup')
   if request.method == 'POST':
      # get the data from the front 
      v_name = request.POST.get('name')
      v_email = request.POST.get('email')
      v_subject = request.POST.get('subject')
      v_message = request.POST.get('message')
      # sent this data to the DB (Models)
      v_contact = Contact(name = v_name, email = v_email, subject = v_subject, message = v_message)
      v_contact.save()
      return render (request,'Helpcenter/thank.html')
   else:
      return render (request, 'Helpcenter/contact.html')
   
def FAQ (request):
   if request.session.get('email') == None:
      return redirect('signup')
   return render (request, 'Helpcenter/FAQs.html')

def thankyou (request):
   return render (request, 'Helpcenter/thank.html')