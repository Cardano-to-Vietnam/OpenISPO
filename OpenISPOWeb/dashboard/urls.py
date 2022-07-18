from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns=[
    path('', views.project, name ="project"),
    path('delegator/', views.delegator, name="delegator"),
    path('pool/', views.pool, name ="pool"),
    path('admin/', views.admin, name ="admin")
]