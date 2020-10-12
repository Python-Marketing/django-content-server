# Generated by Django 2.2.16 on 2020-10-08 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0002_auto_20200929_2310'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('api', '0004_auto_20201008_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField(blank=True, default='Change Me')),
                ('blog_post', models.ForeignKey(on_delete='cascade', to='djangocms_blog.Post')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='djangocms_blog_post_gallery', to=settings.FILER_IMAGE_MODEL, verbose_name='gallery images')),
            ],
        ),
    ]
