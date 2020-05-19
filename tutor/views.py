from django.shortcuts import render
from tutor import models

def tutor_home(request):
    """Show home page of Tutor"""
    courses = models.Course.objects.all()

    passing_dict = {
        'courses': courses
    }
    return render(request, 'tutor/tutor_home.html', passing_dict)
