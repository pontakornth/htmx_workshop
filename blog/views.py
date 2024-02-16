from django.shortcuts import render

from blog.forms import PostForm
from blog.models import Post


# Create your views here.
def post_list(request):
    # TODO: Insert new post form here.
    posts = Post.objects.all()
    return render(request, 'blog/list.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comment_set.all()
    return render(request, 'blog/detail.html', {'post': post, 'comments': comments})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request)
        if form.is_valid():
            form.save()
            # TODO: Redirect
            pass
        else:
            # TODO: Render form
            pass
    else:
        # TODO: Redirect
        pass
