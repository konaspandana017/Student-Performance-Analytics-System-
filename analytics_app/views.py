from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student, Mark
from .services import calculate_average, get_suggestions
from .models import Mark

@login_required
def performance_view(request):
    students = Student.objects.all()
    return render(request, 'analytics_app/performance.html', {'students': students})


@login_required
def reports_view(request):
    marks = Mark.objects.all()
    average = calculate_average(marks)
    return render(request, 'analytics_app/reports.html', {'average': average})


@login_required
def suggestions_view(request):
    marks = Mark.objects.all()
    average = calculate_average(marks)
    attendance = 80  # dummy value for review-1
    suggestion = get_suggestions(average, attendance)
    return render(request, 'analytics_app/suggestions.html', {'suggestion': suggestion})


@login_required
def admin_overview_view(request):
    context = {
        "students_count": Student.objects.count(),
        "marks_count": Mark.objects.count(),
    }
    return render(request, 'analytics_app/admin_overview.html', context)


@login_required
def admin_users_view(request):
    students = Student.objects.order_by("name")
    return render(request, 'analytics_app/admin_users.html', {'students': students})

def performance_view(request):
    marks = Mark.objects.select_related('student', 'subject')
    return render(request, 'analytics_app/performance.html', {'marks': marks})