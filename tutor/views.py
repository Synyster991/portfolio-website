from django.shortcuts import render, redirect
from django.contrib import messages
from tutor import models


def tutor_home(request):
    """Show home page of Tutor"""
    courses = models.Course.objects.all()

    passing_dict = {
        'courses': courses
    }
    return render(request, 'tutor/tutor_home.html', passing_dict)


def detail_course(request, pk):
    course = models.Course.objects.get(pk=pk)
    videos = models.Video.objects.filter(course=course)

    passing_dict = {
        'course': course,
        'videos': videos,
        'show_video': videos[0],
    }
    return render(request, 'tutor/detail_course.html', passing_dict)


def play_video(request, pk, video_pk):
    course = models.Course.objects.get(pk=pk)
    videos = models.Video.objects.filter(course=course)
    show_video = models.Video.objects.get(pk=video_pk)

    passing_dict = {
        'course': course,
        'videos': videos,
        'show_video': show_video,
    }
    return render(request, 'tutor/detail_course.html', passing_dict)


def search_courses(request):
    """Find a course or video by user search value"""
    courses = models.Course.objects.all()
    search_result = []
    num_of_results = 0

    if not request.POST['search_value']:
        return redirect('tutor_home')
    for course_counter in courses:
        temp_videos = models.Video.objects.filter(course=course_counter)
        if str(course_counter).lower().find(request.POST['search_value'].lower()) != -1:
            search_result.append(course_counter)
            num_of_results += 1
        else:
            for video in temp_videos:
                if str(video).lower().find(request.POST['search_value'].lower()) != -1:
                    search_result.append(course_counter)
                    num_of_results += 1

    if search_result:
        courses = search_result
        message_type = 'success'
        if num_of_results == 1:
            message = ['{} results is found'.format(num_of_results)]
        else:
            message = ['{} results are found'.format(num_of_results)]
    else:
        message_type = 'error'
        message = ["Unfortunately that content doesn't exists"]

    passing_dict = {
        'courses': courses,
        'num_of_results': num_of_results,
        'message_type': message_type,
        'message': message
    }
    return render(request, 'tutor/tutor_home.html', passing_dict)