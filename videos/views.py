from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Video

def index(request):
    return render(request, 'videos/index.html')

class CreateVideoView(LoginRequiredMixin, CreateView):
    model = Video
    fields = ['title', 'description', 'video_file', 'thumbnail']
    template_name = 'videos/create_video.html'

    def get_success_url(self):
        return reverse("video-detail", kwargs={"pk" : self.object.pk})


class DetailVideo(DetailView):
    model = Video
    template_name = 'videos/detail_video.html'


class UpdateVideo(LoginRequiredMixin, UpdateView):
    model = Video
    fields = ['title', 'description']
    template_name = 'videos/create_video.html'

    def get_success_url(self):
        return reverse("video-detail", kwargs={"pk" : self.object.pk})


class DeleteVideo(LoginRequiredMixin, DeleteView):
    model = Video
    template_name = 'videos/delete_video.html'

    def get_success_url(self):
        return reverse("index")