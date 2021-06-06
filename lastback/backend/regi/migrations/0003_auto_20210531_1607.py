# Generated by Django 3.0.5 on 2021-05-31 16:07

import django.core.files.storage
from django.db import migrations
import django.utils.timezone
import imagekit.models.fields
import regi.models


class Migration(migrations.Migration):

    dependencies = [
        ('regi', '0002_auto_20210529_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='pic',
            field=imagekit.models.fields.ProcessedImageField(default=django.utils.timezone.now, storage=django.core.files.storage.FileSystemStorage(location='../../../../../../whoareyou/'), upload_to=regi.models.image_path),
            preserve_default=False,
        ),
    ]
