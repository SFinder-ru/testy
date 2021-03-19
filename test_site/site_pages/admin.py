from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_login', 'email', 'first_name', 'created_at',
                    'updated_at')
    list_display_links = ('id', 'user_login', 'first_name')
    search_fields = ('id', 'user_login', 'first_name')


admin.site.register(User, UserAdmin)

# Register your models here.
