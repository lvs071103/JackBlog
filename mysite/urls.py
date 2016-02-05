from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.home'),
    url(r'^(?P<id>\d+)/$', 'blog.views.page_detail', name='page_detail'),
    url(r'^test/$', 'blog.views.test'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^about', 'blog.views.AboutMe', name='AboutMe'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
