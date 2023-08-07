from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView

from blogzine.blog_post.forms import CreatePostForm
from blogzine.blog_post.models import CreatePost, Post

class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(CreatePost, pk=pk)
        return render(request, 'blog_post/post-single.html', {'post': post})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = CreatePost
    form_class = CreatePostForm
    template_name = 'blog_post/dashboard-post-create.html'



    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-details', kwargs={'pk': self.object.pk})


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



def post_list(request):
    posts = CreatePost.objects.all()
    paginator = Paginator(posts, 10)


    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj' : page_obj  ,
        'posts' : posts,
    }
    print(posts)

    return render(request, 'blog_post/dashboard-post-list.html', context)



class PostDeleteView(View):
    def post(self, request, pk):
        post = get_object_or_404(CreatePost, pk=pk)

        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('dashboard')