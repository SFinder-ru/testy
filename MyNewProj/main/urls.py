from django.urls import path
from .views import BBLoginView, RegisterUserView


urlpatterns = [
    path('login/', BBLoginView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register')
]
