# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160204_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackendCkeditor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
