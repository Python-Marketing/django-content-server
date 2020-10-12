from PIL import Image
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand

from api.models import *

from djangocms_blog.cms_appconfig import BlogConfig
from djangocms_blog.models import Post as BlogPost
from site_server.default_site import blogs, image_sizes, developer, AllowedSearchDomains
from filer.models import ThumbnailOption
from django.conf import settings


from tracker.models import Developer, Story, Task


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
        do = BlogPost.objects.all().count()
        if do == 0:
            for key, item in blogs.items():
                self.stdout.write("Adding Blog content {}".format(item['title']))

                from django.contrib.auth.models import User
                from django.core.files import File
                from filer.models import Image

                filename = 'file'
                user = User.objects.get(id=1)

                with open(item['image_path'] + item['image'], "rb") as f:

                    file_obj = File(f, name=item['image'])
                    image = Image.objects.create(owner=user,
                                                 original_filename=filename,
                                                 file=file_obj)
                    post = BlogPost()
                    post.author = user
                    post.title = item['title']
                    post.subtitle = item['subtitle']
                    post.abstract = item['abstract']
                    post.app_config = BlogConfig.objects.latest('id')
                    post.publish = True
                    post.main_image = image
                    post.save()

        # Adapting site settings
        self.stdout.write("Changing site details")
        do = Site.objects.all().count()
        if do == 1:
            site = Site.objects.get(id=1)
            site_name = getattr(settings, 'SITE_NAME', 'localhost')
            site_domain = getattr(settings, 'SITE_URL', 'http://127.0.0.1')
            site.name = site_name
            site.domain = site_domain
            site.save()

        # Example Story
        self.stdout.write("Setting up first Story")
        do = Story.objects.all().count()
        if do == 0:
            new_story = Story()
            new_story.name = "My First Story"
            new_story.description = "Learn about this site\n"
            new_story.description += "Get customer to use form"
            new_story.estimate = 1
            new_story.save()

        # We need to setup a developer for tracker
        self.stdout.write("Setting up Story developer")
        do = Developer.objects.all().count()
        if do == 0:
            delevoper = Developer()
            delevoper.first_name = developer['first_name']
            delevoper.last_name = developer['last_name']
            delevoper.save()

        # Example Task
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

        # TODO : Delete
        # do = 1#AllowedDomain.objects.all().count()
        # if do == 0:
        #     for key, item in AllowedSearchDomains.items():
        #         self.stdout.write("{}".format(key))
        #         domain = AllowedDomain()
        #         domain.name = key
        #         domain.class_names = ""#item['class_names']
        #         domain.id_names = ""#item['id_names']
        #         domain.save()
        self.stdout.write("Site ready")

