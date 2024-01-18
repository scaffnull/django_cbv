from django.shortcuts import render
from django.views.generic import View, TemplateView
# Create your views here.

# Standard view
# def index(request):
#     return render(request, 'basic_app/index.html')
# VERY BASIC
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Classed based views are cool")

# TEMPLATE VIEW
class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context

