from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# def homePage(request):
#     return HttpResponse('<h1>Asilbek</h1>')
class HomePageView(TemplateView):
    template_name = 'home.html'