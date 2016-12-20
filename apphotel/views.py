from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from apphotel.models import Room_type,Pay_type,Rent,Room,Rating,Room_rating,Customer,Booking,Bill,Bill_payment
from apphotel.forms import Room_typeForm,Pay_typeForm,RentForm,RoomForm,RatingForm,RRForm,TypeCustomerForm,CustomerForm,BookingForm,BillForm,Bill_paymentForm
from django.shortcuts import redirect
from django.http.response import HttpResponseRedirect

# Create your views here.

def index(request):
	titulo = 'Bienvenidos'
	if request.user.is_authenticated():
		titulo="Bienvenido, %s !" %(request.user)
	context = {
		'titulo_template':titulo
	}
	return render(request,"index.html", context)

def inicio(request):
	return HttpResponse("<h1>This is the hotel app homepage</h1>")

#Room Type

def roomtype(request):
	objs= Room_type.objects.all()
	
	context = {
		'objs':objs
	}
	return render(request,'room_type/roomtype.html', context)

def roomtype_detail(request,pk):
	obj= get_object_or_404(Room_type, pk=pk)
	rents=obj.rent_activa()
	
	return render(request,'room_type/roomtype_detail.html',{'obj': obj,'rents':rents})

def roomtype_new(request):
	if request.method == "POST":
		form = Room_typeForm(request.POST)
		if form.is_valid():
			new_obj=form.save()
			return redirect('room_type_detail', pk=new_obj.pk)
	else:
		form = Room_typeForm()
		return render(request,'room_type/roomtype_new.html', {'form':form})

def roomtype_edit(request, pk):
        obj = get_object_or_404(Room_type, pk=pk)
        if request.method == "POST":
            form = Room_typeForm(request.POST, instance=obj)
            if form.is_valid():
                obj=form.save()
                return redirect('room_type_detail', pk=obj.pk)
        else:
            form = Room_typeForm(instance=obj)
        return render(request, 'room_type/roomtype_edit.html', {'form': form})

# Pay Type
def paytype(request):
	objs= Pay_type.objects.all()
	
	context = {
		'objs':objs
	}
	return render(request,'pay_type/paytype.html', context)

def paytype_new(request):
	if request.method == "POST":
		form = Pay_typeForm(request.POST)
		if form.is_valid():
			new_obj=form.save()
			return redirect('pay_type')
	else:
		form = Pay_typeForm()
		return render(request,'pay_type/paytype_new.html', {'form':form})

def paytype_edit(request, pk):
        obj = get_object_or_404(Pay_type, pk=pk)
        if request.method == "POST":
            form = Pay_typeForm(request.POST, instance=obj)
            if form.is_valid():
                obj=form.save()
                return redirect('pay_type')
        else:
            form = Pay_typeForm(instance=obj)
        return render(request, 'pay_type/paytype_edit.html', {'form': form})
#Rent

def rent_roomtype(request, pk):
	objs=  Rent.objects.filter(name_type=pk)
	
	return render(request,'rent/rent_roomtype.html',{'objs': objs})

def rent_new(request):
	if request.method == "POST":
		form = RentForm(request.POST)
		if form.is_valid():
			new_obj=form.save()
			return HttpResponseRedirect(reverse('room_type'))
	else:
		form = RentForm()
		return render(request,'rent/rent_new.html', {'form':form})

def rent_edit(request, pk):
        obj = get_object_or_404(Rent, pk=pk)
        ident=obj.name_type_id
        if request.method == "POST":
            form = RentForm(request.POST, instance=obj)
            if form.is_valid():
                obj=form.save()
                return redirect('rent_roomtype', pk=ident)
        else:
            form = RentForm(instance=obj)
        return render(request, 'rent/rent_edit.html', {'form': form,'ident':ident})

#Room

def rooms(request):
	objs=  Room.objects.order_by('name_type')
	
	context = {
		'objs':objs
	}
	return render(request,'room/rooms.html', context)

def room_new(request):
	if request.method == "POST":
		form = RoomForm(request.POST)
		if form.is_valid():
			new_obj=form.save()
			return redirect('rooms')
	else:
		form = RoomForm()
		return render(request,'room/room_new.html', {'form':form})

def room_edit(request, pk):
        obj = get_object_or_404(Room, pk=pk)
        if request.method == "POST":
            form = RoomForm(request.POST, instance=obj)
            if form.is_valid():
                obj=form.save()
                return redirect('rooms')
        else:
            form = RoomForm(instance=obj)
        return render(request, 'room/room_edit.html', {'form': form})

#Rating

def ratings(request):
	objs=  Rating.objects.all()
	
	context = {
		'objs':objs
	}
	return render(request,'rating/ratings.html', context)

def rating_new(request):
	if request.method == "POST":
		form = RatingForm(request.POST)
		if form.is_valid():
			new_obj=form.save()
			return redirect('ratings')
	else:
		form = RatingForm()
		return render(request,'rating/rating_new.html', {'form':form})

def rating_edit(request, pk):
        obj = get_object_or_404(Rating, pk=pk)
        if request.method == "POST":
            form = RatingForm(request.POST, instance=obj)
            if form.is_valid():
                obj=form.save()
                return redirect('ratings')
        else:
            form = RatingForm(instance=obj)
        return render(request, 'rating/rating_edit.html', {'form': form})

#Room Rating
def rr(request):
	objs= Room_rating.objects.all()
	
	context = {
		'objs':objs
	}
	return render(request,'room_rating/rr.html', context)

def rr_detail(request,pk):
	obj= get_object_or_404(Room_rating, pk=pk)
	
	return render(request,'room_rating/rr_detail.html',{'obj': obj})

def rr_new(request):
	if request.method == "POST":
		form = RRForm(request.POST)
		if form.is_valid():
			new_obj=form.save()
			return redirect('rr_detail', pk=new_obj.pk)
	else:
		form = RRForm()
		return render(request,'room_rating/rr_new.html', {'form':form})

def rr_edit(request, pk):
        obj = get_object_or_404(Room_rating, pk=pk)
        if request.method == "POST":
            form = RRForm(request.POST, instance=obj)
            if form.is_valid():
                obj=form.save()
                return redirect('rr_detail', pk=obj.pk)
        else:
            form = RRForm(instance=obj)
        return render(request, 'room_rating/rr_edit.html', {'form': form})

#customer
def customers(request):
	objs=  Customer.objects.order_by('firstname')
	context = {
	  'objs':objs
	}
	return render(request,'customer/customers.html', context)	

def customer_new(request):
	if request.method == "POST":
		form = CustomerForm(request.POST)
		if form.is_valid():
			new_obj=form.save()
			return redirect('customer_detail', pk=new_obj.pk)
	else:
		form = CustomerForm()
		return render(request,'customer/customer_new.html', {'form':form})

def customer_detail(request,pk):
	obj= get_object_or_404(Customer, pk=pk)
	
	return render(request,'customer/customer_detail.html',{'obj': obj})

def customer_edit(request, pk):
        obj = get_object_or_404(Customer, pk=pk)
        if request.method == "POST":
            form = CustomerForm(request.POST, instance=obj)
            if form.is_valid():
                obj=form.save()
                return redirect('customer_detail', pk=obj.pk)
        else:
            form = CustomerForm(instance=obj)
        return render(request, 'customer/customer_edit.html', {'form': form})


#Booking
def bookings(request):
	objs=  Booking.objects.all()

	context = {
	  'objs':objs
	}
	return render(request,'booking/bookings.html', context)	

def booking_detail(request,pk):
	obj= get_object_or_404(Booking, pk=pk)
	
	return render(request,'booking/booking_detail.html',{'obj': obj})	

def booking_new(request):
	if request.method == "POST":
		form = BookingForm(request.POST)
		if form.is_valid():
			new_obj=form.save()
			return redirect('booking_detail', pk=new_obj.pk)
	else:
		form = BookingForm()
		return render(request,'booking/booking_new.html', {'form':form})

def booking_edit(request, pk):
        obj = get_object_or_404(Booking, pk=pk)
        if request.method == "POST":
            form = BookingForm(request.POST, instance=obj)
            if form.is_valid():
                obj=form.save()
                return redirect('booking_detail', pk=obj.pk)
        else:
            form = BookingForm(instance=obj)
        return render(request, 'booking/booking_edit.html', {'form': form})



#bill
def bills(request):
	objs=  Bill.objects.all()
	
	context = {
		'objs':objs
	}
	return render(request,'bill/bills.html', context)

def bill_new(request):
	if request.method == "POST":
		form = BillForm(request.POST)
		if form.is_valid():
			new_obj=form.save()
			return redirect('bills')
	else:
		form = BillForm()
		return render(request,'bill/bill_new.html', {'form':form})

def bill_edit(request, pk):
        obj = get_object_or_404(Bill, pk=pk)
        if request.method == "POST":
            form = BillForm(request.POST, instance=obj)
            if form.is_valid():
                obj=form.save()
                return redirect('bills')
        else:
            form = BillForm(instance=obj)
        return render(request, 'bill/bill_edit.html', {'form': form})

def bill_detail(request,pk):
	obj= get_object_or_404(Bill, pk=pk)
	
	return render(request,'bill/bill_detail.html',{'obj': obj})

#Bill Payment
def bills_payment(request):
	objs=  Bill_payment.objects.all()
	
	context = {
		'objs':objs
	}
	return render(request,'bill_payment/bills_payment.html', context)

def bill_payment_new(request):
	if request.method == "POST":
		form = Bill_paymentForm(request.POST)
		if form.is_valid():
			new_obj=form.save()
			return redirect('bills_payment')
	else:
		form = Bill_paymentForm()
		return render(request,'bill_payment/bill_payment_new.html', {'form':form})

def bill_payment_edit(request, pk):
        obj = get_object_or_404(Bill_payment, pk=pk)
        if request.method == "POST":
            form = Bill_paymentForm(request.POST, instance=obj)
            if form.is_valid():
                obj=form.save()
                return redirect('bills_payment')
        else:
            form = Bill_paymentForm(instance=obj)
        return render(request, 'bill_payment/bill_payment_edit.html', {'form': form})

def bill_payment_detail(request,pk):
	obj= get_object_or_404(Bill_payment, pk=pk)
	obj.set_amount_restanting
	
	return render(request,'bill_payment/bill_payment_detail.html',{'obj': obj})

#booking customer

def type_customer(request):
	if request.method == "POST":
		if request.POST.get("customer")=='1':
			return redirect('bcustomer_new')
		else:
			return redirect('bbooking_new')		
	else:
		form=TypeCustomerForm()
		return render(request, 'booking/typecustomer.html', {'form': form})

def bcustomer_new(request):
	if request.method == "POST":
		form = CustomerForm(request.POST)
		if form.is_valid():
			new_obj=form.save()
			return redirect('bbooking_new')
	else:
		form = CustomerForm()
		return render(request,'customer/customer_new.html', {'form':form})

def bbooking_new(request):
	if request.method == "POST":
		form = BookingForm(request.POST)
		if form.is_valid():
			new_obj=form.save()
			return redirect('rooms_disponibles', pk=new_obj.pk)
	else:
		form = BookingForm()
		return render(request,'booking/booking_new.html', {'form':form})

def rooms_disponibles(request,pk):
	objs=  Room.objects.filter(is_reserved=False)
	
	context = {
		'objs':objs,
		'reserva':pk
	}
	return render(request,'room/rooms_disponibles.html', context)

def room_reservar(request,pk,b):
	 obj = get_object_or_404(Room, pk=pk)
	 if request.method == "POST":
	 	form = RoomForm(request.POST, instance=obj)
	 	if form.is_valid():
	 		obj=form.save()
	 		return redirect('rooms_disponibles',b)
	 else:
	 	form = RoomForm(instance=obj)
	 	return render(request, 'room/room_new.html', {'form': form})
