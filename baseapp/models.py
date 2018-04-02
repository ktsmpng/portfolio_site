from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	thumbnail_image = models.ImageField(upload_to="baseapp/media",blank=True, null=True)
	url_link = models.URLField(blank=True, null=True);

	def __str__(self):
		return self.name

class Blog(models.Model):
	name = models.CharField(max_length=30)
	short_description = models.CharField(max_length=100)
	content = models.TextField()
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.name