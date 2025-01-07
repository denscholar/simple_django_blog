from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(
        post_list, 2
    )  # this takes the post list and how many post in a page
    page_number = request.GET.get("page", 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer get the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range get last page of results
        posts = paginator.page(paginator.num_pages)
    context = {"posts": posts}
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
