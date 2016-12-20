from django.conf.urls import include, url
from . import views
urlpatterns = [
   #url(r'^$', views.inicio),
   url(r'^$', views.index, name='index'),
   url(r'^roomtype/$', views.roomtype , name="room_type"),
   url(r'^roomtype/(?P<pk>[0-9]+)/$', views.roomtype_detail, name="room_type_detail"),
   url(r'^roomtype/new/$', views.roomtype_new, name='room_type_new'),
   url(r'^roomtype/(?P<pk>[0-9]+)/edit/$', views.roomtype_edit, name='room_type_edit'),
   #pay type
   url(r'^paytype/$', views.paytype , name="pay_type"),
   url(r'^paytype/new/$', views.paytype_new, name='pay_type_new'),
   url(r'^paytype/(?P<pk>[0-9]+)/edit/$', views.paytype_edit, name='pay_type_edit'),
   #Rent
   url(r'^rentroomtype/(?P<pk>[0-9]+)/$', views.rent_roomtype, name='rent_roomtype'),
   url(r'^rentroomtype/new/$', views.rent_new, name='rent_new'),
   url(r'^rentroomtype/(?P<pk>[0-9]+)/edit/$', views.rent_edit, name='rent_edit'),
   url(r'^rooms/$', views.rooms, name='rooms'),
   url(r'^rooms/new/$', views.room_new, name='room_new'),
   url(r'^roooms/(?P<pk>[0-9]+)/edit/$', views.room_edit, name='room_edit'),
   #rating
    url(r'^ratings/$', views.ratings , name="ratings"),
    url(r'^ratings/new/$', views.rating_new, name='rating_new'),
    url(r'^ratings/(?P<pk>[0-9]+)/edit/$', views.rating_edit, name='rating_edit'),
    #room-rating
    #rating
    url(r'^rr/$', views.rr , name="rr"),
    url(r'^rr/new/$', views.rr_new, name='rr_new'),
    url(r'^rr/(?P<pk>[0-9]+)/edit/$', views.rr_edit, name='rr_edit'),
    url(r'^rr/(?P<pk>[0-9]+)/$', views.rr_detail, name="rr_detail"),
    #customer
    url(r'^customers/$', views.customers, name="customers"),
    url(r'^customer/new/$', views.customer_new, name='customer_new'),
    url(r'^customer/(?P<pk>[0-9]+)/$', views.customer_detail, name="customer_detail"),
    url(r'^customer/(?P<pk>[0-9]+)/edit/$', views.customer_edit, name='customer_edit'),
    #Booking
    url(r'^bookings/$', views.bookings, name="bookings"),
    url(r'^booking/new/$', views.booking_new, name='booking_new'),
    url(r'^booking/(?P<pk>[0-9]+)/$', views.booking_detail, name="booking_detail"),
    url(r'^booking/(?P<pk>[0-9]+)/edit/$', views.booking_edit, name='booking_edit'),
    #Bill
    url(r'^bills/$', views.bills , name="bills"),
    url(r'^bills/new/$', views.bill_new, name='bill_new'),
    url(r'^bills/(?P<pk>[0-9]+)/edit/$', views.bill_edit, name='bill_edit'),
    url(r'^bills/(?P<pk>[0-9]+)/$', views.bill_detail, name="bill_detail"),

    #Bill Payment
    url(r'^bills_payment/$', views.bills_payment , name="bills_payment"),
    url(r'^bills_payment/new/$', views.bill_payment_new, name='bill_payment_new'),
    url(r'^bills_payment/(?P<pk>[0-9]+)/edit/$', views.bill_payment_edit, name='bill_payment_edit'),
    url(r'^bills_payment/(?P<pk>[0-9]+)/$', views.bill_payment_detail, name="bill_payment_detail"),

   #booking-Customer
    url(r'^booking/typecustomer/$', views.type_customer, name='type_customer'),
    url(r'^booking/customer/new/$', views.bcustomer_new, name='bcustomer_new'),
    url(r'^booking/booking/new/$', views.bbooking_new, name='bbooking_new'),
    url(r'^booking/roomsdisponibles/(?P<pk>[0-9]+)/$', views.rooms_disponibles, name='rooms_disponibles'),
    url(r'^booking/roomsdisponibles/reservar/(?P<pk>[0-9]+)/(?P<b>[0-9]+)/$', views.room_reservar, name='room_reservar'),
   



]
