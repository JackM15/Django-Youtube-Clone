from django.urls import path
from .views import CreateVideoView, DeleteVideo, DetailVideo, UpdateVideo, VideoCategoryList, SearchVideo

urlpatterns = [
    path("create/", CreateVideoView.as_view(), name="video-create"),
    path("<int:pk>/", DetailVideo.as_view(), name="video-detail"),
    path("<int:pk>/update/", UpdateVideo.as_view(), name="video-update"),
    path("<int:pk>/delete/", DeleteVideo.as_view(), name="video-delete"),
    path("category/<int:pk>/", VideoCategoryList.as_view(), name="category-list"),
    path("search/", SearchVideo.as_view(), name="video-search"),
] 
