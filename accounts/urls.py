from django.urls import path
from .views import (
    UserLoginView,
    UserLogoutView,
    role_redirect,
    admin_dashboard,
    teacher_dashboard,
    student_dashboard,
    signup_view,   # ✅ ADD THIS
)

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),

    path("signup/", signup_view, name="signup"),  # ✅ works now

    path("redirect/", role_redirect, name="role_redirect"),

    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
    path("teacher-dashboard/", teacher_dashboard, name="teacher_dashboard"),
    path("student-dashboard/", student_dashboard, name="student_dashboard"),
]