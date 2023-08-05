from django import views
from django.core.paginator import Paginator
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