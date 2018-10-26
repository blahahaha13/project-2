from django.urls import path
from . import views

urlpatterns = [
  path('', views.landing, name='landing'),
  path('about/', views.about, name='about'),
  path('models/', views.models, name='models'),
  path('models/<int:model_id>/', views.modelinfo, name='model info'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('register', views.register, name='register'),
  path('test-stripe', views.test_stripe, name='test'),
  path('checkout', views.checkout, name='checkout'),
  path('stripe_default_form', views.stripe_default_form, name='stripe_default_form'),

  # path('checkout/', views.checkout, name='checkout'),
]