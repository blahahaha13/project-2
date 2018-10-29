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
# PUBLISHABLE_KEY = 'pk_test_oWcgMJxoTjtnsREeFyHNiuOd'

# Create your views here.

def landing(request):
  return render(request, 'landing.html')

def about(request):
  return render(request, 'about.html')

def models(request):
  motorcycles = Motorcycle.objects.all()
  return render(request, 'models.html', {'motorcycles': motorcycles})

def modelinfo(request, motorcycle_id):
  motorcycle = Motorcycle.objects.get(id=motorcycle_id)
  return render(request, 'modelinfo.html', {'motorcycle': motorcycle})

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

# class Motorcycle:
#   def __init__(self, name, description, price, img):
#     self.name = name
#     self.description = description
#     self.price = price
#     self.img = img

# roadsters = [
#   m = Motorcycle(name='R 1200 R', description="The BMW G 310 R is the essence of riding pleasure. It was built for pulsing cities and those who simply love riding motorcycles. It is maneuverable, easy to handle and sporty at the same time. Whether you're a tall or small rider, you’ll immediately feel at home on the BMW G 310 R. The bike is lightweight, yet a real powerhouse with its 313 cc engine. Get to work, the next hot spot or out of the city safely and reliably on the G 310 R. Premium quality, excellent workmanship and extraordinary technology ensure intense riding pleasure", price=14345, img='../static/images/R_1200_R.jpg'),
#   s = Motorcycle(name='S 1000 R', description="Riding dynamics coupled with touring suitability - at the very highest level: that's the R 1200 RS. With its potent engine and stable suspension, the sports touring bike offers more than just a huge amount of riding pleasure. Thanks to its relaxed, sporty seating position and its perfect wind and weather protection, the bike offers an incredible ride feel when traveling fast and riding along country roads in sporty style", price=13995, img='../static/images/S_1000_R.jpg'),
#   x = Motorcycle(name='F 800 R', description="The R nineT Racer lets you relive the era of legendary superbikes. Far removed from obsessive retro romanticism, but rather on a customizable bike with innovative technology and in customary BMW Motorrad quality. Crouched behind the striking half fairing, both hands tight on the low-slung handlebar grips, you can feel the powerful boxer work, you hear its unmistakable roar. And you already know: only a strong character can hold the racing line. On the road, as in life.", price=9995, img='../static/images/F_800_R.jpg'),
#   f = Motorcycle(name='G 310 R', description="The BMW G 310 R is the essence of riding pleasure. It was built for pulsing cities and those who simply love riding motorcycles. It is maneuverable, easy to handle and sporty at the same time. Whether you're a tall or small rider, you’ll immediately feel at home on the BMW G 310 R. The bike is lightweight, yet a real powerhouse with its 313 cc engine. Get to work, the next hot spot or out of the city safely and reliably on the G 310 R. Premium quality, excellent workmanship and extraordinary technology ensure intense riding pleasure, price=4750, img='../static/images/G_310_R.jpg')
# ]

# heritages = [
#   a = Motorcycle(name='R nineT', description="Motorcycling is a sign of pure freedom: landscape, corners, straights, every mile counts. If this is the path you have chosen, the R nineT is the perfect companion and knows hardly any limits when it comes to your personal fulfillment thanks to its countless customization possibilities. The character of its air-cooled boxer engine, combined with its state-of-the-art technology, irresistibly propels you forward in a way that can be clearly felt with its full torque curve. Right from the start, the R nineT has enthralled, inspired and stimulated motorcycling enthusiasts around the world", price=15495, img='../static/images/R_nineT.jpg'),
#   b = Motorcycle(name='R nineT Pure', description='The BMW R nineT Pure is perfect for everyone who loves the classic roadster design and is looking for a pure motorcycle experience. The design draws its inspiration directly from the first motorcycles. It is reminiscent of the era of the 1970's and 80's. But its roots go deeper. Even the very first motorcycle from BMW was simple, reduced and dynamic. Already in 1923 the heart of the entire concept was the BMW opposed-twin engine. At the same time, it offers you many options to customise your motorcycle. You can realize your dreams: of your bike and your lifestyle. You will feel where it comes from Whether you're customising it or enjoying the thrill of opening the throttle', price=11995, img='../static/images/R_nineT_Pure.jpg')
#   c = Motorcycle(name='R nineT Racer', description='The R nineT Racer lets you relive the era of legendary superbikes. Far removed from obsessive retro romanticism, but rather on a customizable bike with innovative technology and in customary BMW Motorrad quality. Crouched behind the striking half fairing, both hands tight on the low-slung handlebar grips, you can feel the powerful boxer work, you hear its unmistakable roar. And you already know: only a strong character can hold the racing line. On the road, as in life', price=13545, img='../static/images/R_nineT_Racer.jpg')
#   d = Motorcycle(name='R nineT Scrambler', description='Feel the wind, lean into every curve and experience the freedom in every mile you ride – the BMW R nineT Scrambler empowers you to do your own thing. It’s rugged bike with an authentic scrambler look, combined with the innovative technology and familiar quality of BMW Motorrad. Whether in the city, on winding country roads or on the beach, the potent opposed-twin engine and high-positioned dual silencers deliver powerful acceleration and an unmistakable sound. Even long trips with two people are a breeze thanks to the relaxed seating position. In just a few steps you can also give your R nineT Scrambler your own personal touch', price=12995, img='../static/images/R_nineT_Scrambler.jpg')
#   e = Motorcycle(name='R ninT Urban G/S', description='Enjoy the confident feel of a boxer with an upright and relaxed riding position, coupled with modern technology. Choose from countless customizing options to integrate your own unique ideas. The R nineT Urban G/S makes a clear statement: It pays tribute to the early days of BMW Motorrad's G/S success story. Just one look and it's clear that the R nineT Urban G/S captures the off-road spirit of that era. At the same time, its riding characteristics make it a true member of today's R nineT family', price=12995, img='../static/images/R_nineT_Urban_G:s.jpg')
# ]


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

