from django.urls import path
from . import views

urlpatterns = [
  path('', views.landing, name='landing'),
  path('about/', views.about, name='about'),
  path('models/', views.models, name='models'),
  path('models/<int:motorcycle_id>', views.modelinfo, name='model info'),
  path('charge/', views.charge, name='charge'),
]
