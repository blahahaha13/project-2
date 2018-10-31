from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.contrib import auth
from .models import Reciept, Motorcycle
from django.template import RequestContext
from django.contrib.auth import authenticate, login

import datetime
import stripe
stripe.api_key = 'pk_test_oWcgMJxoTjtnsREeFyHNiuOd'


def landing(request):
  return render(request, 'landing.html')

def base(request):
  return render(request, 'base.html')

def about(request):
  return render(request, 'about.html')

def models(request):
  motorcycles = Motorcycle.objects.all()
  return render(request, 'models.html', {'motorcycles': motorcycles})

def modelinfo(request, motorcycle_id):
  motorcycle = Motorcycle.objects.get(id=motorcycle_id)
  return render(request, 'modelinfo.html', {'motorcycle': motorcycle})

def charge(request):
  price = request.POST['price']
  print(price)
  if request.method == 'POST':
    charge = stripe.Charge.create(
      api_key = 'sk_test_1M26RGS2g2gWRyuKds5rp5wp',
      amount=price,
      currency='usd',
      description='Motorcycle price charge',
      source=request.POST['stripeToken']
    )
  return render(request, 'charge.html')
  

