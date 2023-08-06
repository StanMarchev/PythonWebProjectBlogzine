from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from .forms import CommentForm
from blogzine.blog_post.models import Post

def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-details', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog_post/post-single.html', {'post': post, 'comments': comments, 'form': form})
