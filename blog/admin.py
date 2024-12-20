from django.contrib import admin
from blog.models import Post


# customize the admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "publish", "status"]
