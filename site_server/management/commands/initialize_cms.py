from PIL import Image
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand

from api.models import *
from cms.api import create_page
from djangocms_blog.cms_appconfig import BlogConfig
from djangocms_blog.models import Post as BlogPost
from site_server.default_site import blogs, image_sizes, developer, AllowedSearchDomains
from filer.models import ThumbnailOption

from django.conf import settings


# This will create a page with the settings in default_site.py
from tracker.models import Developer, Story, Task


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
        do = ThumbnailOption.objects.all().count()
        if do == 0:
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
        do = 1#BlogPost.objects.all().count()
        if do == 0:
            for key, item in blogs.items():
                self.stdout.write("Adding Blog content {}".format(item['title']))

                from django.contrib.auth.models import User
                from django.core.files import File
                from filer.models import Image

                filename = 'file'
                filepath = 'path/to/file'
                user = User.objects.get(id=1)

                with open(item['image_path'] + item['image'], "rb") as f:

                    file_obj = File(f, name=item['image'])
                    image = Image.objects.create(owner=user,
                                                 original_filename=filename,
                                                 file=file_obj)
                    instance = BlogPost()
                    instance.author = user
                    instance.title = item['title']
                    instance.subtitle = item['subtitle']
                    instance.abstract = item['abstract']
                    instance.app_config = BlogConfig.objects.latest('id')
                    instance.publish = True
                    instance.main_image = image
                    instance.save()

        self.stdout.write("Changing site details")
        do = Site.objects.all().count()
        if do == 0:
            site = Site.objects.get(id=1)
            site_name = getattr(settings, 'SITE_NAME', 'localhost')
            site_domain = getattr(settings, 'SITE_URL', 'http://127.0.0.1')
            site.name = site_name
            site.domain = site_domain
            site.save()

        self.stdout.write("Setting up first Story")
        do = Story.objects.all().count()
        if do == 0:
            new_story = Story()
            new_story.name = "My First Story"
            new_story.description = "Learn about this site\n"
            new_story.description += "Get customer to use form"
            new_story.estimate = 1
            new_story.save()
        self.stdout.write("Setting up Story developer")
        do = Developer.objects.all().count()
        if do == 0:
            delevoper = Developer()
            delevoper.first_name = developer['first_name']
            delevoper.last_name = developer['last_name']
            delevoper.save()

        self.stdout.write("Setting up Story Task")
        do = Task.objects.all().count()
        if do == 0:
            task = Task()
            task.name = 'First task for Story'
            task.description = "Own the website and content"
            task.estimate = 1
            task.iteration = 1
            task.completed = False
            task.developer = Developer.objects.get(id=1)
            task.parent_story = Story.objects.get(id=1)
            task.save()

        do = AllowedDomain.objects.all().count()
        if do == 0:
            for key, item in AllowedSearchDomains.items():
                self.stdout.write("{}".format(key))
                domain = AllowedDomain()
                domain.name = key
                domain.class_names = ""#item['class_names']
                domain.id_names = ""#item['id_names']
                domain.save()
        self.stdout.write("Site ready")

