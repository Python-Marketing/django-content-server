import sys

# This will create a page with the settings in default_site.py
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from api.models import AllowedDomain, BeautifulGoogleSearch
from api.utils.page import create_new_page
from djangocms_blog.cms_appconfig import BlogConfig
from djangocms_blog.models import Post as BlogPost


class Command(BaseCommand):

    def handle(self, **options):
        self.stdout.write("Initialize Web content CMS")

        search_results = {

        }
        from googlesearch import search
        # to search and eventually create pages and full those pages with content
        queries = {
            "Hubble": "Hubble images science news random",
        }
        from cms.models import Page
        # Lets remove the default pages
        try:
            default_pages = Page.objects.all().delete()
            # Hack to delete the configs properly...
            default_blog_posts = BlogPost.objects.filter().delete()
            default_pages = Page.objects.filter(id=1).delete()
            default_configs = BlogConfig.objects.filter(id=1).delete()
        except:
            pass

        n = 0
        for page, terms in queries.items():
            is_home = False
            if n == 0:
                is_home = True
            create_new_page(self, title=page, description=terms, is_home=is_home)
            n += 1
            try:
                for j in search(terms, tld="co.in", num=13, stop=13, pause=0):
                    self.stdout.write(j)
                    domain = j.split("://")[1].split("/")[0]

                    # Added for control later
                    try:
                        allowed = AllowedDomain.objects.filter(domain=domain).latest('id')
                    except:
                        allowed = AllowedDomain()
                        allowed.name = domain
                        allowed.domain = domain
                        allowed.term = terms
                        allowed.page_name = page
                        allowed.class_names = ''
                        allowed.id_names = ''
                        allowed.save()
                    # Typical user agent
                    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'
                    accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
                    html = requests.get(j, headers={'User-agent': user_agent, 'Accept': accept})
                    # Give the content of the request to BeautifulSoup
                    soup = BeautifulSoup(html.content, 'html.parser')

                    # Soup tastes yummy
                    if soup:
                        # Create an instance of the search and move on
                        bg_search = BeautifulGoogleSearch()
                        bg_search.allowed = allowed
                        bg_search.term = terms
                        bg_search.link = j
                        bg_search.body = soup.prettify()
                        bg_search.save()
            except:
                self.stdout.write(str(sys.exc_info()))
                self.stdout.write("error {}".format(terms))

        self.stdout.write("Site nearly ready, one more step.")
