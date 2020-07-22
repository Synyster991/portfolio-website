from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from jobs import views as jobs_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # BASE URLS
    path('', jobs_views.index, name='home'),
    path('about/', jobs_views.about, name='about'),
    path('find_me', jobs_views.find_me, name='find_me'),
    path('about/send_email/', jobs_views.send_email_from_about, name='send_email_from_about'),
    path('natalie-date', jobs_views.date, name='date-natalie'),
    path('first-date', jobs_views.first_date, name='first-date'),
    # RE-DIRECT
    path('jobs/', include('jobs.urls')),
    path('blog/', include('blog.urls')),
    path('tutor/', include('tutor.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
