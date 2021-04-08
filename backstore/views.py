from django.shortcuts import render
from django.shortcuts import redirect

from .models import Medicine
from .models import Dealer
from .models import Brand
from .models import Staff
from .models import User
from django.template import loader

import bcrypt

# Create your views here.

from django.http import HttpResponse

def brands(request):
	if not request.session.get('user_logged_in'):
		return redirect('/user')

	brands = Brand.objects.all()

	template = loader.get_template('brands.html')
	data = {
		'brands': brands
	}
	return HttpResponse(template.render(data,request))

def dealers(request):

	if not request.session.get('user_logged_in'):
		return redirect('/user')


	dealer = Dealer.objects.all()

	template = loader.get_template('dealers.html')
	data = {
		'dealers': dealer
	}
	return HttpResponse(template.render(data,request))

# ending session
def logout(request):
	request.session["user_logged_in"] = False
	return redirect('/user')



def medicines(request):
	if not request.session.get('user_logged_in'):
		return redirect('/user')

	medicines = Medicine.objects.all()

	print(medicines)

	template = loader.get_template('listing.html')

	data = {
        'medicines': medicines,
    }

	return HttpResponse(template.render(data, request))

def staffs(request):

	if not request.session.get('user_logged_in'):
		return redirect('/user')

	staf = Staff.objects.all()

	template = loader.get_template('staff.html')

	data = {
		'staff': staf
	}
	
	return HttpResponse(template.render(data,request))


def user(request):


	return render(request, 'user.html')

def register(request):
	name = request.POST.get('name')
	email = request.POST.get('email')

	# Hashing the password before storing
	password = request.POST.get('password')
	salt = bcrypt.gensalt()
	hashed_password = bcrypt.hashpw(password.encode('ascii'), salt)
	
	dob = request.POST.get('date')
	user = User(name=name , email=email, password=hashed_password, dob=dob)
	user.save()

	return redirect("/user")


def login(request):
	name = request.POST.get('name')
	password = request.POST.get('password')
	
	try:
		check_user = User.objects.get(name=name)
	except Exception as e:
		return redirect("/user")

	if(check_user.password == password):

		request.session["user_logged_in"] = True

		# Set the session
		return redirect('/medicines')

	return redirect("/user")
