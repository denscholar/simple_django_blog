from django.urls import path
from blog.views import PostListView
from . import views



app_name = 'blog'


urlpatterns = [
    # path('blog/', views.post_list, name='post_list'),
    path('blog/', PostListView.as_view(), name='post_list'),
    path('/<int:post_id>/share/', views.post_share,  name='post_share'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]