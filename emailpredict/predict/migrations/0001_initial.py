# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EmailAddress'
        db.create_table(u'predict_emailaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('pattern', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predict.Pattern'], null=True, blank=True)),
            ('verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'predict', ['EmailAddress'])

        # Adding model 'Pattern'
        db.create_table(u'predict_pattern', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('pattern', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('probability', self.gf('django.db.models.fields.FloatField')(default=1.0)),
        ))
        db.send_create_signal(u'predict', ['Pattern'])


    def backwards(self, orm):
        # Deleting model 'EmailAddress'
        db.delete_table(u'predict_emailaddress')

        # Deleting model 'Pattern'
        db.delete_table(u'predict_pattern')


    models = {
        u'predict.emailaddress': {
            'Meta': {'object_name': 'EmailAddress'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pattern': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['predict.Pattern']", 'null': 'True', 'blank': 'True'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'predict.pattern': {
            'Meta': {'object_name': 'Pattern'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pattern': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'probability': ('django.db.models.fields.FloatField', [], {'default': '1.0'})
        }
    }

    complete_apps = ['predict']