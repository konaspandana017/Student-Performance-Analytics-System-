from django.urls import path
from . import views

urlpatterns = [
    path('', views.performance_view, name='analytics_home'),
    path('performance/', views.performance_view, name='performance'),
    path('reports/', views.reports_view, name='reports'),
    path('suggestions/', views.suggestions_view, name='suggestions'),
    path('admin-overview/', views.admin_overview_view, name='analytics_admin_overview'),
    path('admin-students/', views.admin_users_view, name='analytics_admin_students'),
]