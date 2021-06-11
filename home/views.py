from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.admin import Newsletter
from django.contrib import messages

# Create your views here.
def index(request):
  
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")

def services(request):
    return render(request, 'services.html') 

def product(request):
    return render(request, 'product.html')

def about(request):
    if request.method == "POST":
       
        email = request.POST.get('email')
           
        newsletter = Newsletter( email=email, date = datetime.today())
        newsletter.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'about.html')


# def contact(request):
#     return render(request, 'contact.html')
 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Product = request.POST.get('Product')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, Product=Product, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 