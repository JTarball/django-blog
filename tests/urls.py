from django.conf.urls import patterns, include, url


###############################################################################################################
# APP Url Imports
##############################################################################################################
from django_blog import urls as urls_blog


urlpatterns = patterns('',
    url(r'^blog/', include(urls_blog, namespace="blog")),
)
