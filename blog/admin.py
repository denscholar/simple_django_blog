from django.contrib import admin
from blog.models import Post


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


@admin.register()
class Admin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "body",
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
