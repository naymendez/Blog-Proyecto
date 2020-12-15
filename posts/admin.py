from django.contrib import admin

from .models import post, PostView, Comment, Like, User

admin.site.register(post)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(User)
