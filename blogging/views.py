import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from blogging.models import Post
from django import forms
from django.utils import timezone
from blogging.forms import PostForm

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

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {
        'post': post
    }
    return render(request, 'blogging/detail.html', context)

def add_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.author = request.user
            model_instance.published_date = datetime.datetime.utcnow().replace(tzinfo=timezone.utc) if form.cleaned_data.get('publish') else None
            model_instance.save()
            return redirect('/')
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'blogging/post.html', context)