# Generated by Django 2.2.16 on 2020-10-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_gallery_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='alloweddomain',
            name='page_name',
            field=models.CharField(default=None, max_length=75),
        ),
    ]
