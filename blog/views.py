from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .forms import CommentForm, EmailPostForm
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from django.views.decorators.http import require_POST


# def post_list(request):
#     post_list = Post.published.all()
#     paginator = Paginator(
#         post_list, 2
#     )  # this takes the post list and how many post in a page
#     page_number = request.GET.get("page", 1)

#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         # If page_number is not an integer get the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page_number is out of range get last page of results
#         posts = paginator.page(paginator.num_pages)
#     context = {"posts": posts}
#     return render(request, "blog/list.html", context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    comments = post.comments.filter(active=True)
    form = CommentForm()  # Form for users to comment
    context = {
        "post": post,
        "form": form,
        "comments": comments,
    }

    # try:
    #     post = Post.published.get(id=id)
    #     context = {'post': post}
    # except Post.DoesNotExist:
    #     Http404("No Post found.")
    return render(request, "blog/detail.html", context)


# create a new posts list using class-based views
class PostListView(ListView):
    # alternative post list view
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/list.html"


# post Share
def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == "POST":
        # form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():  # Form fields passed validation
            cd = form.cleaned_data  # ... send email
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = (
                f"{cd['name']} ({cd['email']})" f"recommends you read {post.title}"
            )
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}'s comments: {cd['comments']}"
            )
            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=[cd["to"]],
            )
            sent = True
    else:
        form = EmailPostForm()

    context = {
        "post": post,
        "form": form,
        "sent": sent,
    }
    return render(request, "blog/share.html", context)


# post comment
@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)  # a comment was posted
    if form.is_valid():
        comment = form.save(
            commit=False
        )  # create a comment object without saving it to the database
        comment.post = post  # assign the post to the comment
        comment.save()  # save rge comment to the database

        context = {
            "post": post,
            "form": form,
            "comment": comment,
        }
        return render(request, "blog/comment.html", context)
