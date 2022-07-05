from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('poolregister/', views.pool_register_request_view, name='poolregister'),
    path('projectregister/', views.project_register_request_view, name='projectregister'),
    path('regisdone/', views.register_done_view, name='regis_done'),
]

htmx_urlpatterns = [
    path('validate-pool-<subject>', views.validate_pool_subject, name='validate-pool-subject'),
    path('validate-proj-<subject>', views.validate_proj_subject, name='validate-proj-subject'),
]

urlpatterns += htmx_urlpatterns