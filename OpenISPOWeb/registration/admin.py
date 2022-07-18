from django.contrib import admin
from .models import Disclaimer, PoolRegistration, ProjectRegistration
from .forms import ProjectRegistrationForm

# Register your models here.

class ProjectRegistrationAdmin(admin.ModelAdmin):
    model = ProjectRegistration
    actions = None
    add_form = ProjectRegistrationForm
    list_display = ('token_name','token_num','email','phone','start_time','end_time','create_time','status')
    list_filter = ('status',)
    search_fields = ('token_name',)
    ordering = ('token_name',)


admin.site.register(ProjectRegistration, ProjectRegistrationAdmin)
# admin.site.register(PoolRegistration)
# admin.site.register(Disclaimer)
