from django.db import models
from django.utils import timezone

# Create your models here.
import datetime

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year)]

def current_year():
    return datetime.date.today().year


class Event_Model(models.Model):
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
    facebook_url = models.URLField(default="https://www.facebook.com/iitgcsea/")
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    class Meta:
        ordering= ['-publish_date']

class Alumni(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)
    date_registered = models.DateTimeField(default=timezone.now)
    graduation_year = models.IntegerField(
            choices=year_choices(), default=current_year)
    def __str__(self):
        return self.email

