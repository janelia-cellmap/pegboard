from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = "index.html"


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. From Pegboard.")
