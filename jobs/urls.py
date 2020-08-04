from django.urls import path
from jobs import views

urlpatterns = [
    # GENERAL
    path('party', views.party, name='party'),
    path('party_form',views.party_form, name='submit_form'),
    # JOBS
    path('', views.portfolio, name='portfolio'),
    path('<int:pk>/detail', views.job_detail, name='job_detail'),
    # ACHIEVEMENTS
    path('achievements/', views.achievements, name='achievements'),
    path('achievements/<int:pk>/detail', views.achievement_detail, name='achievement_detail')
]
