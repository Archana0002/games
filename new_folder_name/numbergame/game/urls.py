from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.start_game, name='start'),
    path('guess/', views.guess, name='guess'),
]
