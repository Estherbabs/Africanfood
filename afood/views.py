from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(request, "afood/login.html", {})

def register(request):
    return render(request, "afood/register.html", {})

def addbooking(request):
    return render(request, "afood/add-booking.html", {})

def bookinghistory(request):
    return render(request, "afood/booking-history.html", {})

def cancelbooking(request):
    return