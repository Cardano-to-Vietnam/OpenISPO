from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('poolregister/', views.pool_register_request_view, name='poolregister'),
    path('projectregister/', views.project_register_request_view, name='projectregister'),
    path('regisdone/', views.register_done_view, name='regis_done'),
]
