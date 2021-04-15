from django.urls import path
from .views import UserLoginView, RegisterUserView, profile, UserLogoutView, UserPasswordResetView
from .views import RegisterDoneView, ChangeUserInfoView, UserPasswordChangeView
from .views import UserPasswordResetDoneView, UserPasswordResetConfirmView, UserPasswordResetCompleteView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('password/change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
