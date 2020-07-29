from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('portfolio-single/<int:pk>', views.portfolio_single, name='portfolio-single'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
]