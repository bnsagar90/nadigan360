from django.db import models
from nadigan360.settings import *
from datetime import *

class News(models.Model):
        id              = models.AutoField(primary_key=True)
        title           = models.CharField(max_length=255)
        display_image   = models.ImageField(upload_to='templates/static/img')
        text            = models.TextField()
        number_of_views = models.IntegerField()
        written_by      = models.CharField(max_length=255)
        created_at      = models.DateField()

class Movie_review(models.Model):
	id              = models.AutoField(primary_key=True)
	title           = models.CharField(max_length=255)
	display_image   = models.ImageField(upload_to='templates/static/img')
	review_text	= models.TextField() 
	plus		= models.CharField(max_length=255)
	minus		= models.CharField(max_length=255)
	review_done_by	= models.CharField(max_length=255)
	number_of_views = models.IntegerField()
	created_at      = models.DateField()

class Articles(models.Model):
	id              = models.AutoField(primary_key=True)
	title           = models.CharField(max_length=255)
	display_image   = models.ImageField(upload_to='templates/static/img')
	tags 		= models.ForeignKey('Tags')
	written_by	= models.CharField(max_length=255)
	views_count	= models.IntegerField()
	created_at	= models.DateField()

	def id_str(self):
		return self.id

class News_articles(models.Model):
	news_id 		= models.OneToOneField('Articles')
	text			= models.TextField()


	def news_id_str(self):
		return self.news_id

class Tags(models.Model):
	title = models.AutoField(primary_key=True)


class Reviews(models.Model):
	review_id		= models.OneToOneField('Articles')
	review_text		= models.TextField()
	plus			= models.CharField(max_length=255)
	minus			= models.CharField(max_length=255)
	rating			= models.IntegerField()
	
'''class Gallery(models.Model):
	gallery_id 		= models.OneToOneField('Articles')
	gallery_description	= models.TextField()
	
class Pictures(models.Model):
	gallery_id		= models.ForeignKey('Gallery')
	picture			= models.ImageField(upload_to='templates/static/img')
	picture_description	= models.CharField(max_length=255)'''

class Events(models.Model):
  	event_id 		= models.OneToOneField('Articles')
	event_descrption	= models.TextField()
	event_highlights	= models.TextField()
	




