# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'RecuringJob.typ'
        db.alter_column(u'my_ortoloco_recuringjob', 'typ_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['my_ortoloco.JobType'], on_delete=models.PROTECT))

    def backwards(self, orm):

        # Changing field 'RecuringJob.typ'
        db.alter_column(u'my_ortoloco_recuringjob', 'typ_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['my_ortoloco.AbstractJobType'], on_delete=models.PROTECT))

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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'my_ortoloco.abo': {
            'Meta': {'object_name': 'Abo'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'depot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['my_ortoloco.Depot']", 'on_delete': 'models.PROTECT'}),
            'extra_abos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'extra_abos'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['my_ortoloco.ExtraAboType']"}),
            'extra_abos_changed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'future_extra_abos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'future_extra_abos'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['my_ortoloco.ExtraAboType']"}),
            'future_size': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary_loco': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'abo_primary'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['my_ortoloco.Loco']"}),
            'size': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        u'my_ortoloco.abstractjobtype': {
            'Meta': {'object_name': 'AbstractJobType'},
            'bereich': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['my_ortoloco.Taetigkeitsbereich']", 'on_delete': 'models.PROTECT'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            'displayed_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'my_ortoloco.anteilschein': {
            'Meta': {'object_name': 'Anteilschein'},
            'canceled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['my_ortoloco.Loco']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'my_ortoloco.audit': {
            'Meta': {'object_name': 'Audit'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'field': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'source_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'source_set'", 'to': u"orm['contenttypes.ContentType']"}),
            'target_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'target_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'target_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'my_ortoloco.boehnli': {
            'Meta': {'object_name': 'Boehnli'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['my_ortoloco.Job']"}),
            'loco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['my_ortoloco.Loco']", 'on_delete': 'models.PROTECT'})
        },
        u'my_ortoloco.depot': {
            'Meta': {'object_name': 'Depot'},
            'addr_location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'addr_street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'addr_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['my_ortoloco.Loco']", 'on_delete': 'models.PROTECT'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'longitude': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'weekday': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'my_ortoloco.extraabotype': {
            'Meta': {'object_name': 'ExtraAboType'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'my_ortoloco.job': {
            'Meta': {'object_name': 'Job'},
            'canceled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pinned': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_my_ortoloco.job_set+'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'reminder_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slots': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'my_ortoloco.jobtype': {
            'Meta': {'object_name': 'JobType', '_ormbases': [u'my_ortoloco.AbstractJobType']},
            u'abstractjobtype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['my_ortoloco.AbstractJobType']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'my_ortoloco.loco': {
            'Meta': {'object_name': 'Loco'},
            'abo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'locos'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['my_ortoloco.Abo']"}),
            'addr_location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'addr_street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'addr_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'boehnlis': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'reachable_by_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'loco'", 'unique': 'True', 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'my_ortoloco.onetimejob': {
            'Meta': {'object_name': 'OneTimeJob', '_ormbases': [u'my_ortoloco.Job', u'my_ortoloco.AbstractJobType']},
            u'abstractjobtype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['my_ortoloco.AbstractJobType']", 'unique': 'True'}),
            u'job_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['my_ortoloco.Job']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'my_ortoloco.recuringjob': {
            'Meta': {'object_name': 'RecuringJob', '_ormbases': [u'my_ortoloco.Job']},
            u'job_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['my_ortoloco.Job']", 'unique': 'True', 'primary_key': 'True'}),
            'typ': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['my_ortoloco.JobType']", 'on_delete': 'models.PROTECT'})
        },
        u'my_ortoloco.taetigkeitsbereich': {
            'Meta': {'object_name': 'Taetigkeitsbereich'},
            'coordinator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['my_ortoloco.Loco']", 'on_delete': 'models.PROTECT'}),
            'core': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'areas'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['my_ortoloco.Loco']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['my_ortoloco']