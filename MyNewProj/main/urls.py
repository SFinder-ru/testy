from django.urls import path
from .views import BBLoginView, RegisterUserView, profile, BBLogoutView, RegisterDoneView, user_activate


urlpatterns = [
    path('login/', BBLoginView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', BBLogoutView.as_view(), name='logout'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('register/activate/<str:sign>/', user_activate, name='register_activate')

]
