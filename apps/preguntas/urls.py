from django.conf.urls import patterns, include, url
from .views import preguntas, mkpregunta, detallePregunta


urlpatterns = patterns('',
    url(r'^ask/$', mkpregunta.as_view()),
    url(r'^$', preguntas.as_view()),
    url(r'^detalle/$', detallePregunta.as_view()),
)