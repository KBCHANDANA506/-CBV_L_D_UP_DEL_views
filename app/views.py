from django.shortcuts import render
from app.models import *
# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class Home(TemplateView):

    template_name='app/Home.html'

class schoolList(ListView):
    model=School
    context_object_name='schools'

class school_detail(DetailView):
    model=School
    context_object_name='sclobject'

class School_form(CreateView):
    model=School
    fields='__all__'



class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class School_Delete(DeleteView):
    model=School
    context_object_name='schoolobject'
    success_url=reverse_lazy('schoolList')





