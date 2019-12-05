from django.contrib import admin

# Register your models here.
from .models import Event_Model
from .models import Alumni


admin.site.register(Event_Model)
admin.site.register(Alumni)
