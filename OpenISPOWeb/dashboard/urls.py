from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns=[    
    path('', views.project_dashboard, name ="project_dashboard"),
    path('project_dashboard', views.project_dashboard, name ="project_dashboard"),
    path('project_contract', views.project_contract, name ="project_contract"),
    path('project_notification', views.project_notification, name ="project_notification"),
    path('pool_dashboard', views.pool_dashboard, name ="pool_dashboard"),
    path('pool_contract', views.pool_contract, name ="pool_contract"),
    path('pool_notification', views.pool_notification, name ="pool_notification"),
    path('delegator_dashboard', views.delegator_dashboard, name="delegator_dashboard"),
    path('admin/', views.admin, name ="admin")
]







