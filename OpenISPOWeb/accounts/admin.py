from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import ProjectUserCreationForm, ProjectUserChangeForm
from .models import ProjectUser


class ProjectUserAdmin(UserAdmin):
    form = ProjectUserChangeForm
    actions = None
    add_form = ProjectUserCreationForm
    model = ProjectUser
    list_display = ('email','name','status','user_type')
    list_filter = ('status','user_type',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'status','user_type',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_type', 'status')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(ProjectUser, ProjectUserAdmin)
admin.site.unregister(Group)

