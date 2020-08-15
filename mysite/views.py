from django.views.generic.base import TemplateView


class IndeView(TemplateView):
    template_name = 'index.html'
