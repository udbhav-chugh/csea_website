from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'home'

urlpatterns = [
    path('', views.index , name='index'),
    path('cseweb/csea/', views.index , name='index'),
    path('cseweb/csea/members/',TemplateView.as_view(template_name='members1.html')),
    path('cseweb/csea/calendar/',TemplateView.as_view(template_name='calendar.html')),
    path('cseweb/csea/events/',views.events_view),
    path('cseweb/csea/developers/',TemplateView.as_view(template_name='developers.html')),
]
