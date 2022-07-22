from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('poolregister/', views.pool_register_request_view, name='poolregister'),
    path('projectregister/', views.project_register_request_view, name='projectregister'),
    path('regisdone/', views.register_done_view, name='regis_done'),
    path('projectemailverify/(?P<prjidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.project_email_verify, name='projectemailverify'),  
    path('poolemailverify/(?P<poolidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.pool_email_verify, name='poolemailverify'),  
]

htmx_urlpatterns = [
    path('validate-pool-<subject>', views.validate_pool_subject, name='validate-pool-subject'),
    path('validate-proj-<subject>', views.validate_proj_subject, name='validate-proj-subject'),
]

urlpatterns += htmx_urlpatterns