from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ProjectUserCreationForm
from .models import ProjectUser


class ProjectUserAdmin(UserAdmin):
    add_form = ProjectUserCreationForm
    model = ProjectUser
    list_display = ('email','phone',)
    list_filter = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Permissions', {'fields': ()}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(ProjectUser, ProjectUserAdmin)
# admin.site.register(Disclaimer)
# admin.site.register(PoolRegis)
# admin.site.register(ProjectRegis)
# admin.site.register(MatchingProjectPool)
