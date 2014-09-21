from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

admin.autodiscover()

import settings

urlpatterns = patterns('',
    url(r'^', include('register.urls',namespace='regis')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^wechat/$', 'wechat.views.index'),
    url(r'^rest/', include('restframe.urls')) 
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

handler404 = 'register.views.handler404'
handler500 = 'register.views.handler500'
