from django.contrib import admin
from nd360.models import *


class Articles_admin(admin.TabularInline):
	model = Articles
	extra = 0

class News_articles_Admin(admin.ModelAdmin):
	list_display = ('id', 'news_id')

class Reviews_display(admin.ModelAdmin):
	list_display = ('review_id', 'id')
	
 
#admin.site.register(Articles)
admin.site.register(News)
admin.site.register(Reviews)
admin.site.register(Events)

