
from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from .models import Product, CartItem
from .models import Contact
from django.http import HttpResponse
from django.contrib import messages

def home(request):

    return render(request, 'home.html')

def products(request):

    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def add_to_cart(request, product_id):
   product = get_object_or_404(Product, id=product_id)
   cart_item, created = CartItem.objects.get_or_create(product=product)
   cart_item.quantity += 1
   cart_item.save()
   # Add success message
   messages.success(request, f'{product.name} has been added to your cart.')
   return redirect('cart')

   

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('home')
    return render(request, 'contact.html')


def cart(request):
    cart_items = request.session.get('cart',{})
    products = Product.objects.filter(id__in=cart_items.keys())
    return render(request, 'cart.html', {'products':products})
