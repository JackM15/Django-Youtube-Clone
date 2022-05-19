from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.views.generic.list import ListView

from .models import Category, Video, Comment
from .forms import CommentForm

class Index(ListView):
    model = Video
    template_name = 'videos/index.html'
    order_by = "-date_posted"

class CreateVideoView(LoginRequiredMixin, CreateView):
    model = Video
    fields = ['title', 'description', 'video_file', 'thumbnail', "category"]
    template_name = 'videos/create_video.html'

    def form_valid(self, form):
        # Assign the current user to the new video
        form.instance.uploader = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("video-detail", kwargs={"pk" : self.object.pk})


class DetailVideo(View):
    def get(self, request, pk):
        video = Video.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(video=video).order_by("-created_on")
        categories = Video.objects.filter(category=video.category)[:15]

        context = {
            "object": video,
            "form": form,
            "comments": comments,
            "categories": categories,
        }

        return render(request, "videos/detail_video.html", context)

    def post(self, request, pk):
        video = Video.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(
                user = self.request.user,
                comment = form.cleaned_data["comment"],
                video = video
            )
            comment.save()

        comments = Comment.objects.filter(video=video).order_by("-created_on")
        categories = Video.objects.filter(category=video.category)[:15]

        context = {
            "object": video,
            "form": form,
            "comments": comments,
            "categories": categories,
        }

        return render(request, "videos/detail_video.html", context)


class UpdateVideo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Video
    fields = ['title', 'description']
    template_name = 'videos/create_video.html'

    def get_success_url(self):
        return reverse("video-detail", kwargs={"pk" : self.object.pk})
    
    def test_func(self):
        video = self.get_object()
        return self.request.user == video.uploader


class DeleteVideo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    template_name = 'videos/delete_video.html'

    def get_success_url(self):
        return reverse("index")

    def test_func(self):
        video = self.get_object()
        return self.request.user == video.uploader


class VideoCategoryList(View):
    def get(self, request, pk, *args, **kwargs):
        category = Category.objects.get(pk=pk)
        videos = Video.objects.filter(category=pk).order_by("-date_posted")

        context = {
            "category": category,
            "videos": videos,
        }

        return render(request, "videos/video_category.html", context)