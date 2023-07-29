from django import views
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView

from blogzine.blog_post.forms import CreatePostForm
from blogzine.blog_post.models import CreatePost, Post


# Create your views here.
class PostDetailsView(views.View):
    pass

class PostCreateView(CreateView):
    model = CreatePost
    form_class = CreatePostForm
    template_name = 'blog_post/dashboard-post-create.html'
    success_url = reverse_lazy('dashboard')
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)






class PostEditView(UpdateView):
    model = CreatePost
    # form_class = CreatePostForm
    template_name='blog_post/dashboard-post-edit.html'
    success_url = reverse_lazy('dashboard')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_id'] = self.get_object().pk
        return context

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('post-create', kwargs={
    #         'pk': self.object.pk
    #     })




class PostListView(ListView):
    model = Post
    template_name = 'blog_post/dashboard-post-list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):

        return Post.objects.all()
