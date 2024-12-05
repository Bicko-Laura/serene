from django.contrib import messages
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import login

from application.forms import OrderForm


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

# def view_order(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = OrderForm(request.POST, request.FILES)
#             if form.is_valid():
#                 order = form.save(commit=False)
#                 order.user = request.user
#                 order.save()
#                 return redirect('package')
#             else:
#                 messages.error(request, 'Please fill in all the fields')
#         else:
#             form = OrderForm()
#      else:
#         return redirect('package', {'form': form })


def view_order(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OrderForm(request.POST, request.FILES)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
                return redirect('package')  # Replace 'package' with the appropriate URL name
            else:
                messages.error(request, 'Please fill in all the fields correctly.')
        else:
            form = OrderForm()
        return render(request, 'view_order.html', {'form': form})  # Replace 'order_form.html' with your template name
    else:
        messages.error(request, 'You need to be logged in to place an order.')
        return redirect('login')  # Repl