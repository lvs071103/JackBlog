from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog
from datetime import datetime

# Create your views here.
#def home(request):
#    return HttpResponse("Hello World, Django")

#def detail(request, my_args):
#    #return HttpResponse("You're looking at my_args %s." % my_args)
#    post = Blog.objects.all()[int(my_args)]
#    str = ("title = %s, category=%s, timestamp = %s, body = %s" %(post.title, post.category, post.timestamp, post.body))
#    return HttpResponse(str)
#def test(request):
#    return render(request, 'test.html', {'current_time': datetime.now()})

def home(request):
    post_list = Blog.objects.all()
    return render(request, 'home.html', {'post_list': post_list})
