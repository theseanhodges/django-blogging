from django.shortcuts import render
from django.http import HttpResponse

def test_view(request, *args, **kwargs):
    body = "Testing view\n\n"
    if args:
        body += "Args:\n" + "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n" + "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")
