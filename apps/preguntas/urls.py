from django.conf.urls import patterns, include, url
from .views import preguntas, mkpregunta, detallePregunta, BusquedaAjax


urlpatterns = patterns('',
    url(r'^ask/$', mkpregunta.as_view()),
    url(r'^$', 'apps.preguntas.views.preguntas'),
    url(r'^busqueda_ajax/$', BusquedaAjax.as_view()),
    url(r'^detalle/$', detallePregunta.as_view()),
)