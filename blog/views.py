from django.shortcuts import render, redirect

from blog.forms import PostForm
from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    form = PostForm()
    return render(request, 'blog/list.html', {'posts': posts, 'form': form})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comment_set.all()
    return render(request, 'blog/detail.html', {'post': post, 'comments': comments})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', pk=form.instance.pk)
        else:
            return render(request, 'blog/list.html', {form: 'form', 'posts': Post.objects.all()})
    else:
        # TODO: Redirect
        pass
