from django.urls import path
from . import views

urlpatterns = [
    path('', views.thyroid_view, name='thyroid_form'),
]
