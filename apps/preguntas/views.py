from django.views.generic import TemplateView
# Create your views here.

class preguntas(TemplateView):
	template_name = 'preguntas/preguntas.html'

class mkpregunta(TemplateView):
	template_name = 'preguntas/hacer-pregunta.html'