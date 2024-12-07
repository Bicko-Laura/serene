from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import  redirect, get_object_or_404

from panel.forms import guest, auth, ProfileForm, ProductForm, WorkerForm
from django.shortcuts import render
from .models import Profile, Product, Worker, send_welcome_email
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request,'home.html')
def package(request):
    return render(request, 'package.html')
def narok(request):
    return render(request, 'narok.html')

def coast(request):
    return render(request, 'coast.html')

def central(request):
    return render(request, 'central.html')

@guest
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('application/home')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})


@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('application/home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

@auth
def view_order(request):
    return render(request, 'package.html')














@auth
def edit(request, id):
    print(f"Request Method: {request.method}")
    profile = get_object_or_404(Profile, id=id)
    print(f"Profile: {profile}")
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully')
            return redirect('about')
        else:
            print(f"Form Errors: {form.errors}")
            messages.error(request, 'Please check details')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit.html', {'form': form, 'profile': profile})





@auth
def delete(request, id):
    product = get_object_or_404(Product, id=id)

    try:
        product.delete()
        messages.success(request, 'Product Succefully deleted')
    except Exception as e:
        messages.error(request, 'Productt not deleted')

    return redirect('product')







def panel_view(request):
    return render(request, 'dashboard.html')

