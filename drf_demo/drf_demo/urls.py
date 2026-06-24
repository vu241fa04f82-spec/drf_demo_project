from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to DRF Demo Student API Project")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('student/', include('student_app.urls')),
]