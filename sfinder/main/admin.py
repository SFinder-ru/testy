from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email',
                    'is_superuser', 'is_staff', 'is_active', 'last_login',
                    'date_joined', 'get_fav_users',
                    'get_part_projects', 'get_fav_projects', 'job_desc')
    list_display_links = ('id', 'username', 'email')
    search_fields = ('id', 'username', 'email')
    exclude = ['groups', 'user_permissions', 'last_login',
               'date_joined']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'details', 'created_at',
                    'project_html')
    list_display_links = ('id', 'project_html')
    search_fields = ('id', 'project_html')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'contacts', 'created_at',
                    'updated_at', 'get_part_users', 'get_creators', 'get_comments')
    list_display_links = ('id', 'name', 'get_creators')
    search_fields = ('id', 'name', 'get_creators')


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


class RolesAdmin(admin.ModelAdmin):
    list_display = ('id', 'role')
    list_display_links = ('id',)


admin.site.register(AdvUser, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Technologies, TechnologiesAdmin)
admin.site.register(ActiveArea, ActiveAreaAdmin)
admin.site.register(Qualification, QualificationAdmin)
admin.site.register(ProfSkills, ProfSkillsAdmin)

