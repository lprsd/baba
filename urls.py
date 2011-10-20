from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth import views as auth_views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'notification.views.home', name='home'),
    url(r'^notification/$', 'categories.views.frontend'),
    url(r'^notification/edit/(?P<uhash>\d+)/$', 'categories.views.frontend_user'),
    url(r'^notification/mail/$', 'categories.views.frontend_user'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    url(r'^login/$',auth_views.login,{'template_name':'admin/login.html'},name='forgot_password1'),
	url(r'^logout/$',auth_views.logout,name='forgot_password1'),
	url(r'^passreset/$',auth_views.password_reset,name='forgot_password1'),
	url(r'^passresetdone/$',auth_views.password_reset_done,name='forgot_password2'),
	url(r'^passresetconfirm/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.password_reset_confirm,name='forgot_password3'),
	url(r'^passresetcomplete/$',auth_views.password_reset_complete,name='forgot_password4'),
    url(r'^password/change/$', auth_views.password_change, name='auth_password_change'),
    url(r'^password/change/done/$', auth_views.password_change_done, name='auth_password_change_done'),
)
