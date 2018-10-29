from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.contrib import auth
from .models import Reciept
from django.template import RequestContext
from django.contrib.auth import authenticate, login


import datetime
import stripe
stripe.api_key = 'pk_test_oWcgMJxoTjtnsREeFyHNiuOd'
# PUBLISHABLE_KEY = 'pk_test_oWcgMJxoTjtnsREeFyHNiuOd'

# Create your views here.

def landing(request):
  return render(request, 'landing.html')

def about(request):
  return render(request, 'about.html')

def models(request):
  return render(request, 'models.html', {'roadsters': roadsters, 'heritages': heritages})

def modelinfo(request):
  return render(request, 'modelinfo.html')

def stripe_default_form(request):
  return render(request, 'stripe_default_form.html')
def payment(request):
  return render(request, 'payment.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('landing')
    else:
      return render(request, 'form.html', {'error': 'Invalid Credentials'})
  else:
    return render(request, 'form.html')

def logout(request):
  auth.logout(request)
  return redirect('home')

def register(request):
  if request.method == 'POST':
    # Get Form Values
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')

    # Check if Passwords Match
    if password == password2:
      # Check if username exists
      if User.objects.filter(username=username).exists():
        return render(request, 'register.html', {'error': 'Username already in use'})
      else:
        # Check if email exists
        if User.objects.filter(email=email).exists():
          return render(request, 'register.html', {'error': 'Email already in use'})
        else:
          # Register User
          user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
          user.save()
          return redirect('login')
    else: 
      return render(request, 'register.html', {'error': 'Passwords do not match'})
  else: 
    return render(request, 'register.html')

class Motorcycle:
  def __init__(self, name, description, price, img):
    self.name = name
    self.description = description
    self.price = price
    self.img = img

roadsters = [
  Motorcycle('R 1200 R', "The BMW G 310 R is the essence of riding pleasure. It was built for pulsing cities and those who simply love riding motorcycles. It is maneuverable, easy to handle and sporty at the same time. Whether you're a tall or small rider, you’ll immediately feel at home on the BMW G 310 R. The bike is lightweight, yet a real powerhouse with its 313 cc engine. Get to work, the next hot spot or out of the city safely and reliably on the G 310 R. Premium quality, excellent workmanship and extraordinary technology ensure intense riding pleasure.", '$14,345', '../static/images/R_1200_R.jpg'),
  Motorcycle('S 1000 R', "Riding dynamics coupled with touring suitability - at the very highest level: that's the R 1200 RS. With its potent engine and stable suspension, the sports touring bike offers more than just a huge amount of riding pleasure. Thanks to its relaxed, sporty seating position and its perfect wind and weather protection, the bike offers an incredible ride feel when traveling fast and riding along country roads in sporty style.", '$13,995', '../static/images/S_1000_R.jpg'),
  Motorcycle('F 800 R', "The R nineT Racer lets you relive the era of legendary superbikes. Far removed from obsessive retro romanticism, but rather on a customizable bike with innovative technology and in customary BMW Motorrad quality. Crouched behind the striking half fairing, both hands tight on the low-slung handlebar grips, you can feel the powerful boxer work, you hear its unmistakable roar. And you already know: only a strong character can hold the racing line. On the road, as in life.", '$9,995', '../static/images/F_800_R.jpg'),
  Motorcycle('G 310 R', 'lorem', '$4,750', '../static/images/G_310_R.jpg')
]

heritages = [
  Motorcycle('R nineT', 'lorem', '$15,495', '../static/images/R_nineT.jpg'),
  Motorcycle('R nineT Pure', 'lorem', '$11,995', '../static/images/R_nineT_Pure.jpg'),
  Motorcycle('R nineT Racer', 'lorem', '$13,545', '../static/images/R_nineT_Racer.jpg'),
  Motorcycle('R nineT Scrambler', 'lorem', '$12,995', '../static/images/R_nineT_Scrambler.jpg'),
  Motorcycle('R ninT Urban G/S', 'lorem', '$12,995', '../static/images/R_nineT_Urban_G:s.jpg')
]


def test_stripe(request):
  stripe.api_key ='pk_test_oWcgMJxoTjtnsREeFyHNiuOd'
  # print(stripe.api_key)
  test_order = stripe.Order.create(
    currency='usd',
    items=[
      {
        "type":'sku',
        "parent":'sku_DrJitqPlmVgKYf'
      }
    ],
    shipping={
      "name":'Jenny Rosen',
      "address":{
        "line1":'1234 Main Street',
        "city":'San Francisco',
        "state":'CA',
        "country":'US',
        "postal_code":'94111'
      },
    },
    email='jenny.rosen@example.com'
  ) 

  pay_order = stripe.Order.retrieve(test_order)
  order.pay(
    source="tok_visa"
  )

  stripe.Charge.create(
    amount=2000,
    currency="usd",
    source="tok_mastercard", # obtained with Stripe.js
    description="Charge for jenny.rosen@example.com"
  )
def token_stripe(request):
  stripe.api_key ='pk_test_oWcgMJxoTjtnsREeFyHNiuOd'

  token_create = stripe.Token.create(
    card={
    "number": '4242424242424242',
    "exp_month": 12,
    "exp_year": 2019,
    "cvc": '123'
    },
  ) 

  charge_token = stripe.Token.retrieve(token_create)
  token.charge(
    source="ch_1DPy9hJ9KznIkzZEEP68FBpA"
  )
  # stripe.terminal.ConnectionToken.create()

# def charge(request):
#   test_order = stripe.Charge.create(
#     api_key = 'sk_test_1M26RGS2g2gWRyuKds5rp5wp',
#     amount=200,
#     currency="usd",
#     source="tok_amex", # obtained with Stripe.js
#     description="Charge for jenny.rosen@example.com"
#   )
#   pay_order = stripe.Order.retrieve(test_order)
#   order.pay(
#     source="tok_amex"
#   )
# transaction = Transaction(profile=request.user.profile,
#   token=token,
#   order_id=order_to_purchase.id,
#   amount=order_to_purchase.get_cart_total(),
#   sucess=True)
# transaction.save
# class HomePageView(TemplateView):
#     template_name = 'home.html'

# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['key'] = settings.STRIPE_PUBLISHABLE_KEY
#     return context


# def charge(request):
#     if request.method == 'POST':
#         charge = stripe.Charge.create(
#         amount=500,
#         currency='usd',
#         description='A Django charge',
#         source=request.POST['stripeToken']
#         )
#         return render(request, 'charge.html')
#         context_instance=RequestContext(request)

