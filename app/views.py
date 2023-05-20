from django.shortcuts import render
from app.models import *
# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView

class Home(TemplateView):

    template_name='app/Home.html'

class School_List(ListView):
    model=School
    context_object_name='schools'

class school_detail(DetailView):
    model=School
    context_object_name='sclobject'

