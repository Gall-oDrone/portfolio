from django.shortcuts import render
# from rest_framework import viewsets
import os
from django.conf import settings
from django.db.models import Count, Q, Sum
from django.shortcuts import get_object_or_404, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from constants import PROJECT_CATEGORIES
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser, JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
from rest_framework import permissions, generics, viewsets
from projectsApi.models import Project, Stack, UrlType, UrlRoute, Tag, Tagging, Category, Video, Image, ProjectCategory
from .serializers import ProjectSerializer, VideoFormSerializer, ImageFormSerializer
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)

import json


# Add this CBV
class Assets(View):

    def get(self, _request, filename):
        path = os.path.join(os.path.dirname(__file__), 'static', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/javascript')
        else:
            return HttpResponseNotFound()


def set_stacks():
    try:
        if (Stack.objects and len(Stack.objects.all()) == 0):
            for s in Stack.STACKS:
                stack = Stack.objects.create(stacks=s[0])
    except Exception as e:
        print("The Stack table does not exist: ", e)


def set_url_types():
    try:
        if (UrlType.objects and len(UrlType.objects.all()) == 0):
            for ut in UrlType.TYPES:
                utype = UrlType.objects.create(urlType=ut[0])
    except Exception as e:
        print("The http url type table does not exist: ", e)


def set_url_routes():
    try:
        if (UrlRoute.objects and len(UrlRoute.objects.all()) == 0):
            for u in UrlRoute.ROUTES:
                route = UrlRoute.objects.create(route=u[0])
    except Exception as e:
        print("The http url route table does not exist: ", e)


def set_project_categories():
    try:
        if (ProjectCategory.objects and len(ProjectCategory.objects.all()) == 0):
            for c in PROJECT_CATEGORIES:
                category = ProjectCategory.objects.create(categories=c[0])
    except Exception as e:
        print("The categories table does not exist: ", e)


class ProjectListView(ListAPIView):
    queryset = Project.objects.all().order_by('created_at')
    serializer_class = ProjectSerializer
    permission_classes = (permissions.AllowAny,)
    set_project_categories()

    def tags_count():
        queryset = Project \
            .objects \
            .values("tags__tag") \
            .annotate(Count("tags__tag"))
        return queryset

    def showvideo(request):
        lastvideo = Video.objects.last()
        videofile = lastvideo.videofile
        form = VideoFormSerializer(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        context = {'videofile': videofile,
                   'form': form
                   }
        return render(request, 'Blog/videos.html', context)


class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.AllowAny,)


class ProjectCreateView(CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.AllowAny)

    def post(self, request, *args, **kwargs):
        print("request from ProjectCreateView")
        request_data = json.loads((self.request.data["data"]))
        request_files = (self.request.FILES)
        serializer = ProjectSerializer(data=request_data)
        serializer.is_valid()
        print(serializer.is_valid())
        create_article = serializer.create(request_data, request_files)
        if create_article:
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)


class ProjectDeleteView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProjectUpdateView(UpdateAPIView):
    queryset = Project.objects.all()
    print("queryset from ProjectUpdateView")
    # print(queryset)
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def update_likes_count(self, request):
        print("request from ProjectUpdateView")
        print(request.data)
        Like.objects.filter(article_id=self.request.data.get("article_id")).filter(
            user_id=self.request.data.get("user_id")).values("liked")[0]["liked"]
        Like.objects.filter(article_id=self.request.data.get(
            "article")).filter(liked=True).Count()
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid()
        print(serializer.is_valid())
        update_article = serializer.update_likes(request)
        if update_article:
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoFormSerializer
    parser_classes = (MultiPartParser, FileUploadParser, FormParser,)
    permission_classes = (permissions.AllowAny)

    def createVideo(self, request, *args, **kwargs):
        file_serializer = VideoFormSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageCreateView(CreateAPIView):
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)
    queryset = Image.objects.all()
    serializer_class = ImageFormSerializer
    permission_classes = (permissions.AllowAny,)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        imageSerializer = ImageFormSerializer(data=request.data)
        if imageSerializer.is_valid():
            imageSerializer.save()
            return Response(imageSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(imageSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDestroyView(DestroyAPIView):
    parser_classes = (MultiPartParser, FormParser,
                      FileUploadParser, JSONParser)
    queryset = Image.objects.all()
    serializer_class = ImageFormSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        print("createImage at ImageViewSet")
        print("self.request.FILES")
        print(self.request.FILES)
        print(request.objects.all())
        imageSerializer = ImageFormSerializer(data=request.data)
        if imageSerializer.is_valid():
            imageSerializer.save()
            return Response(imageSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(imageSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
