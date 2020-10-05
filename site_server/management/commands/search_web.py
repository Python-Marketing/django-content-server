import sys

# This will create a page with the settings in default_site.py
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from api.models import *


class Command(BaseCommand):

    def handle(self, **options):
        self.stdout.write("Initialize Web content CMS")

        search_results = {

        }
        try:
            from googlesearch import search
        except ImportError:
            self.stdout.write("No module named 'google' found")

            # to search
        queries = [
            "science supernovae news 2020",
            "science Python Programming news 2020",
            "science evolution and paleontology 2020",
            "science rockets elon musk 2020",
            "science abiogenesis 2020",
        ]

        for query in queries:
            try:

                for j in search(query, tld="co.in", num=10, stop=10, pause=0):
                    self.stdout.write(j)
                    domain = j.split("://")[1].split("/")[0]

                    try:
                        allowed = AllowedDomain.objects.filter(name=domain).latest('id')
                    except:
                        allowed = AllowedDomain()
                        allowed.name = domain
                        allowed.class_names = ''
                        allowed.id_names = ''
                        allowed.save()

                    page = requests.get(j)
                    soup = BeautifulSoup(page.content, 'html.parser')

                    if soup:
                        BGsearch = BeautifulGoogleSearch()
                        BGsearch.allowed = allowed
                        BGsearch.term = query
                        BGsearch.link = j
                        BGsearch.body = soup.prettify()
                        BGsearch.save()
            except:
                self.stdout.write(str(sys.exc_info()))
                self.stdout.write("error {}".format(query))

        self.stdout.write("Site ready")
