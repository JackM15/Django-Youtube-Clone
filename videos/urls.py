from django.urls import path
from .views import CreateVideoView, DetailVideo, UpdateVideo

urlpatterns = [
    path("create/", CreateVideoView.as_view(), name="video-create"),
    path("<int:pk>/", DetailVideo.as_view(), name="video-detail"),
    path("<int:pk>/update/", UpdateVideo.as_view(), name="video-update"),
] 
