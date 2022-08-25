import os
from django.conf import settings
from django.contrib.sites.models import Site
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser, JSONParser
import json
import urllib.parse
from .models import (
    ContactForm,
    Language,
    PhoneModel,
    Universities, 
    ProfileInfo, 
    Degree, 
    Bachelor, 
    Master, 
    Doctorate, 
    Course, 
    TechnologyUsed
    )
from .serializers import ( 
    ProfileInfoSerializer,
    TechnologyUsedSerializer, 
    ProfileContactFormsSerializer,
    testSerializer,
    universitySerializer,

)
from constants import *
from django.views import View

from rest_framework.generics import (
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView
)

def set_degree():
    try:
        if(len(Degree.objects.all()) == 0):
            for d in Degree.DEGREES:
                degree = Degree.objects.create(degree=d[0])
    except Exception as e:
        print("Error: ", e)

def set_contact_forms():
    try:
        if(len(ContactForm.objects.all()) == 0):
            for cf in CONTACT_FORMS:
                cfoms = ContactForm.objects.create(form=cf[0])
    except Exception as e:
        print("Error: ", e)

def set_languages():
    try:
        if(len(Language.objects.all()) == 0):
            for l in LANGUAGES:
                lang = Language.objects.create(langauge=l[0])
            for ll in LANGUAGE_LEVELS:
                lang_lev = Language.objects.create(level=ll[0])
    except Exception as e:
        print("Error: ", e)

def set_phone_types():
    try:
        if(len(PhoneModel.objects.all()) == 0):
            for pt in PHONE_TYPES:
                lang = PhoneModel.objects.create(phone_type=pt[0])
    except Exception as e:
        print("Error: ", e)

def set_technologies(del_n_update):
    try:
        if(del_n_update):
            TechnologyUsed.objects.all().delete()
        if(len(TechnologyUsed.objects.all()) == 0):
            for tu in TECHNOLOGIES:
                tech = TechnologyUsed.objects.create(technology=tu[0])
    except Exception as e:
        print("Error: ", e)

class ProfilePageView(RetrieveAPIView):
    queryset = ProfileInfo.objects.all()
    serializer_class = ProfileInfoSerializer
    permission_classes = (permissions.AllowAny,)
    set_degree()
    def get_object(self, *args, **kwargs):
        try:
            print("UserProfileInfoView")
            userInfo = ProfileInfo.objects.get(personal__firstname="Diego")
            ProfileInfoSerializer(userInfo)
            return userInfo
        except ObjectDoesNotExist:
            raise Http404("You do not have an active order")
            return Response({"message": "You do not have an active order"}, status=HTTP_400_BAD_REQUEST)

class ContactFormsView(RetrieveAPIView):            
    queryset = ProfileInfo.objects.all()
    serializer_class = ProfileContactFormsSerializer
    permission_classes = (permissions.AllowAny,)
    def get_object(self, *args, **kwargs):
        try:
            user = ProfileInfo.objects.get(personal__firstname="Diego")
            ProfileInfoSerializer(user)
            return user
        except ObjectDoesNotExist:
            raise Http404("You do not have an active order")

class TechnologiesUsedView(generics.ListAPIView):
    serializer_class = (TechnologyUsedSerializer)
    set_technologies(False)
    technologies = TechnologyUsed.objects.all()
    queryset =technologies

class Degrees_and_CoursesView(generics.ListAPIView):
    serializer_class = (testSerializer)
    universities = Universities.objects.all()
    for u in universities:
        if(u.thumbnail == ""):
            for l in UNIVERSITIES:
                if(l[1] == u.university):
                    create_logo("self", url, l[0], u)

    permission_classes = (permissions.AllowAny,)
    if(len(Bachelor.objects.all()) == 0):
        for b in Bachelor.BACHELOR_DEGREES:
            bachelor = Bachelor.objects.create(bachelor_degree=b[0])
    if(len(Master.objects.all()) == 0):
        for m in Master.MASTER_DEGREES:
            master = Master.objects.create(master_degree=m[0])
    if(len(Doctorate.objects.all()) == 0):
        for p in Doctorate.PHD_DEGREES:
            pHD = Doctorate.objects.create(pHd_degree=p[0])
    if(len(Course.objects.all()) == 0):
        for c in Course.COURSES:
            course = Course.objects.create(course=c[0])

    def get_queryset(self):
        print("Lacking")
        qs = {"data"}
        print(qs)
        return qs

class UniView(generics.ListAPIView):
    serializer_class = universitySerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Universities.objects.all()

class DegView(generics.ListAPIView):
    serializer_class = universitySerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Universities.objects.all()
