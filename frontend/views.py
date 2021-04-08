from django.shortcuts import render
from .models import Contact


from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse

def index(request):

	return render(request,'index.html')

def contact(request):
	User.objects.all()
	return render(request,'contact.html')

def save_contact(request):
	name = request.POST.get('name')
	email = request.POST.get('email')
	comments = request.POST.get('comments')

	contact =  Contact(name=name ,email=email ,comments=comments)
	contact.save()

	messages.success(request, 'Form submitted successfully')

	return redirect('/app/contact')