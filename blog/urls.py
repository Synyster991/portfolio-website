from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pk>/detail', views.detail_post, name='detail_post'),
    path('<int:pk>/add_comment', views.add_comment, name='add_comment'),
]

