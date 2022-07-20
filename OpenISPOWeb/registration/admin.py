from django.contrib import admin
from .models import Disclaimer, PoolRegistration, ProjectRegistration
from .forms import ProjectRegistrationForm, PoolRegistrationForm

# Register your models here.

class ProjectRegistrationAdmin(admin.ModelAdmin):
    model = ProjectRegistration
    actions = None
    add_form = ProjectRegistrationForm
    list_display = ('token_name','token_num','email','phone','start_time','end_time','create_time','status')
    list_filter = ('status',)
    search_fields = ('token_name',)
    ordering = ('token_name',)

class PoolRegistrationAdmin(admin.ModelAdmin):
    model = PoolRegistration
    actions = None
    add_form = PoolRegistrationForm
    list_display = ('pool_name','pool_id','email','phone','create_time','status')
    list_filter = ('status',)
    search_fields = ('pool_name',)
    ordering = ('pool_name',)


admin.site.register(ProjectRegistration, ProjectRegistrationAdmin)
admin.site.register(PoolRegistration, PoolRegistrationAdmin)
# admin.site.register(Disclaimer)
