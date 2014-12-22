# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pattern.probability'
        db.add_column(u'predict_pattern', 'probability',
                      self.gf('django.db.models.fields.FloatField')(default=1.0),
                      keep_default=False)

        # Deleting field 'EmailAddress.probability'
        db.delete_column(u'predict_emailaddress', 'probability')


    def backwards(self, orm):
        # Deleting field 'Pattern.probability'
        db.delete_column(u'predict_pattern', 'probability')

        # Adding field 'EmailAddress.probability'
        db.add_column(u'predict_emailaddress', 'probability',
                      self.gf('django.db.models.fields.FloatField')(default=1.0),
                      keep_default=False)


    models = {
        u'predict.emailaddress': {
            'Meta': {'object_name': 'EmailAddress'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pattern': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['predict.Pattern']", 'null': 'True', 'blank': 'True'})
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