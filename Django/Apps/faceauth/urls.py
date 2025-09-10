from django.urls import path
from . import views

urlpatterns = [
    path('', views.faceauth, name='faceauth'),
]