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
    url(r'^login', hello.views.loginUser, name='login'),
    url(r'^islogged', hello.views.isLoggedUser, name='isLoggedUser'),
    url(r'^logout', hello.views.logoutUser, name='logout'),
    url(r'^profile', hello.views.profile, name='profile'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', hello.views.registerIndependent, name='registerIndependent'),
    url(r'^comments/', hello.views.registerComment, name='registerComment'),
    url(r'^detail', hello.views.detail, name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
