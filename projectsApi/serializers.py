from random import choices
from constants import PROJECT_CATEGORIES
from rest_framework import serializers
from projectsApi.models import Project, Video, Stack, Tag, Url, Image, UrlRoute, ProjectCategory
from django.core.files.storage import FileSystemStorage
import json


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class ProjectSerializer(serializers.ModelSerializer):
    id = StringSerializer(many=False)
    tags = StringSerializer(many=True)
    overview = StringSerializer(many=False)
    description = StringSerializer(many=False)
    stacks = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    urls = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    def get_stacks(self, instance):
        request = self.context.get('request')
        stacks = ProjectStackSerializer(instance.stacks, many=True, context={
                                        'request': request}).data
        return stacks

    def get_category(self, instance):
        request = self.context.get('request')
        categories = ProjectCategorySerializer(instance.category, many=False, context={
                                               'request': request}).data["categories"]
        return categories

    def get_image(self, obj):
        request = self.context.get('request')
        image_url = ImageFormSerializer(obj.image, many=False, context={
                                        'request': request}).data["image"]
        return image_url

    def get_video(self, obj):
        request = self.context.get('request')
        video_url = VideoFormSerializer(obj.video, many=False, context={
                                        'request': request}).data["file"]
        return video_url

    def get_urls(self, obj):
        request = self.context.get('request')
        urls = ProjectUrlsFormSerializer(obj.urls, many=True, context={
                                         'request': request}).data
        return urls

    class Meta:
        model = Project
        fields = ('id', 'title', 'overview',
                  'stacks', 'video', 'image',
                  'urls', 'tags', 'description',
                  'category'
                  )

    def create(self, request, *args):
        data = request
        print("DATA:", data)
        files = args[0]
        project = Project()
        project.save()
        project.title = data["title"]
        project.overview = data["overview"]
        project.description = data["description"]
        if files is dict:
            for f in files:
                myfile = files[f]
                print("file type: ", myfile.content_type.split('/')[0])
                file_type = myfile.content_type.split('/')[0]
                fs = FileSystemStorage()
                valid_extensions = ['.pdf', '.doc',
                                    '.docx', '.jpg', '.png', '.xlsx', '.xls']
                if file_type == "video":
                    print("myfile.name is video")
                    videoD = Video()
                    filename = fs.save("projects/videos/"+myfile.name, myfile)
                    uploaded_file_url = fs.url(filename)
                    videoD.file = "projects/videos/"+myfile.name
                    videoD.save()
                    print("videoD, ", videoD)
                    print("videoD.id, ", videoD.id)
                    project.video = Video(id=videoD.id)
                    # raise ValidationError('Unsupported file extension.')
            else:
                print("myfile.name is image")
                filename = fs.save("projects/images/"+myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                print("uploaded_file_url")
                print(uploaded_file_url)
                print(myfile.name)
                print(project.image)
                project.image = "projects/images/"+myfile.name

        for c in data['tags']:
            try:
                print("try")
                print(c)
                print(Tag.objects.all())
                titles = []
                for cs in Tag.objects.all():
                    titles.append(cs.tag)
                    if cs.tag == c:
                        project.tags.add(cs.id)
                if c not in titles:
                    newC = Tag()
                    newC.tag = c
                    newC.save()
                    project.tags.add(newC.id)
            except:
                print("except")
                newC = Tag()
                newC.tag = c
                newC.save()
                project.tags.add(newC.id)
        project.save()
        return project


class VideoFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ("__all__")


class ImageFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("__all__")


class ProjectUrlsFormSerializer(serializers.ModelSerializer):
    url_type = StringSerializer(many=False)

    class Meta:
        model = Url
        fields = ("url", "url_type", "url_type")


class ProjectCategorySerializer(serializers.ModelSerializer):
    categories = serializers.ChoiceField(choices=PROJECT_CATEGORIES)

    class Meta:
        model = ProjectCategory
        fields = ("__all__")


class ProjectStackSerializer(serializers.ModelSerializer):
    stack = StringSerializer(many=False)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Stack
        fields = ("__all__")

    def get_image(self, instance):
        request = self.context.get('request')
        image_url = ImageFormSerializer(instance.image, many=False, context={
                                        'request': request}).data["image"]
        return image_url
