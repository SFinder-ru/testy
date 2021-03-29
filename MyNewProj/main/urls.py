from django.urls import path
from .views import BBLoginView, RegisterUserView, profile, BBLogoutView


urlpatterns = [
    path('login/', BBLoginView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', BBLogoutView.as_view(), name='logout'),

]
