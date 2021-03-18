from django.contrib import admin
from django.urls import path
from site_pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('chat/', views.chat),
    path('about/', views.about_us),
    path('profile/', views.user_profile)
]
