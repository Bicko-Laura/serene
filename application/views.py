from django.shortcuts import render

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