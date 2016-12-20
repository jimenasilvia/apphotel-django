from django.contrib import admin

# Register your models here.
from .models import Customer,Room_type,Room,Rating,Room_rating,Booking,Rent,Bill,Pay_type,Bill_payment

# Register your models here.


class AdminCustomer(admin.ModelAdmin):
	list_display = ['name','firstname','lastname','document_type','document_number','email','telephone']
	class Meta:
		model = Customer

admin.site.register(Customer,AdminCustomer)

class AdminRoom_type(admin.ModelAdmin):
	list_display = ['name_type','description']
	class Meta:
		model = Room_type

admin.site.register(Room_type,AdminRoom_type)

class AdminRating(admin.ModelAdmin):
	list_display = ['description']
	class Meta:
		model = Rating

admin.site.register(Rating,AdminRating)

class AdminPay_type(admin.ModelAdmin):
	list_display = ['pay_type']
	class Meta:
		model = Pay_type

admin.site.register(Pay_type,AdminPay_type)


class AdminRoom(admin.ModelAdmin):
	list_display = ['nro_room', 'name_type','is_reserved']
	list_filter = ['name_type','is_reserved']
	class Meta:
		model = Room

admin.site.register(Room,AdminRoom)


class AdminRoom_rating(admin.ModelAdmin):
	list_display = ['room','rating','from_date','to_date','is_active']
	class Meta:
		model = Room_rating

admin.site.register(Room_rating,AdminRoom_rating)

class AdminBooking(admin.ModelAdmin):
	list_display = ['admin','customer','reservation_date','in_date','out_date']
	list_filter = ['customer','reservation_date']
	class Meta:
		model = Booking

admin.site.register(Booking,AdminBooking)

class AdminRent(admin.ModelAdmin):
	list_display = ['name_type','amount','from_date','to_date','is_active']
	list_filter = ['is_active']
	class Meta:
		model = Rent

admin.site.register(Rent,AdminRent)


class AdminBill(admin.ModelAdmin):
    list_display = ['booking','rent']
    class Meta:
    	model = Bill

admin.site.register(Bill,AdminBill)


class AdminBill_payment(admin.ModelAdmin):
    list_display = ['bill','pay_type','payment_date']
    list_filter  = ['bill']
    class Meta:
		model = Bill_payment

admin.site.register(Bill_payment,AdminBill_payment)






