from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.register_request, name='register'),
    path('logindone/',views.login_done, name='logindone'),
]
