from django.urls import path
from jobs import views

urlpatterns = [
    # JOBS
    path('', views.portfolio, name='portfolio'),
    path('<int:pk>/detail', views.job_detail, name='job_detail'),
    # ACHIEVEMENTS
    path('achievements/', views.achievements, name='achievements'),
    path('achievements/<int:pk>/detail', views.achievement_detail, name='achievement_detail')
]
