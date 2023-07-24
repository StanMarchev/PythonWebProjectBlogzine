from django import views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from blogzine.blog_post.models import CreatePost


# Create your views here.
class PostDetailsView(views.View):
    pass

class PostCreateView(CreateView):
    model = CreatePost
    template_name = 'blog_post/dashboard-post-create.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostEditView(views.View):
    pass
