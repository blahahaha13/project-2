from django.urls import path
from . import views

urlpatterns = [
  path('', views.landing, name='landing'),
  path('about/', views.about, name='about'),
  path('models/', views.models, name='models'),
  path('models/<int:motorcycle_id>', views.modelinfo, name='model info'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('register', views.register, name='register'),
  # path('test-stripe', views.test_stripe, name='test'),
  path('payment', views.payment, name='payment'),
 
  # path('charge/', views.charge, name='charge'),
  # path('', views.HomePageView.as_view(), name='home'),
  
  path('charge/', views.charge, name='charge'),
  path('', views.HomePageView.as_view(), name='home'),
]
