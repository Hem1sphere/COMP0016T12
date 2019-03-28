from django.contrib import admin
from .models import Discussion,Each_discussion


class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('title','get_author')


class Each_discussionAdmin(admin.ModelAdmin):
    list_display = ('commenter','get_discussion_title')


admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Each_discussion, Each_discussionAdmin)
