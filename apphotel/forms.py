from django import forms
from .models import Room_type, Pay_type,Rent,Room,Rating,Room_rating,Customer,Booking,Bill,Bill_payment
class Room_typeForm(forms.ModelForm):

        class Meta:
            model = Room_type
            fields = ('name_type', 'description',)

class Pay_typeForm(forms.ModelForm):

        class Meta:
            model = Pay_type
            fields = ('pay_type',)
class RentForm(forms.ModelForm):

        class Meta:
            model = Rent
            fields = ('name_type','amount','from_date','to_date','is_active')

class RoomForm(forms.ModelForm):

        class Meta:
            model = Room
            fields = ('nro_room','name_type','is_reserved','booking')

class RatingForm(forms.ModelForm):

        class Meta:
            model = Rating
            fields = ('description',)
class RRForm(forms.ModelForm):

        class Meta:
            model = Room_rating
            fields = ('room','rating','from_date','to_date','is_active')

CHOICES=[('1','New Customer'),
         ('2','Registered Customer')]



class TypeCustomerForm(forms.Form):
    customer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields= {'name','firstname','lastname','document_type','document_number','email','telephone','foto'}

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields= {'admin','customer','out_date'}

class BillForm(forms.ModelForm):
    class Meta:
        model=Bill
        fields= {'booking','rent','total'}

class Bill_paymentForm(forms.ModelForm):
    class Meta:
        model=Bill_payment
        fields= {'bill','pay_type','amount_paid','amount_restanting'}