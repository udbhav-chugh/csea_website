from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'home'

urlpatterns = [
    path('members/',TemplateView.as_view(template_name='members1.html')),
    path('events/',TemplateView.as_view(template_name='events1.html')),
    path('', TemplateView.as_view(template_name="home.html")),
]
