# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Depot', fields ['code']
        db.create_unique(u'loco_app_depot', ['code'])


        # Changing field 'Depot.contact'
        db.alter_column(u'loco_app_depot', 'contact_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], on_delete=models.PROTECT))

        # Changing field 'Abo.abotype'
        db.alter_column(u'loco_app_abo', 'abotype_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['loco_app.AboType'], on_delete=models.PROTECT))

    def backwards(self, orm):
        # Removing unique constraint on 'Depot', fields ['code']
        db.delete_unique(u'loco_app_depot', ['code'])


        # Changing field 'Depot.contact'
        db.alter_column(u'loco_app_depot', 'contact_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Abo.abotype'
        db.alter_column(u'loco_app_abo', 'abotype_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['loco_app.AboType']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'loco_app.abo': {
            'Meta': {'object_name': 'Abo'},
            'abotype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['loco_app.AboType']", 'on_delete': 'models.PROTECT'}),
            'depot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['loco_app.Depot']", 'on_delete': 'models.PROTECT'}),
            'extra_abos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['loco_app.ExtraAboType']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'abos'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        },
        u'loco_app.abotype': {
            'Meta': {'object_name': 'AboType'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'loco_app.audit': {
            'Meta': {'object_name': 'Audit'},
            'action': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'source_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'source_set'", 'to': u"orm['contenttypes.ContentType']"}),
            'target_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'target_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'target_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'loco_app.depot': {
            'Meta': {'object_name': 'Depot'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'on_delete': 'models.PROTECT'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'weekday': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'loco_app.extraabotype': {
            'Meta': {'object_name': 'ExtraAboType'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'loco_app.loco': {
            'Meta': {'object_name': 'Loco'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'loco'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'loco_app.staticstring': {
            'Meta': {'object_name': 'StaticString'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '10000'})
        }
    }

    complete_apps = ['loco_app']