from django.contrib import admin
from django.urls import path
from site_pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('chat/', views.chat),
    path('about/', views.about_us),
    path('profile/', views.user_profile)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)