from django.shortcuts import render, redirect
from .models import ProductRequest

def home(request):
    if request.method == "POST":
        product_request = ProductRequest(
            full_name=request.POST['full_name'],
            phone_number=request.POST['phone_number'],
            country=request.POST['country'],
            address=request.POST['address']
        )
        product_request.save()
        return redirect('home')
    return render(request, 'home.html')