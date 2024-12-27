from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import Post


def post_list(request):
    posts = Post.published.all()
    context = {"posts": posts}

    print(posts)

    return render(request, "blog/list.html", context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {"post": post}

    # try:
    #     post = Post.published.get(id=id)
    #     context = {'post': post}
    # except Post.DoesNotExist:
    #     Http404("No Post found.")
    return render(request, "blog/detail.html", context)
