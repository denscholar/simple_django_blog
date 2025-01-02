from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import Post


def post_list(request):
    posts = Post.published.all()
    context = {"posts": posts}

    print(posts)

    return render(request, "blog/list.html", context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    context = {"post": post}

    # try:
    #     post = Post.published.get(id=id)
    #     context = {'post': post}
    # except Post.DoesNotExist:
    #     Http404("No Post found.")
    return render(request, "blog/detail.html", context)
