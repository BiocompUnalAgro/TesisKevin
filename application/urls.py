from django.urls import path
from application import views

urlpatterns = [
    path('/', views.Home, name='Home')
]