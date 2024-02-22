from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json

# Create your views here.
def store(req):
    products = Product.objects.all()
    context = {'products' : products}
    return render(req, 'store/store.html', context)

def cart(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = {}
    context = {'items' : items, 'order' : order}
    return render(req, 'store/cart.html', context)

def checkout(req):
    context = {}
    return render(req, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)    
    productId = data['productId']
    action = data['action']
    print(f"ProductId: {productId}")
    print(f"Akcja: {action}")
    return JsonResponse('Item added ', safe=False)
