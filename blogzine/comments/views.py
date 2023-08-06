from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from blogzine.blog_post.models import Post, CreatePost


from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Comment
from .forms import CommentForm

class CommentView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = Comment.objects.filter(post=post)
        form = CommentForm()
        return render(request, 'blog_post/post-single.html', {'post': post, 'comments': comments, 'form': form})

    def post(self, request, pk):
        post = get_object_or_404(CreatePost, pk=pk)
        comments = Comment.objects.filter(post=post)

        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                return redirect(reverse('post-details', kwargs={'pk': post.pk}))
        else:
            form = CommentForm()

        return render(request, 'blog_post/post-single.html', {'post': post, 'comments': comments, 'form': form})

