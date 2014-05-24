# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table(u'nd360_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('modified_at', self.gf('django.db.models.fields.DateField')()),
            ('created_at', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'nd360', ['News'])

        # Adding model 'News_Image_Links'
        db.create_table(u'nd360_news_image_links', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nd360.News'])),
            ('image_links', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'nd360', ['News_Image_Links'])

        # Adding model 'News_Videos_links'
        db.create_table(u'nd360_news_videos_links', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nd360.News'])),
            ('video_links', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'nd360', ['News_Videos_links'])

        # Adding model 'News_Other_Info'
        db.create_table(u'nd360_news_other_info', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nd360.News'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'nd360', ['News_Other_Info'])

        # Adding model 'Movie_review'
        db.create_table(u'nd360_movie_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nd360.News'])),
            ('casts', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('director', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('writer', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('editor', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cinematography', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('music', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('choreography', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('total_ratings', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('story_ratings', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('music_ratings', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('acting_ratings', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('comedy_ratings', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('vfx_ratings', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('plot', self.gf('django.db.models.fields.TextField')()),
            ('plus', self.gf('django.db.models.fields.TextField')()),
            ('minus', self.gf('django.db.models.fields.TextField')()),
            ('review_text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'nd360', ['Movie_review'])

        # Adding model 'Events'
        db.create_table(u'nd360_events', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nd360.News'])),
            ('event_date', self.gf('django.db.models.fields.DateField')()),
            ('event_venue', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('event_participants', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('event_highlights', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('event_description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'nd360', ['Events'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table(u'nd360_news')

        # Deleting model 'News_Image_Links'
        db.delete_table(u'nd360_news_image_links')

        # Deleting model 'News_Videos_links'
        db.delete_table(u'nd360_news_videos_links')

        # Deleting model 'News_Other_Info'
        db.delete_table(u'nd360_news_other_info')

        # Deleting model 'Movie_review'
        db.delete_table(u'nd360_movie_review')

        # Deleting model 'Events'
        db.delete_table(u'nd360_events')


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