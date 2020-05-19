from django.contrib import admin

from .models import Course, Video, PostQA, CommentQA

admin.site.register(Course)
admin.site.register(Video)
admin.site.register(PostQA)
admin.site.register(CommentQA)
