# Some utilities to add blog posts and pages
from aldryn_apphooks_config.utils import setup_config

from cms.api import create_page
from django.contrib.sites.models import Site

from djangocms_blog.cms_appconfig import BlogConfig
from site_server.settings import CMS_TEMPLATES


# This will create a page with the settings in default_site.py
def create_new_page(self, title="Blank", description="Default", created_by="", is_home=False):
    self.stdout.write("Creating Page")
    template = CMS_TEMPLATES[0][0]
    language = 'en'
    menu_title = title
    slug = title.lower().replace(" ", "-")
    meta_description = description
    from django.contrib.auth.models import User
    if created_by == "":
        created_by = User.objects.get(id=1).get_full_name()
    in_navigation = True
    published = True
    site = Site.objects.get(id=1)
    xframe_options = 3
    page_title = title

    self.stdout.write("Title : {}".format(title))
    # Call the create_page function from cms.api

    app_hook = BlogConfig()
    app_hook.default_published = False
    app_hook.namespace = title.lower()
    app_hook.title = title
    app_hook.app_title = title
    #app_hook.app_title
    app_hook.save()


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
        page_title=page_title,
        is_home=False
    )
