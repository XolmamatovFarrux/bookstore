from django.urls import path
from .views import HomeView, AboutView, IndexView,  LessonsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('about/', AboutView.as_view(), name='about'),

    path('index/', IndexView.as_view(), name='index'),

    path ('lessons/',LessonsView.as_view(), name='lessons'),

]