from django.urls import path

from .views import contato, index

urlpatterns = [
    path('', index),
    path('contato',contato),
]