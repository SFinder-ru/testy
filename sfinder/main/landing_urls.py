from django.urls import path

from .views import landing_index, landing_about

urlpatterns = [
    path('', landing_index),
    path('about/', landing_about),
]