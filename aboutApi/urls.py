import os
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from django.urls import path, re_path
from aboutApi.views import (
    ProfilePageView, 
    ContactFormsView,
    TechnologiesUsedView,
)

router = DefaultRouter()
urlpatterns = [
    path('', ProfilePageView.as_view()),
    path('contact/', ContactFormsView.as_view()),
    path('technologies/', TechnologiesUsedView.as_view()),
    
 ]
