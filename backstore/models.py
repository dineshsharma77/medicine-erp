from django.db import models
# Create your models here.

class Brand(models.Model):
	name = models.CharField(max_length=200)

class Dealer(models.Model):
	name = models.CharField(max_length=100)
	contact = models.IntegerField()
	address = models.CharField(max_length=200)

class Staff(models.Model):
	name = models.CharField(max_length=100)
	contact = models.IntegerField()
	address = models.CharField(max_length=200)


class Medicine(models.Model):
	name = models.CharField(max_length=200)
	dealer = models.ForeignKey(Dealer,on_delete=models.CASCADE)
	brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
	quantity = models.IntegerField()
	packing = models.IntegerField()
	cost = models.IntegerField()
	selling_price = models.IntegerField()
	expiry_date = models.DateField()
	batch_no = models.CharField(max_length=100)

class User(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=100)
	dob = models.DateField()