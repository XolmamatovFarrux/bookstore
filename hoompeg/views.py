from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView

# Create your views here.
# def hoom(request):
#     return HttpResponse("Hello World")
class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class IndexView(TemplateView):
    template_name = 'index.html'

class LessonsView(TemplateView):
    template_name = 'lessons.html'
#
# class HomePageView(TemplateView):
#     model= Post
#     template_name = 'home.html'