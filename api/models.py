from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import safe
from django.utils.html import format_html
from filer.fields.image import FilerImageField

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

from django.db import models
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from djangocms_blog.models import Post as BlogPost

User = settings.AUTH_USER_MODEL
upload_dir = settings.MEDIA_ROOT[1:] + "/Posts"


class Video(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=175)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True)

    def __unicode__(self):
        return force_text(_('%s uploaded %s') % (self.author.get_full_name(), self.title))


class Donation(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    charity = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date_created = models.DateTimeField(_('created at'), auto_now_add=True)
    date_modified = models.DateTimeField(_('modified at'), auto_now=True)

    def __unicode__(self):
        return force_text(_('%s donated %s') % (self.author.get_full_name(), self.amount))


class Testimonial(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)

    date_created = models.DateTimeField(_('created at'), auto_now_add=True)
    date_modified = models.DateTimeField(_('modified at'), auto_now=True)

    def __str__(self):
        return force_text(_('%s wrote %s') % (self.author.get_full_name(), self.body))

    def __unicode__(self):
        return force_text(_('%s wrote %s') % (self.author.get_full_name(), self.body))


class Volunteer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(_('created at'), auto_now_add=True)
    date_modified = models.DateTimeField(_('modified at'), auto_now=True)

    def __str__(self):
        return force_text(_('%s volunteered email address : %s') % (self.author.first_name, self.author.email))

    def __unicode__(self):
        return force_text(_('%s volunteered email address : %s') % (self.author.first_name, self.author.email))


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    date_created = models.DateTimeField(_('created at'), auto_now_add=True)
    date_modified = models.DateTimeField(_('modified at'), auto_now=True)


# search domains div classes and id
class AllowedDomain(models.Model):
    name = models.CharField(max_length=75)
    domain = models.URLField(blank=True)
    term = models.CharField(max_length=75, blank=True)
    page_name = models.CharField(max_length=75, default=None)
    class_names = models.CharField(max_length=150)
    id_names = models.CharField(max_length=150)

    def __unicode__(self):
        return force_text(_('%s') % self.name)

    def __str__(self):
        return force_text(_('%s') % self.name)


class GumtreeCategoryLabel(models.Model):

    name = models.CharField(max_length=75)
    link = models.CharField(max_length=75)
    key = models.CharField(max_length=75)

    def __unicode__(self):
        return force_text(_('%s') % self.name)

    def __str__(self):
        return force_text(_('%s') % self.name)


class GumtreeCategory(models.Model):
    label = models.ForeignKey(GumtreeCategoryLabel, on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    link = models.CharField(max_length=75)
    key = models.CharField(max_length=75)

    def __unicode__(self):
        return force_text(_('%s') % self.name)

    def __str__(self):
        return force_text(_('%s') % self.name)


class GumtreeProvince(models.Model):
    name = models.CharField(max_length=75)
    link = models.CharField(max_length=75)
    key = models.CharField(max_length=75)

    def __unicode__(self):
        return force_text(_('%s') % self.name)

    def __str__(self):
        return force_text(_('%s') % self.name)


class GumtreeLocation(models.Model):
    name = models.CharField(max_length=75)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    link = models.CharField(max_length=75)
    key = models.CharField(max_length=75)
    province = models.ForeignKey(GumtreeProvince, on_delete=models.CASCADE, blank=True, null=True)

    def __unicode__(self):
        return force_text(_('%s') % self.name)

    def __str__(self):
        return force_text(_('%s') % self.name)


class BeautifulGoogleSearch(models.Model):
    allowed = models.ForeignKey(AllowedDomain, on_delete=models.CASCADE)
    term = models.CharField(max_length=75)
    link = models.URLField(blank=True)
    body = models.TextField(blank=True)
    date_created = models.DateTimeField(_('created at'), auto_now_add=True)
    date_modified = models.DateTimeField(_('modified at'), auto_now=True)

    def __unicode__(self):
        return force_text(_('%s') % self.allowed.name)

    def __str__(self):
        return force_text(_('%s') % self.allowed.name)


class BeautifulGoogleResult(models.Model):
    bgs = models.ForeignKey(BeautifulGoogleSearch, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    subtitle = models.CharField(max_length=75)
    abstract = models.TextField(blank=True)
    image = models.CharField(max_length=75)
    date_created = models.DateTimeField(_('created at'), auto_now_add=True)
    date_modified = models.DateTimeField(_('modified at'), auto_now=True)

    def __unicode__(self):
        return force_text(_('%s') % self.bgs.allowed.name)

    def __str__(self):
        return force_text(_('%s') % self.bgs.allowed.name)


class BeautifulGumtreeSearch(models.Model):
    allowed = models.ForeignKey(AllowedDomain, on_delete=models.CASCADE)
    term = models.CharField(max_length=75)
    link = models.URLField(blank=True)
    body = models.TextField(blank=True)
    date_created = models.DateTimeField(_('created at'), auto_now_add=True)
    date_modified = models.DateTimeField(_('modified at'), auto_now=True)

    def __unicode__(self):
        return force_text(_('%s') % self.term)

    def __str__(self):
        return force_text(_('%s') % self.term)


class BeautifulGumtreeQuery(models.Model):
    id = models.AutoField(primary_key=True)

    label = models.ForeignKey(GumtreeCategoryLabel, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ManyToManyField(GumtreeCategory, blank=True)
    province = models.ForeignKey(GumtreeProvince, on_delete=models.CASCADE, blank=True, null=True)
    location = models.ManyToManyField(GumtreeLocation, blank=True)

    term = models.CharField(max_length=75)
    price_start = models.PositiveIntegerField(blank=True, null=True)
    price_end = models.PositiveIntegerField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    running = models.BooleanField(default=False)

    def get_results_count(self):
        count = BeautifulGumtreeResult.objects.filter(query__id=self.id).count()
        return count

    def get_results_by_category_count(self, category):
        count = BeautifulGumtreeResult.objects.filter(query__id=self.id, category=category).count()
        return count

    def get_results_by_location_count(self, location):
        count = BeautifulGumtreeResult.objects.filter(query__id=self.id, location=location).count()
        return count

    def __unicode__(self):
        return force_text(_('%s') % self.term)

    def __str__(self):
        return force_text(_('%s') % self.term)


class BeautifulGumtreeResult(models.Model):
    bgs = models.ForeignKey(BeautifulGumtreeSearch, on_delete=models.CASCADE)
    query = models.ForeignKey(BeautifulGumtreeQuery, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    subtitle = models.CharField(max_length=75)
    abstract = models.TextField(blank=True)
    image = models.CharField(max_length=75)
    price = models.CharField(max_length=75)

    location = models.ForeignKey(GumtreeLocation, blank=True, on_delete=models.CASCADE)
    label = models.ForeignKey(GumtreeCategoryLabel, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(GumtreeCategory, blank=True, on_delete=models.CASCADE)
    province = models.ForeignKey(GumtreeProvince, blank=True, on_delete=models.CASCADE)

    cell = models.CharField(max_length=75)
    email = models.EmailField(max_length=75)
    date_created = models.DateTimeField(_('created at'), auto_now_add=True)
    date_modified = models.DateTimeField(_('modified at'), auto_now=True)

    def admin_image(self):
        try:
            images = self.image.replace("[", "").replace("]", "").replace(",", "").split('src="')
            img = images[1].split('"')[0]
            # <picture><source srcset="https://i.ebayimg.com/images/g/2-oAAOSwHMhbsRBs/s-l800.webp" type="image/webp"><source srcset="https://i.ebayimg.com/images/g/2-oAAOSwHMhbsRBs/s-l800.jpg" type="image/jpeg"><img alt="2013 - 2017 zx6r zx636 kawasaki fairing kits" class="lazyloaded" src="https://i.ebayimg.com/images/g/2-oAAOSwHMhbsRBs/s-l800.jpg"/></source></source></picture>
            return '<img src="{}" />'.format(format_html(safe(img)))
        except:
            pass
        return ''

    admin_image.allow_tags = True

    def __unicode__(self):
        return force_text(_('%s') % self.bgs.allowed.name)

    def __str__(self):
        return force_text(_('%s') % self.bgs.allowed.name   )


class Picture(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    caption = models.TextField(blank=True)
    comments = GenericRelation('Comment')


class Gallery(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    image = FilerImageField(verbose_name=_('gallery images'), blank=True, null=True,
                                 on_delete=models.SET_NULL,
                                 related_name='djangocms_blog_post_gallery')
    caption = models.TextField(blank=True, default='Change Me')
    comments = GenericRelation('Comment')
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return force_text(_('%s') % self.caption)

    def __str__(self):
        return force_text(_('%s') % self.caption)


class Page(models.Model):
    slug = models.SlugField(unique=True)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    slug = models.SlugField(unique=True)
    body = models.TextField(blank=True)
    link = models.URLField(blank=True)
    file = models.FileField(upload_to=upload_dir)
    comments = GenericRelation('Comment')
    pictures = GenericRelation('Picture')
    page = models.ForeignKey(Page, on_delete=models.CASCADE)


class ExtendedPage(models.Model):
    page = models.ForeignKey(Page,
                             # unique=True,
                             verbose_name=_("Page"),
                             editable=False,
                             related_name='extended_fields',
                             on_delete=models.CASCADE
                             )
    description = models.TextField(blank=True)
    background_image = models.FileField(upload_to=upload_dir)


class PageDetailExtension(PageExtension):
    image = models.ImageField(upload_to=upload_dir)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to=upload_dir)


extension_pool.register(PageDetailExtension)
