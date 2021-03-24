from django.urls import path
from blogging.views import test_view

urlpatterns = [
    path("", test_view, name="blog_index"),
]