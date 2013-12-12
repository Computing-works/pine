from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'$', 'register.views.home', name='home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
