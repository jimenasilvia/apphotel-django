from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import date, datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your models here.
DOCUMENT_TYPE = (
    ('d','DNI'),
    ('p','Pasaporte'),
    ('o','Otro'),
    )

class Customer(models.Model):
	name =models.CharField(max_length=50)
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	document_type = models.CharField(max_length=1, choices=DOCUMENT_TYPE, verbose_name='Document Type')
	document_number = models.CharField(max_length=16, verbose_name='Document Number')
	email = models.EmailField(max_length=256,blank=True)
	telephone = models.CharField(max_length=15,blank=True)
	foto = models.ImageField(upload_to="migrations", verbose_name='Foto', null=True, blank=True)

	def __unicode__(self):
		return '{0} {1} {2}'.format(self.name,self.firstname,self.lastname)

class Room_type(models.Model):
	name_type=models.CharField(verbose_name='Room Type',max_length=15)
	description=models.TextField(blank=True)

	def __unicode__(self):
		return self.name_type

	def rent_activa(self):
		fecha = datetime.now().date()
		return Rent.objects.filter(name_type=self.id,is_active=True,from_date__lte=timezone.now(),to_date__gte=timezone.now())



class Pay_type(models.Model):
	pay_type=models.CharField(max_length=12,verbose_name='Pay Type')

	def __unicode__(self):
		return self.pay_type

class Rating(models.Model):
	description=models.TextField(verbose_name='Rating')

	def __unicode__(self):
		return self.description

class Rent(models.Model):
    name_type=models.ForeignKey(Room_type,verbose_name='Room Type')
    amount=models.DecimalField( default=0, max_digits=10, decimal_places=3)
    from_date=models.DateTimeField()
    to_date=models.DateTimeField()
    is_active=models.BooleanField()

    def __unicode__(self):
		return '{0} {1}'.format(self.name_type,self.amount)

	

class Booking(models.Model):
    admin=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    reservation_date=models.DateTimeField(auto_now_add=True)
    in_date=models.DateTimeField(auto_now_add=True)
    out_date=models.DateTimeField()

   

    def __unicode__(self):
        return 'Booking#{0}'.format(self.id)

    def id_customer(self):
		return str(self.customer).split('-')[1]


class Room(models.Model):
	nro_room=models.CharField(max_length=3)
	name_type=models.ForeignKey(Room_type,verbose_name='Room Type')
	is_reserved=models.BooleanField()
	booking=models.ForeignKey(Booking,blank=True,null=True,on_delete=models.DO_NOTHING)


	def __unicode__(self):
		return self.nro_room


class Room_rating(models.Model):
     room=models.ForeignKey(Room,verbose_name='Room',default=1)
     rating=models.ForeignKey(Rating,blank=True,null=True)
     from_date=models.DateTimeField()
     to_date=models.DateTimeField()
     is_active=models.BooleanField()
     def __unicode__(self):
		return '{0}'.format(self.room)

class Bill(models.Model):
	booking=models.ForeignKey(Booking)
	rent=models.ForeignKey(Rent)
	total=models.DecimalField(default=0, max_digits=10, decimal_places=3)

	def __unicode__(self):
		return "Bill #{0}".format(self.id)
	@property
	def set_total(self):
		rent = get_object_or_404(Rent, pk=self.rent_id)
		numero=Room.objects.filter(name_type=rent.name_type,booking=self.booking).count()
		self.total = numero*rent.amount
		self.save()


class Bill_payment(models.Model):
	bill=models.ForeignKey(Bill,blank=True,null=True)
	pay_type=models.ForeignKey(Pay_type,blank=True,null=True,on_delete=models.DO_NOTHING)
	payment_date=models.DateTimeField(auto_now_add=False,auto_now=True)
	amount_paid=models.DecimalField(default=0, max_digits=10, decimal_places=3)
	amount_restanting=models.DecimalField(default=0, max_digits=10, decimal_places=3)
	
	def __unicode__(self):
		return "Payment #{0}".format(self.id)
	@property
	def set_amount_restanting(self):
		bill = get_object_or_404(Bill, pk=self.bill_id)
		self.amount_restanting = bill.total-self.amount_paid
		self.save()

##'''