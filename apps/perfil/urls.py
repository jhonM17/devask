from django.conf.urls import patterns, include, url
from .views import perfil


urlpatterns = patterns('',
    url(r'^$', perfil.as_view()),
    
)