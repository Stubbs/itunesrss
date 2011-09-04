from django.db import models
from django.contrib.syndication.views import Feed

import datetime

# Create your models here.
class Podcast(models.Model):
	"""Model to hold a podcasts details."""
	title = models.CharField(max_length=255, blank=False)
	subtitle = models.CharField(blank=True, max_length=100)
	summary = models.TextField(blank=True)
	pub_date = models.DateField(default=datetime.datetime.today)
	approval_date_time = models.DateTimeField(blank=False, default=datetime.datetime.now)
	enclosure_url = models.CharField(max_length=2048, blank=False)
	author = models.CharField(blank=False, max_length=100)
	image = models.CharField(blank=True, max_length=255)
	enclosure_mime_type = models.CharField(blank=False, max_length=100, default="audio/mpeg")
	enclosure_length = models.IntegerField(blank=True, null=True)
	duration = models.CharField(blank=True, max_length=100)
	keywords = models.CharField(blank=False, max_length=100)
	explicit = models.CharField(blank=False, max_length=5, default="no")
	
	class Admin:
		list_display = ('',)
		search_fields = ('',)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		"""Returns the absolute URL of the item."""
		return self.enclosure_url