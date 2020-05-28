from django.urls import path

from tutor import views


urlpatterns = [
    path('', views.tutor_home, name='tutor_home'),
    path('search', views.search_courses, name='search_courses'),
    path('search_qa', views.search_qa, name='search_qa'),
    path('create_post', views.create_post.as_view(), name='create_post'),
    path('<int:pk>/detail', views.detail_course, name='detail_course'),
    path('<int:pk>/<int:video_pk>/play_video', views.play_video, name='play_video'),
]