from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^', include('register.urls',namespace='regis')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

handler404 = 'register.views.handler404'
handler500 = 'register.views.handler500'
