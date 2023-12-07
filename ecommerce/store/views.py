from django.shortcuts import render

# Create your views here.
def store(req):
    context = {}
    return render(req, 'store/store.html', context)

def cart(req):
    context = {}
    return render(req, 'store/cart.html', context)

def checkout(req):
    context = {}
    return render(req, 'store/checkout.html', context)
