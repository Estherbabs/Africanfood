from django.shortcuts import render, redirect
from django.http import HttpResponse
from afood.models import Booking
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect('bookinghistory')

    if request.method== 'GET':
        return render(request, "afood/login.html", {})
    elif request.method== 'POST':
        
        user= authenticate(
            request, 
            username= request.POST.get('username'), 
            password=request.POST.get('password'))
        if user:
            login(request, user)
            print("")
            return redirect('bookinghistory')
        else:
            return render(request, "afood/login.html", {})
            
def register(request):
    if request.user.is_authenticated:
        return redirect('bookinghistory')
    if(request.method=='POST'):
        user=User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
        )
        user.save()
        return redirect('login')
    else: 
        return render(request, "afood/register.html", {})
    
def logoutView(request):
    logout(request)
    return redirect('login')

def addbooking(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if(request.method=='POST'):
            booking=Booking.objects.create(
                date=request.POST.get('date'),
                time=request.POST.get('time'),
                user=request.user,
                mb_tables=request.POST.get('mb_tables')
            )
            return redirect('bookinghistory')
        else: 
            return render(request, "afood/add-booking.html", {})

def bookinghistory(request):
    if not request.user.is_authenticated:
        return redirect('login')
    bookings=Booking.objects.filter(user=request.user.id).order_by("-date")
    return render(request, "afood/booking-history.html", {'object': bookings})

def cancelbooking(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    
    return