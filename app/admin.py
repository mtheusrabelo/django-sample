from django.contrib import admin
from .models import Project, Comment, Tag

admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Tag)
