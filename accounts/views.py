from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import SignupForm


class UserLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        return "/accounts/redirect/"


class UserLogoutView(LogoutView):
    next_page = "/accounts/login/"


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def role_redirect(request):
    user = request.user
    if user.is_superuser:
        return redirect("admin_dashboard")
    if user.is_staff:
        return redirect("teacher_dashboard")
    return redirect("student_dashboard")


def _counts():
    total_users = User.objects.count()
    total_admins = User.objects.filter(is_superuser=True).count()
    total_teachers = User.objects.filter(is_staff=True, is_superuser=False).count()
    total_students = User.objects.filter(is_staff=False, is_superuser=False).count()
    recent_users = User.objects.order_by("-last_login").exclude(last_login=None)[:5]
    return {
        "total_users": total_users,
        "total_admins": total_admins,
        "total_teachers": total_teachers,
        "total_students": total_students,
        "recent_users": recent_users,
    }


@login_required
def admin_dashboard(request):
    ctx = _counts()
    return render(request, "accounts/admin_dashboard.html", ctx)


@login_required
def teacher_dashboard(request):
    # teacher view: show student count + recent logins (demo friendly)
    ctx = _counts()
    return render(request, "accounts/teacher_dashboard.html", ctx)


@login_required
def student_dashboard(request):
    # student view: placeholders for performance until analytics connects
    ctx = {
        "attendance_pct": 0,
        "avg_score": 0,
        "weak_subjects": [],
        "suggestions": [
            "Maintain regular attendance to improve consistency.",
            "Revise key topics weekly and practice previous questions.",
            "Focus more on weak subjects and attempt short quizzes."
        ],
    }
    return render(request, "accounts/student_dashboard.html", ctx)

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Account created successfully. Please login.")

            return redirect("login")

    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})