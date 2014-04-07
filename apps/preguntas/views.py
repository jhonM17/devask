from django.views.generic import TemplateView, ListView
from .models import Pregunta, Tag
from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.

#class preguntas(ListView):
#	template_name = 'preguntas/preguntas.html'
#	model = Pregunta
#	context_object_name = 'Preguntas'

def preguntas(request):
	preguntas = Pregunta.objects.all()
	tags = Tag.objects.all()
	return render_to_response('preguntas/preguntas.html', {'preguntas':preguntas, 'tags':tags}, context_instance=RequestContext(request))

from django.core import serializers
from django.http import HttpResponse

class BusquedaAjax(TemplateView):

	def get(self, request, *args, **kwargs):
		id_tag = request.GET['id']
		preguntas = Pregunta.objects.filter(tag__id = id_tag)
		data = serializers.serialize('json', preguntas, fields={'nombre','contenido','tag'})
		return HttpResponse(data, mimetype='application/json')


class mkpregunta(TemplateView):
	template_name = 'preguntas/hacer-pregunta.html'

class detallePregunta(TemplateView):
	template_name = 'preguntas/detalle-pregunta.html'