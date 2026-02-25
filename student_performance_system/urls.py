from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('login')
urlpatterns = [
    path('', home_redirect),  # THIS fixes 404 at /
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]