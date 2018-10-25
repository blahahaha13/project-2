from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Reciept
# Create your views here.

def landing(request):
  return render(request, 'landing.html')

def about(request):
  return render(request, 'about.html')

def models(request):
  return render(request, 'models.html', {'motorcycles': motorcycles})

def modelInfo(request):
  return render(request, 'modelinfo.html')

def checkout(request):
  return render(request, 'form.html')


class Motorcycle:
  def __init__(self, name, description, price, img):
    self.name = name
    self.description = description
    self.price = price
    self.img = img

motorcycles = [
  Motorcycle('S 1000 R', "The BMW G 310 R is the essence of riding pleasure. It was built for pulsing cities and those who simply love riding motorcycles. It is maneuverable, easy to handle and sporty at the same time. Whether you're a tall or small rider, you’ll immediately feel at home on the BMW G 310 R. The bike is lightweight, yet a real powerhouse with its 313 cc engine. Get to work, the next hot spot or out of the city safely and reliably on the G 310 R. Premium quality, excellent workmanship and extraordinary technology ensure intense riding pleasure.", '$4,750', 'http://stat.overdrive.in/wp-content/uploads/2018/06/BMW-G-310-R.jpg'),
  Motorcycle('R 1200 RS', "Riding dynamics coupled with touring suitability - at the very highest level: that's the R 1200 RS. With its potent engine and stable suspension, the sports touring bike offers more than just a huge amount of riding pleasure. Thanks to its relaxed, sporty seating position and its perfect wind and weather protection, the bike offers an incredible ride feel when traveling fast and riding along country roads in sporty style.", '$15,245', 'http://www.motorcycle.com/blog/wp-content/uploads/2014/09/093014-2015-bmw-r1200rs-f.jpg'),
  Motorcycle('R nineT Racer', "The R nineT Racer lets you relive the era of legendary superbikes. Far removed from obsessive retro romanticism, but rather on a customizable bike with innovative technology and in customary BMW Motorrad quality. Crouched behind the striking half fairing, both hands tight on the low-slung handlebar grips, you can feel the powerful boxer work, you hear its unmistakable roar. And you already know: only a strong character can hold the racing line. On the road, as in life.", '$13,545', 'https://www.brm.co.nz/wp-content/uploads/2018/01/140A8756.jpg'),
]









