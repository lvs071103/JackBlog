from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
#def home(request):
#    return HttpResponse("Hello World, Django")

#def detail(request, my_args):
#    #return HttpResponse("You're looking at my_args %s." % my_args)
#    post = Blog.objects.all()[int(my_args)]
#    str = ("title = %s, category=%s, timestamp = %s, body = %s" %(post.title, post.category, post.timestamp, post.body))
#    return HttpResponse(str)
def page_detail(request, id):
    try:
        post = Blog.objects.get(id=str(id))
    except Blog.DoesNotExist:
        raise Http404
    return render(request, 'pagedetail.html', {'post' :post})

def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})

def home(request):
    posts = Blog.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})

def AboutMe(request):
    return render(request, 'about_me.html')
