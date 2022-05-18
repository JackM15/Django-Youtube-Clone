from django.urls import path
from .views import CreateVideoView

urlpatterns = [
    path("create/", CreateVideoView.as_view(), name="video-create"),
] 
