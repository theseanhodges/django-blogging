from django.urls import path
from blogging.views import list_view, detail_view, add_view
from blogging.feeds import LatestEntriesFeed

urlpatterns = [
    path("", list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('post/', add_view, name="blog_post"),
    path('feed/', LatestEntriesFeed())
]