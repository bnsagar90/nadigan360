# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.tag_type'
        db.add_column(u'nd360_news', 'tag_type',
                      self.gf('django.db.models.fields.CharField')(default='None', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News.tag_type'
        db.delete_column(u'nd360_news', 'tag_type')


    models = {
        u'nd360.events': {
            'Meta': {'object_name': 'Events'},
            'event_date': ('django.db.models.fields.DateField', [], {}),
            'event_description': ('django.db.models.fields.TextField', [], {}),
            'event_highlights': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'event_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.News']"}),
            'event_participants': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'event_venue': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'nd360.movie_review': {
            'Meta': {'object_name': 'Movie_review'},
            'acting_ratings': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'casts': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'choreography': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cinematography': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'comedy_ratings': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'director': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'editor': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minus': ('django.db.models.fields.TextField', [], {}),
            'movie_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.News']"}),
            'music': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'music_ratings': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'plot': ('django.db.models.fields.TextField', [], {}),
            'plus': ('django.db.models.fields.TextField', [], {}),
            'review_text': ('django.db.models.fields.TextField', [], {}),
            'story_ratings': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_ratings': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vfx_ratings': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'writer': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nd360.news': {
            'Meta': {'object_name': 'News'},
            'created_at': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateField', [], {}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tag_type': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nd360.news_image_links': {
            'Meta': {'object_name': 'News_Image_Links'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.News']"}),
            'image_links': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nd360.news_other_info': {
            'Meta': {'object_name': 'News_Other_Info'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.News']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nd360.news_videos_links': {
            'Meta': {'object_name': 'News_Videos_links'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.News']"}),
            'video_links': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['nd360']