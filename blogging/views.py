from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from blogging.models import Post

def test_view(request, *args, **kwargs):
    body = "Testing view\n\n"
    if args:
        body += "Args:\n" + "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n" + "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {
        'posts': posts
    }
    return render(request, 'blogging/list.html', context)
