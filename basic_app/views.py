from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, 
                                  ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from . import models
# Create your views here.

# Standard view
# def index(request):
#     return render(request, 'basic_app/index.html')
# VERY BASIC
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Classed based views are cool")

# TEMPLATE VIEW
# class IndexView(TemplateView):
#     template_name = 'basic_app/index.html'

#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'BASIC INJECTION!'
#         return context

# LIST VIEW

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    #detta gör så att i school_list döper man om school_list till schools
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

# CREATE A SCHOOl
class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

# UPDATE A CREATED SCHOOL
class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

# DELETE A SCHOOL
class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
