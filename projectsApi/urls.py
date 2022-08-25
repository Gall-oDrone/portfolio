from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from django.urls import path, re_path
from projectsApi.views import (
    ProjectListView, 
    ProjectDetailView, 
    ProjectCreateView,
    ProjectDeleteView,
    ProjectUpdateView,
    VideoViewSet,
    ImageCreateView,
    ImageDestroyView,
)

router = DefaultRouter()
router.register(r'', VideoViewSet, basename='video')
urlpatterns = [
    path('', ProjectListView.as_view()),
    path('create/', ProjectCreateView.as_view()),
    path('<pk>', ProjectDetailView.as_view()),
    path('<pk>/update/', ProjectUpdateView.as_view()),
    path('<pk>/delete/', ProjectDeleteView.as_view()),
    path('create/images/', ImageCreateView.as_view),
    path('destroy/images/', ImageDestroyView.as_view),
    url(r'^video/', include(router.urls)),
 ]