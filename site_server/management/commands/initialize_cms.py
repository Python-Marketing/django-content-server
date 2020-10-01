from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand

from api.models import *
from cms.api import create_page
from djangocms_blog.cms_appconfig import BlogConfig
from djangocms_blog.models import Post as BlogPost
from site_server.default_site import blogs, image_sizes
from filer.models import ThumbnailOption

from django.conf import settings

# This will create a page with the settings in default_site.py
def create_new_page(self):
    self.stdout.write("Creating Page")
    from site_server.default_site import (
        title, template, language, menu_title, slug,
        meta_description, created_by, in_navigation,
        published, site, xframe_options, page_title,
    )
    self.stdout.write("Title : {}".format(title))
    # Call the create_page function from cms.api
    create_page(
        title=title,
        template=template,
        language=language,
        menu_title=menu_title,
        slug=slug,
        meta_description=meta_description,
        created_by=created_by,
        in_navigation=in_navigation,
        published=published,
        site=site,
        xframe_options=xframe_options,
        page_title=page_title
    )


class Command(BaseCommand):

    def handle(self, **options):
        self.stdout.write("Initialize CMS")
        # Add some image options
        for key, item in image_sizes.items():
            self.stdout.write("Adding image option {} : {} x {}".format(key, item['width'], item['height']))
            ThumbnailOption(
                name=key,
                width=item['width'],
                height=item['height'],
                crop=False,
                upscale=False
            ).save()
        # Adding the default blog content
        from django.contrib.auth.models import User
        for key, item in blogs.items():
            self.stdout.write("Adding Blog content {}".format(item['title']))
            BlogPost(
                author=User.objects.get(id=1),
                title=item['title'],
                subtitle=item['subtitle'],
                abstract=item['abstract'],
                app_config=BlogConfig.objects.latest('id'),
                publish=True
            ).save()
        self.stdout.write("Changing site details")
        site = Site.objects.get(id=1)
        site_name = getattr(settings, 'SITE_NAME', 'localhost')
        site_domain = getattr(settings, 'SITE_URL', 'http://127.0.0.1')
        site.name = site_name
        site.domain = site_domain
        site.save()
        self.stdout.write("Site ready")
