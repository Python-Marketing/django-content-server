import sys

# This will create a page with the settings in default_site.py
import requests
from bs4 import BeautifulSoup
from cms.models import Title
from django.core.management.base import BaseCommand

from api.models import *
from api.utils.page import create_new_page
from djangocms_blog.cms_appconfig import BlogConfig


class Command(BaseCommand):

    def handle(self, **options):
        self.stdout.write("Initialize Web content CMS")

        search_results = {

        }
        try:
            from googlesearch import search
        except ImportError:
            self.stdout.write("No module named 'google' found")

        # to search and eventually create pages and full those pages with content
        queries = {
            "Universe": "Supernova Gallaxies Hubble 2020",
            "Abiogenesis": "Abiogenesis evolution science 2020",
            "Tom Cruise": "Tom Cruise latest gossip 2020",
            "Python": "Jobs Python Cape Town",
        }
        from cms.models import Page
        #default_pages = Page.objects.all().delete()
        #default_titles = Title.objects.all().delete()
        #default_configs = BlogConfig.objects.all().delete()
        n = 0
        for page, terms in queries.items():
            if n == 0:
                create_new_page(self, title=page, description=terms, is_home=True)
            else:
                create_new_page(self, title=page, description=terms, is_home=False)
            n+=1
            try:
                for j in search(terms, tld="co.in", num=10, stop=10, pause=0):
                    self.stdout.write(j)
                    domain = j.split("://")[1].split("/")[0]

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

                    html = requests.get(j)
                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup:
                        bg_search = BeautifulGoogleSearch()
                        bg_search.allowed = allowed
                        bg_search.term = terms
                        bg_search.link = j
                        bg_search.body = soup.prettify()
                        bg_search.save()
            except:
                self.stdout.write(str(sys.exc_info()))
                self.stdout.write("error {}".format(terms))

        self.stdout.write("Site ready")
