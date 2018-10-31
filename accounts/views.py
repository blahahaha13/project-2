from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

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
