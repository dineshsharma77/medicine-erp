from django.shortcuts import render
from django.shortcuts import redirect

from .models import Medicine
from .models import Dealer
from .models import Brand
from .models import Staff
from .models import User

from django.template import loader
from datetime import timedelta, datetime

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
	# finding out medicines which are out of stock
	medicines = Medicine.objects.all()

					
	
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


def dashboard(request):
	if not request.session.get('user_logged_in'):
		return redirect('/user')

		# template = loader.get_template('dashboard.html')

	expiring_medicines = checkexpiry()
	print(expiring_medicines)

	stock = checkstock()

	# exp_med = Expiring_medicines.objects.all()
	# stock = Stock.objects.all()

	template = loader.get_template('dashboard.html')

	data = {
		'expiring_medicines' : expiring_medicines,
		'stock' : stock,
	}		
	return HttpResponse(template.render(data,request))


def delete(request, id):
	try:
		delete_med = Medicine.objects.get(id=id)

		delete_med.delete()
	except Exception as e:
		print ("exception occurred  " + str(e))
	

	return redirect('/medicines')




def checkexpiry():

	
	today = datetime.now()

	time_diff = timedelta(days=60)

	des_date = (today + time_diff)

	expiring_medicines = Medicine.objects.filter( expiry_date__range=(today, des_date))

	return expiring_medicines


def checkstock():

	stock = Medicine.objects.filter( packing__range= (0,5))

	# for med in stock:
	# 	name = med.name
	# 	brand = med.brand.name
	# 	batch_no = med.batch_no
	# 	quantity = med.quantity
	# 	packing = med.packing
	# 	dealer = med.dealer.name
	# 	cost = med.cost
	# 	selling_price = med.selling_price
	# 	expiry_date = med.expiry_date

	# 	stock = Stock(name = name,brand=brand,batch_no=batch_no,quantity=quantity,packing=packing,dealer=dealer,cost=cost,selling_price=selling_price,expiry_date=str(expiry_date))

	# 	stock.save()

	return stock



