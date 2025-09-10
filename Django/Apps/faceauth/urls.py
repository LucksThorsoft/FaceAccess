from django.urls import path
from . import views

urlpatterns = [
    path('faceauth/', views.faceauth, name='faceauth'),
]