from django.conf.urls import patterns, include, url
from django.contrib.auth.views import \
            login,logout, \
            password_change,password_change_done,   \
            password_reset,password_reset_done,password_reset_confirm,password_reset_complete

urlpatterns = patterns('register.views',
    url(r'^$', 'index_view', name='home'),
    url(r'^home/$', 'index_view'),
    
    url(r'^about/$','about_view',name='about'),
    
    url(r'^account/create/$', 'account_create_view',name='create_user'),
    url(r'^account/login/$', login, name='login'),
    url(r'^account/logout/$', 'account_logout_view', name='logout'),
    
    url(r'^account/password/change/$', password_change, name='psw_ch'),
    url(r'^account/password/change/done/$', password_change_done, name='psw_ch_done'),
    
    url(r'^enroll/$', 'enrollment', name='enroll'),
    url(r'^contact/$', 'contact_view', name='contact'),
    
    url(r'^nclab-test/$','nclab_view',name='nclab'),
)
