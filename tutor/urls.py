from django.urls import path

from tutor import views


urlpatterns = [
    path('', views.tutor_home, name='tutor_home'),
]