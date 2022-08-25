from django.contrib import admin

from .models import (
    Project, Tag, Tagging, Category,
    Image, Video, Url, Stack, UrlType,
    UrlRoute, ProjectCategory
)

# class RatingAdmin(admin.ModelAdmin):
#     readonly_fields = ('upload_time')

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Tagging)
admin.site.register(Category)
admin.site.register(ProjectCategory)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Url)
admin.site.register(UrlType)
admin.site.register(UrlRoute)
admin.site.register(Stack)
