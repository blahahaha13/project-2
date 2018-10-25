from django.shortcuts import render

# Create your views here.

def landing(request):
  return render(request, 'landing.html')

def about(request):
  return render(request, 'about.html')

def models(request):
  return render(request, 'models.html')

def modelInfo(request):
  return render(request, 'modelinfo.html')

def checkout(request):
  return render(request, 'form.html')