from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from .models import Profile
from videos.models import Video
from django.views.generic.edit import UpdateView

class ProfileView(View):

    def get(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=pk)
        videos = Video.objects.all().filter(uploader=pk).order_by("-date_posted")

        context = {
            'profile': profile,
            'videos': videos
        }

        return render(request, 'profiles/profile.html', context)


class UpdateProfile(UpdateView):
    model = Profile
    fields = ['name', 'location', 'image']
    template_name = 'profiles/update_profile.html'

    def form_valid(self, form):
        if not form.instance.image:
            form.instance.image = "uploads/profile_pics/default.jpg"
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.object.pk})