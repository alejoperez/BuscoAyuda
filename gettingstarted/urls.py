from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
from django.conf import settings
from django.conf.urls.static import static
# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^independents', hello.views.getIndependents, name='independents'),
    url(r'^jobs', hello.views.getJobs, name='jobs'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', hello.views.registerIndependent, name='registerIndependent'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
