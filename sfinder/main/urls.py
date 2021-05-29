from django.urls import path, re_path
from allauth.account import views
from .views import *

urlpatterns = [
    path('login/',
         views.login,
         name='account_login'),

    path('signup/',
         views.signup,
         name='account_signup'),

    path('profile/',
         profile,
         name='profile'),

    path('project/<int:pk>/',
         ViewProject.as_view(),
         name='project'),

    path('projects/',
         ViewAllProjects.as_view(),
         name='all_projects'),

    path('create_project/',
         create_project,
         name='create_project'),

    path('logout/',
         views.logout,
         name='account_logout'),

    path('profile/email/',
         views.email,
         name='account_email'),

    path(
        'confirm-email/',
        views.email_verification_sent,
        name='account_email_verification_sent',
    ),

    re_path(
        r'^confirm-email/(?P<key>[-:\w]+)/$',
        views.confirm_email,
        name='account_confirm_email',
    ),

    path('profile/change/', 
         ChangeUserInfoView.as_view(), 
         name='profile_change'),

    path('password/change/', 
         UserPasswordChangeView.as_view(), 
         name='password_change'),

    path('password_reset/', 
         UserPasswordResetView.as_view(), 
         name='password_reset'),

    path('password_reset/done/', 
         UserPasswordResetDoneView.as_view(), 
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
         UserPasswordResetConfirmView.as_view(), 
         name='password_reset_confirm'),

    path('password/reset/complete/', 
         UserPasswordResetCompleteView.as_view(), 
         name='password_reset_complete'),
]
