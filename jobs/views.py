from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail

from .models import Job, Achievement


def handler404(request, *args, **argv):
    response = render('404.html')
    response.status_code = 404
    return response


def index(request):
    """Redirect to index page and return 3 jobs"""
    jobs = Job.objects.all().order_by('-id')[:3]

    passing_dict = {
        'jobs': jobs
    }
    return render(request, 'jobs/index.html', passing_dict)


def about(request):
    return render(request, 'jobs/about.html')


def find_me(request):
    subject = 'Find Me Feature Activated'
    message = 'Someone is spying on you. O.O'
    sender = 'f_dimitrievski@outlook.com'
    receiver = ['filipdimi1999@gmail.com']
    send_mail(subject, message, sender, receiver)

    return render(request, 'jobs/find_me.html')


def portfolio(request):
    """Redirect to portfolio and return all jobs """
    jobs = Job.objects.all().order_by('-id')

    passing_dict = {
        'jobs': jobs
    }
    return render(request, 'jobs/portfolio.html', passing_dict)


def job_detail(request, pk):
    """Showing detail of a job"""
    job = get_object_or_404(Job, pk=pk)

    passing_dict = {
        'job': job
    }
    return render(request, 'jobs/job_detail.html', passing_dict)


def achievements(request):
    """Redirect to achievements and list them"""
    achievements_all = Achievement.objects.all().order_by('-id')

    passing_dict = {
        'achievements': achievements_all
    }
    return render(request, 'jobs/achievements.html', passing_dict)


def achievement_detail(request, pk):
    """Showing detail of a achievement"""
    achievement = get_object_or_404(Achievement, pk=pk)

    passing_dict = {
        'achievement': achievement
    }
    return render(request, 'jobs/achievement_detail.html', passing_dict)


def send_email_from_about(request):
    """Send email with gmail services"""
    subject = 'Wave from Portfolio About'
    message = 'from: {} \n\n{}'.format(request.POST['guest_email'], request.POST['guest_msg'])
    sender = 'f_dimitrievski@outlook.com'
    receiver = ['filipdimi1999@gmail.com']

    auto_reply_subject = 'Auto-reply from filipdimitrievski.com'
    auto_reply_message = 'Thank you for contacting me. \nI will reply as soon as possible. \n\nRegards, \nFilip ' \
                         'Dimitrievski'
    auto_reply_receiver = [request.POST['guest_email']]

    send_mail(subject, message, sender, receiver)
    send_mail(auto_reply_subject, auto_reply_message, sender, auto_reply_receiver)

    return redirect('about')


def date(request):
    return render(request, 'jobs/date.html')
