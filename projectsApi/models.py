import os
from uuid import uuid4
from django.db import models
from django_resized import ResizedImageField
from io import BytesIO
from PIL import Image as PilImg
from constants import *
from .utils import image_resize
from django.conf import settings

USE_S3 = settings.USE_S3


def generateUUID():
    return str(uuid4())


def get_upload_path(instance, dir, filename):
    return os.path.join(dir, filename)


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=110)

    def __str__(self):
        return self.tag


class UrlType(models.Model):
    REPO = 'repo'
    WEBSITE = 'demo'
    TYPES = [
        (REPO, ('repo')),
        (WEBSITE, ('demo'))
    ]
    urlType = models.CharField(max_length=30, choices=TYPES, blank=True)

    def __str__(self):
        return self.urlType


class UrlRoute(models.Model):
    GITHUB = 'github'
    WEBSITE = 'website'
    LINKEDIN = 'linkedin'
    TWITTER = 'twitter'
    ROUTES = [
        (GITHUB, ('Github')),
        (WEBSITE, ('Website')),
        (LINKEDIN, ('Linkedin')),
        (TWITTER, ('Twitter')),
    ]
    route = models.CharField(max_length=30, choices=ROUTES, blank=True)

    def __str__(self):
        return self.route


class Url(models.Model):
    url = models.URLField(max_length=200, editable=True)
    url_type = models.ForeignKey(
        UrlType, related_name="url_types", on_delete=models.CASCADE, blank=True, null=True)
    url_route = models.ForeignKey(
        UrlRoute, related_name="url_routes", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.url


class Video(models.Model):
    id = models.UUIDField(primary_key=True, max_length=36,
                          default=generateUUID, editable=False)
    file = models.FileField(upload_to="projects/videos",
                            null=True, verbose_name="")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.file)


class Image(models.Model):
    id = models.UUIDField(primary_key=True, max_length=36,
                          default=generateUUID, editable=False)
    # models.ImageField(upload_to="projects/images", null=True, blank=True)
    image = ResizedImageField(
        size=[1391, 2000], quality=75, upload_to='projects/images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.image)


'''
    def save(self, *args, **kwargs):
        if USE_S3:
            image_resize(self.image, 1920, 1080)
            super().save(*args, **kwargs)
        else:
            if self.image:  # check if image exists before resize
                img = PilImg.open(self.image.path)

            if img.height < 1080 or img.width < 1920:
                new_height = 1391
                new_width = 2000
                img = img.resize((new_width, new_height))
                img.save(self.image.path)
'''


class Stack(models.Model):
    stack = models.CharField(max_length=15, blank=True)
    image = ResizedImageField(
        size=[66, 66], quality=75, upload_to='projects/images/logos/stacks', null=True, blank=True)

    def __str__(self):
        return self.stack


class ProjectCategory(models.Model):
    categories = models.CharField(
        max_length=50, choices=PROJECT_CATEGORIES, blank=True)

    def __str__(self):
        return self.categories


class Project(models.Model):
    id = models.UUIDField(primary_key=True, max_length=36,
                          default=generateUUID, editable=False)
    title = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=False, null=True)
    overview = models.TextField()
    description = models.TextField(max_length=400, blank=True)
    tags = models.ManyToManyField(Tag, related_name="project_tags")
    category = models.ForeignKey(ProjectCategory, related_name='project_category',
                                 on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ForeignKey(Image, related_name='project_image',
                              on_delete=models.SET_NULL, blank=True, null=True)
    video = models.ForeignKey(Video, related_name='project_video',
                              on_delete=models.SET_NULL, blank=True, null=True)
    stacks = models.ManyToManyField(Stack, related_name="project_stacks")
    previous_project = models.ForeignKey(
        "self", related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_project = models.ForeignKey(
        "self", related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    urls = models.ManyToManyField(Url, related_name="project_urls")

    def __str__(self):
        return self.title


class Tagging(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    taggings = models.ForeignKey(Tag, on_delete=models.CASCADE)
