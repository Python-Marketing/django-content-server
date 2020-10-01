from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

from django.db import models
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from djangocms_blog.models import Post as BlogPost

User = settings.AUTH_USER_MODEL
upload_dir = settings.MEDIA_ROOT[1:] + "/Posts"


class Video(models.Model):
    author = models.ForeignKey(User, on_delete="cascade")
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=175)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True)

    def __str__(self):
        return force_text(_('%s uploaded %s') % (self.author.get_full_name(), self.title))


class Donation(models.Model):
    author = models.ForeignKey(User, on_delete="cascade")
    charity = models.ForeignKey(BlogPost, on_delete="cascade")
    amount = models.PositiveIntegerField()
    date_created = models.DateTimeField(_('created at'), auto_now_add=True)
    date_modified = models.DateTimeField(_('modified at'), auto_now=True)

    def __str__(self):
        return force_text(_('%s donated %s') % (self.author.get_full_name(), self.amount))


class Testimonial(models.Model):
    author = models.ForeignKey(User, on_delete="cascade")
    body = models.TextField(blank=True)

    date_created = models.DateTimeField(_('created at'), auto_now_add=True)
    date_modified = models.DateTimeField(_('modified at'), auto_now=True)

    def __str__(self):
        return force_text(_('%s wrote %s') % (self.author.get_full_name(), self.body))


class Volunteer(models.Model):
    author = models.ForeignKey(User, on_delete="cascade")
    date_created = models.DateTimeField(_('created at'), auto_now_add=True)
    date_modified = models.DateTimeField(_('modified at'), auto_now=True)

    def __str__(self):
        return force_text(_('%s volunteered email address : %s') % (self.author.first_name, self.author.email))

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete="cascade")
    body = models.TextField(blank=True)
    content_type = models.ForeignKey(ContentType, on_delete="cascade")
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    date_created = models.DateTimeField(_('created at'), auto_now_add=True)
    date_modified = models.DateTimeField(_('modified at'), auto_now=True)


class Picture(models.Model):
    author = models.ForeignKey(User, on_delete="cascade")
    image = models.ImageField()
    caption = models.TextField(blank=True)
    comments = GenericRelation('Comment')


class Page(models.Model):
    slug = models.SlugField(unique=True)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete="cascade")
    title = models.CharField(max_length=75)
    slug = models.SlugField(unique=True)
    body = models.TextField(blank=True)
    link = models.URLField(blank=True)
    file = models.FileField(upload_to=upload_dir)
    comments = GenericRelation('Comment')
    pictures = GenericRelation('Picture')
    page = models.ForeignKey(Page, on_delete="cascade")


class ExtendedPage(models.Model):
    page = models.ForeignKey(Page,
                             # unique=True,
                             verbose_name=_("Page"),
                             editable=False,
                             related_name='extended_fields',
                             on_delete="cascade"
                             )
    description = models.TextField(blank=True)
    background_image = models.FileField(upload_to=upload_dir)


class PageDetailExtension(PageExtension):
    image = models.ImageField(upload_to=upload_dir)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to=upload_dir)


extension_pool.register(PageDetailExtension)
