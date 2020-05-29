from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from tutor import models


def tutor_home(request):
    """Show home page of Tutor"""
    courses = models.Course.objects.all()
    posts = models.PostQA.objects.all()

    passing_dict = {
        'courses': courses,
        'posts': posts,
    }
    return render(request, 'tutor/tutor_home.html', passing_dict)


def detail_course(request, pk):
    course = models.Course.objects.get(pk=pk)
    videos = models.Video.objects.filter(course=course)
    show_video = videos[0]

    passing_dict = {
        'course': course,
        'videos': videos,
        'show_video': show_video,
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
    posts = models.PostQA.objects.all()
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
        'posts': posts,
        'num_of_results': num_of_results,
        'message_type': message_type,
        'message': message
    }
    return render(request, 'tutor/tutor_home.html', passing_dict)


def search_qa(request):
    """Search for existing post"""
    posts = models.PostQA.objects.all()
    search_result = []
    nums_of_results = 0

    if not request.POST['search_value_qa']:
        return redirect('tutor_home')
    for post in posts:
        if str(post).lower().find(request.POST['search_value_qa'].lower()) != -1:
            search_result.append(post)
            nums_of_results += 1
        elif post.body.lower().find(request.POST['search_value_qa'].lower()) != -1:
            search_result.append(post)
            nums_of_results += 1
        else:
            comments = models.CommentQA.objects.filter(post=post)
            for comment in comments:
                if str(comment).lower().find(request.POST['search_value_qa'].lower()) != -1:
                    search_result.append(post)
                    nums_of_results += 1

    if search_result:
        posts = search_result
        message_type = 'success_qa'
        if nums_of_results == 1:
            message = ['{} results is found'.format(nums_of_results)]
        else:
            message = ['{} results are found'.format(nums_of_results)]
    else:
        message_type = 'error_qa'
        message = ["Unfortunately that content doesn't exists"]

    passing_dict = {
        'posts': posts,
        'nums_of_results': nums_of_results,
        'message_type': message_type,
        'message_qa': message
    }
    return render(request, 'tutor/tutor_home.html', passing_dict)


def question_detail(request, post_pk):
    """Show details of question"""
    post = models.PostQA.objects.get(pk=post_pk)
    comments = models.CommentQA.objects.filter(post=post)

    passing_dict = {
        'post': post,
        'comments': comments
    }
    return render(request, 'tutor/detail_question.html', passing_dict)


def add_comment(request, post_pk):
    """Create Comment for a post"""
    post = models.PostQA.objects.get(pk=post_pk)

    if request.method == 'POST':
        if request.POST['name_field'] and request.POST['comment_field']:
            temp_comment = models.CommentQA()
            temp_comment.person = request.POST['name_field']
            temp_comment.body = request.POST['comment_field']
            temp_comment.post = post
            temp_comment.save()

            return redirect('question_detail', post_pk)
        else:
            return redirect('question_detail', post_pk)
    else:
        return redirect('question_detail', post_pk)


class create_post(generic.CreateView):
    """Create Post"""
    model = models.PostQA
    fields = ['title', 'person', 'body', 'source_link']
    template_name = 'tutor/tutor_home.html'
    success_url = reverse_lazy('tutor_home')




