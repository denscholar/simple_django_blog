from django.contrib import admin
from blog.models import Comment, Post


# customize the admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "publish", "status")
    list_filter = ("created", "author", "publish", "status")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    # raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ("status", "publish")
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Comment)
class Admin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "created",
        "updated",
        "active",
    )
    list_filter = (
        "created",
        "updated",
        "active",
    )
    search_fields = ["name", "email", "body"]
