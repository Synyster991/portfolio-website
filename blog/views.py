from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages

from .models import Post, Comment


def blog(request):
    """Return blog page with all posts"""
    posts = Post.objects.all().order_by('-id')

    passing_dict = {
        'posts': posts,
    }
    return render(request, 'blog/blog.html', passing_dict)


def detail_post(request, pk):
    """Show details of the post"""
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)

    passing_dict = {
        'post': post,
        'comments': comments
    }
    return render(request, 'blog/detail_post.html', passing_dict)


def add_comment(request, pk):
    """Add comment to post"""
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['person'] and request.POST['body']:
            new_comment = Comment()
            new_comment.person = request.POST['person']
            new_comment.body = request.POST['body']
            new_comment.post_date = timezone.datetime.now()
            new_comment.post = post
            new_comment.save()

            messages.add_message(request, messages.INFO, 'Comment created!')
            return redirect('detail_post', pk)
        else:
            messages.add_message(request, messages.INFO, 'Comment is not created! All fields are required.')
            return redirect('detail_post', pk)
    else:
        return redirect('detail_post', pk)


def search_post(request):
    posts = Post.objects.all()
    search_results = []
    num_of_results = 0

    for post in posts:
        if str(post).lower().find(request.POST['search_term'].lower()) != -1:
            search_results.append(post)
            num_of_results += 1

    if not search_results:
        filtered_posts = []
        message = ["Nothing is found by this name",
                   "Unfortunately that post doesn't exists",
                   "Email Filip if you want to hear his opinion about that"]
    else:
        filtered_posts = search_results
        if num_of_results == 1:
            message = ['{} results is found'.format(num_of_results)]
        else:
            message = ['{} results are found'.format(num_of_results)]

    passing_dict = {
        'posts': filtered_posts,
        'message': message,
        'last_search': request.POST['search_term'],
        'msg_num': len(message)
    }
    return render(request, 'blog/blog.html', passing_dict)
