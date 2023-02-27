from django.urls import path
from . import views


app_name = 'my_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('rental_review/', views.rental_review, name='rental_review'),
    path('thank_you/', views.thank_you, name='thank_you'),
]