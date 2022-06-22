from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ProjectUserCreationForm
from .models import ProjectUser, ProjectRole, UserRole

class ProjectUserAdmin(UserAdmin):
    add_form = ProjectUserCreationForm
    model = ProjectUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(ProjectUser, ProjectUserAdmin)
admin.site.register(ProjectRole)
admin.site.register(UserRole)
