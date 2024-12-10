from django.contrib import messages
from django.contrib.auth.context_processors import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import login

from application.forms import OrderForm
from application.models import Order
from panel.forms import guest


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def gallery(request):
    return render(request, 'gallery.html')
def package(request):
    return render(request, 'package.html')
def testimonial(request):
    return render(request, 'testimonial.html')

def narok(request):
    return render(request, 'narok.html')

def coast(request):
    return render(request, 'coast.html')

def central(request):
    return render(request, 'central.html')
def bookings(request):
    if request.user.is_authenticated:
     data = Order.objects.filter(user=request.user)
    else:
        data = []
    return render(request, 'bookings.html', {'data':data})





def view_order(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OrderForm(request.POST, request.FILES)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
                return redirect('package')
            else:
                messages.error(request, 'Please fill in all the fields correctly.')
        else:
            form = OrderForm()
        return render(request, 'view_order.html', {'form': form})
    else:
        messages.error(request, 'You need to be logged in to place an order.')
        return redirect('login')


@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('bookings')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

@guest
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('bookings')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

# @auth
def edit(request, id):
    order = get_object_or_404(Order, id=id)

    if request.method == 'POST':
        form = OrderForm(request.POST,  instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully!')
            return redirect('bookings')
        else:
            messages.error(request, 'Please check form details')
    else:
       form = OrderForm(instance=order)
    return render(request, 'edit.html', {'form': form,'order':order})

def delete(request, id):
    order = get_object_or_404(Order, id=id)

    try:
        order.delete()
        messages.success(request, 'Booking deleted successfully!')
        return redirect('bookings')
    except Exception as e:
        messages.error(request, 'Booking not deleted')

        return redirect('bookings')