from django.shortcuts import render
from django.views.generic import TemplateView


class FrontendView(TemplateView):
    """
    Serve the frontend application.
    """
    template_name = 'index.html'
