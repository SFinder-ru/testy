from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_login', 'email', 'first_name', 'created_at',
                    'updated_at')
    list_display_links = ('id', 'user_login', 'first_name')
    search_fields = ('id', 'user_login', 'first_name')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'details', 'created_at',
                    'project_html')
    list_display_links = ('id', 'project_html')
    search_fields = ('id', 'project_html')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'contacts', 'created_at',
                    'updated_at', 'project_logo', 'get_part_users', 'creator_project')
    list_display_links = ('id', 'name', 'creator_project')
    search_fields = ('id', 'name', 'creator_project')


class TechnologiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_active_area', 'get_qualification', 'get_prof_skills')
    list_display_links = ('id',)


class ActiveAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'active_area')
    list_display_links = ('id',)
    search_fields = ('id', 'active_area')


class QualificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'qualification')
    list_display_links = ('id',)
    search_fields = ('id', 'qualification')


class ProfSkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'prof_skills')
    list_display_links = ('id',)
    search_fields = ('id', 'prof_skills')


admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Technologies, TechnologiesAdmin)
admin.site.register(ActiveArea, ActiveAreaAdmin)
admin.site.register(Qualification, QualificationAdmin)
admin.site.register(ProfSkills, ProfSkillsAdmin)

# Register your models here.
