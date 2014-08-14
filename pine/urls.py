from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers

from django.conf import settings

admin.autodiscover()

import settings

class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = patterns('',
    url(r'^', include('register.urls',namespace='regis')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^wechat/$', 'wechat.views.index'),
    
    url(r'^rest-framework/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')) 
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

handler404 = 'register.views.handler404'
handler500 = 'register.views.handler500'
