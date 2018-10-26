from django.urls import path
from . import views

urlpatterns = [
  path('', views.landing, name='landing'),
  path('about/', views.about, name='about'),
  path('models/', views.models, name='models'),
  path('models/<int:model_id>/', views.modelInfo, name='model info'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('register', views.register, name='register'),
  # path('checkout/', views.checkout, name='checkout'),
]