# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Audit'
        db.create_table(u'my_ortoloco_audit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('source_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='source_set', to=orm['contenttypes.ContentType'])),
            ('source_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('target_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='target_set', null=True, to=orm['contenttypes.ContentType'])),
            ('target_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'my_ortoloco', ['Audit'])

        # Adding model 'Depot'
        db.create_table(u'my_ortoloco_depot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', max_length=1000)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], on_delete=models.PROTECT)),
            ('weekday', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('addr_street', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('addr_zipcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('addr_location', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'my_ortoloco', ['Depot'])

        # Adding model 'ExtraAboType'
        db.create_table(u'my_ortoloco_extraabotype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
        ))
        db.send_create_signal(u'my_ortoloco', ['ExtraAboType'])

        # Adding model 'Abo'
        db.create_table(u'my_ortoloco_abo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('depot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['my_ortoloco.Depot'], on_delete=models.PROTECT)),
            ('primary_loco', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='abo_primary', null=True, to=orm['my_ortoloco.Loco'])),
            ('groesse', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
        ))
        db.send_create_signal(u'my_ortoloco', ['Abo'])

        # Adding M2M table for field extra_abos on 'Abo'
        db.create_table(u'my_ortoloco_abo_extra_abos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('abo', models.ForeignKey(orm[u'my_ortoloco.abo'], null=False)),
            ('extraabotype', models.ForeignKey(orm[u'my_ortoloco.extraabotype'], null=False))
        ))
        db.create_unique(u'my_ortoloco_abo_extra_abos', ['abo_id', 'extraabotype_id'])

        # Adding model 'Anteilschein'
        db.create_table(u'my_ortoloco_anteilschein', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'my_ortoloco', ['Anteilschein'])

        # Adding model 'Taetigkeitsbereich'
        db.create_table(u'my_ortoloco_taetigkeitsbereich', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', max_length=1000)),
            ('coordinator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], on_delete=models.PROTECT)),
        ))
        db.send_create_signal(u'my_ortoloco', ['Taetigkeitsbereich'])

        # Adding M2M table for field users on 'Taetigkeitsbereich'
        db.create_table(u'my_ortoloco_taetigkeitsbereich_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('taetigkeitsbereich', models.ForeignKey(orm[u'my_ortoloco.taetigkeitsbereich'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(u'my_ortoloco_taetigkeitsbereich_users', ['taetigkeitsbereich_id', 'user_id'])

        # Adding model 'Loco'
        db.create_table(u'my_ortoloco_loco', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='loco', unique=True, to=orm['auth.User'])),
            ('abo', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='locos', null=True, to=orm['my_ortoloco.Abo'])),
            ('addr_street', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('addr_zipcode', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('addr_location', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'my_ortoloco', ['Loco'])

        # Adding model 'JobTyp'
        db.create_table(u'my_ortoloco_jobtyp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', max_length=1000)),
            ('bereich', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['my_ortoloco.Taetigkeitsbereich'], on_delete=models.PROTECT)),
            ('duration', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'my_ortoloco', ['JobTyp'])

        # Adding model 'Job'
        db.create_table(u'my_ortoloco_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('typ', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['my_ortoloco.JobTyp'], on_delete=models.PROTECT)),
            ('slots', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'my_ortoloco', ['Job'])

        # Adding model 'Boehnli'
        db.create_table(u'my_ortoloco_boehnli', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['my_ortoloco.Job'])),
            ('loco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['my_ortoloco.Loco'], null=True, on_delete=models.PROTECT, blank=True)),
            ('amount', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
        ))
        db.send_create_signal(u'my_ortoloco', ['Boehnli'])


    def backwards(self, orm):
        # Deleting model 'Audit'
        db.delete_table(u'my_ortoloco_audit')

        # Deleting model 'Depot'
        db.delete_table(u'my_ortoloco_depot')

        # Deleting model 'ExtraAboType'
        db.delete_table(u'my_ortoloco_extraabotype')

        # Deleting model 'Abo'
        db.delete_table(u'my_ortoloco_abo')

        # Removing M2M table for field extra_abos on 'Abo'
        db.delete_table('my_ortoloco_abo_extra_abos')

        # Deleting model 'Anteilschein'
        db.delete_table(u'my_ortoloco_anteilschein')

        # Deleting model 'Taetigkeitsbereich'
        db.delete_table(u'my_ortoloco_taetigkeitsbereich')

        # Removing M2M table for field users on 'Taetigkeitsbereich'
        db.delete_table('my_ortoloco_taetigkeitsbereich_users')

        # Deleting model 'Loco'
        db.delete_table(u'my_ortoloco_loco')

        # Deleting model 'JobTyp'
        db.delete_table(u'my_ortoloco_jobtyp')

        # Deleting model 'Job'
        db.delete_table(u'my_ortoloco_job')

        # Deleting model 'Boehnli'
        db.delete_table(u'my_ortoloco_boehnli')


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
        u'my_ortoloco.abo': {
            'Meta': {'object_name': 'Abo'},
            'depot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['my_ortoloco.Depot']", 'on_delete': 'models.PROTECT'}),
            'extra_abos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['my_ortoloco.ExtraAboType']", 'null': 'True', 'blank': 'True'}),
            'groesse': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary_loco': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'abo_primary'", 'null': 'True', 'to': u"orm['my_ortoloco.Loco']"})
        },
        u'my_ortoloco.anteilschein': {
            'Meta': {'object_name': 'Anteilschein'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
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
            'amount': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['my_ortoloco.Job']"}),
            'loco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['my_ortoloco.Loco']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'})
        },
        u'my_ortoloco.depot': {
            'Meta': {'object_name': 'Depot'},
            'addr_location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'addr_street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'addr_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'on_delete': 'models.PROTECT'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slots': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'typ': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['my_ortoloco.JobTyp']", 'on_delete': 'models.PROTECT'})
        },
        u'my_ortoloco.jobtyp': {
            'Meta': {'object_name': 'JobTyp'},
            'bereich': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['my_ortoloco.Taetigkeitsbereich']", 'on_delete': 'models.PROTECT'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'my_ortoloco.loco': {
            'Meta': {'object_name': 'Loco'},
            'abo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'locos'", 'null': 'True', 'to': u"orm['my_ortoloco.Abo']"}),
            'addr_location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'addr_street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'addr_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'loco'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'my_ortoloco.taetigkeitsbereich': {
            'Meta': {'object_name': 'Taetigkeitsbereich'},
            'coordinator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'on_delete': 'models.PROTECT'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'taetigkeitsbereiche'", 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['my_ortoloco']