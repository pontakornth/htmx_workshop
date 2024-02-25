from django.shortcuts import render, redirect

from blog.forms import PostForm, CommentForm, SearchForm
from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    form = PostForm()
    return render(request, 'blog/list.html', {'posts': posts, 'form': form})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comment_set.all()
    form = CommentForm()
    return render(request, 'blog/detail.html', {'post': post, 'comments': comments, 'form': form})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', pk=form.instance.pk)
        else:
            # TODO: Render HTMX form
            return render(request, 'blog/list.html', {form: 'form', 'posts': Post.objects.all()})
    else:
        # TODO: Redirect
        return redirect('blog:post_list')


def comment_create(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('blog:post_detail', pk=pk)
        else:
            # TODO: Render HTMX form
            pass
    else:
        # TODO: Redirect
        return redirect('blog:post_detail', pk=pk)


def about(request):
    return render(request, 'blog/about.html')


def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        posts = Post.objects.none()
        if form.is_valid():
            q = form.cleaned_data['q']
            if q is not None and len(q) > 0:
                posts = Post.objects.filter(content__icontains=q)
        return render(request, 'blog/search.html', {'posts': posts, 'form': form})
    return redirect('blog:post_search')
