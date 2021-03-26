from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post

class LatestEntriesFeed(Feed):
    title = "Latest blog entries"
    link = "/"
    description = "Latest blogs entries about heffalumps and woozles."

    def items(self):
        return Post.objects.exclude(
            published_date__exact=None
        ).order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_body(self, item):
        return item.body

    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])