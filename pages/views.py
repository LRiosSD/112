from re import template
from tempfile import tempdir
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name="index.html"

class AboutPageView(TemplateView):
    template_name="about.html"
    