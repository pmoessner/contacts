from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'contacts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^', include('user_contacts.urls')),
=======
>>>>>>> 5cf6e32fd21493e80ee93c2f618a58aa044b76ac
)
