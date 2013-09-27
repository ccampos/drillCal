# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Day'
        db.create_table(u'drills_day', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('exert_percent', self.gf('django.db.models.fields.IntegerField')(default=85)),
            ('distance', self.gf('django.db.models.fields.FloatField')(default=3.11)),
        ))
        db.send_create_signal(u'drills', ['Day'])


    def backwards(self, orm):
        # Deleting model 'Day'
        db.delete_table(u'drills_day')


    models = {
        u'drills.day': {
            'Meta': {'object_name': 'Day'},
            'distance': ('django.db.models.fields.FloatField', [], {'default': '3.11'}),
            'exercise_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'exert_percent': ('django.db.models.fields.IntegerField', [], {'default': '85'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['drills']