from django.db import models

# Create your models here.

class Event_Model(models.Model):
	title =models.TextField()
	content =models.TextField(null=True, blank=True)
	facebook_url =models.URLField(default="https://www.facebook.com/iitgcsea/")
	publish_date =models.DateTimeField(auto_now=False, auto_now_add=False)
	image   = models.ImageField(upload_to='image/', blank=True, null=True)
	class Meta:
		ordering= ['-publish_date']



