from django.contrib import admin
from .models import Disclaimer, PoolRegistration, ProjectRegistration

# Register your models here.

admin.site.register(Disclaimer)
admin.site.register(PoolRegistration)
admin.site.register(ProjectRegistration)
