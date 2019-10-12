from django.urls import path
from . import views

from django.views.generic import TemplateView

app_name = 'home'

urlpatterns = [
    path('', views.index , name='index'),
    path('members/',TemplateView.as_view(template_name='members1.html')),
    path('calendar/',TemplateView.as_view(template_name='calendar.html')),
    path('events/',views.events_view),
    path('developers/',TemplateView.as_view(template_name='developers.html')),
]
