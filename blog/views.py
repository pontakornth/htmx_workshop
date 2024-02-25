from http import HTTPStatus

from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET

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
            post = form.save()
            if request.htmx:
                return render(request, 'blog/partials/_post.html', {'post': post})
            return redirect('blog:post_detail', pk=form.instance.pk)
        else:
            if request.htmx:
                response = render(request, 'blog/partials/_new_post_form.html', {'form': form},
                                  status=HTTPStatus.UNPROCESSABLE_ENTITY)
                response.headers['HX-Retarget'] = 'this'
                response.headers['HX-Reswap'] = 'outerHTML'
                return response
            return render(request, 'blog/list.html', {form: 'form', 'posts': Post.objects.all()})
    else:
        # TODO: Redirect
        return redirect('blog:post_list')


@require_POST
def comment_create(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = Post.objects.get(pk=pk)
        comment.save()
        if request.htmx:
            return render(request, 'blog/partials/_comment.html', {'comment': comment})
        return redirect('blog:post_detail', pk=pk)
    else:
        if request.htmx:
            response = render(request, 'blog/partials/_new_comment_form.html',
                              {'form': form, 'post': Post.objects.get(pk=pk)})
            response.headers['HX-Retarget'] = 'this'
            response.headers['HX-Reswap'] = 'outerHTML'
            return response
        return redirect('blog:post_detail', pk=pk)


def about(request):
    return render(request, 'blog/about.html')


@require_GET
def search(request):
    form = SearchForm(request.GET)
    posts = Post.objects.none()
    if form.is_valid():
        q = form.cleaned_data['q']
        if q is not None and len(q) > 0:
            posts = Post.objects.filter(content__icontains=q)
    return render(request, 'blog/search.html', {'posts': posts, 'form': form})
