import os
import sys
import time

# This will create a page with the settings in default_site.py
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from rest_framework.utils import json

from api.models import AllowedDomain, BeautifulGoogleSearch, BeautifulGoogleResult, BeautifulGumtreeResult, \
    BeautifulGumtreeSearch, GumtreeCategory, GumtreeProvince, GumtreeCategoryLabel, GumtreeLocation
from djangocms_blog.cms_appconfig import BlogConfig
from djangocms_blog.models import Post as BlogPost


def add_location(self, name='', link='', key='', province=None, parent=None):
    location = GumtreeLocation()
    location.name = name.replace("&amp;", "")
    location.link = link
    location.key = key
    location.parent = parent
    location.province = province
    location.save()
    return location

class Command(BaseCommand):

    def __init__(self, **args):
        super().__init__()

        self.terms = ""
        self.page = ""
        self.version = ""
        self.category = ""
        self.done = False
        self.url_start = 'https://www.gumtree.co.za'
        self.location_url = 'https://www.gumtree.co.za/pages/locations/'
        self.location = ''

        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'
        accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"

        self.headers = {'User-agent': user_agent, 'Accept': accept}
        BeautifulGumtreeResult.objects.all().delete()
        BeautifulGumtreeSearch.objects.all().delete()
        GumtreeCategoryLabel.objects.all().delete()
        GumtreeCategory.objects.all().delete()
        GumtreeProvince.objects.all().delete()
        GumtreeLocation.objects.all().delete()

    def handle(self, **options):

        self.stdout.write("Initialize Gumtree")
        # sa_location = GumtreeLocation()
        # sa_location.name = 'South Africa'
        # sa_location.link = 'all-the-ads'
        # sa_location.key = 'b0'
        # sa_location.save()
        # getting the home page and using those resolts
        results = requests.get(self.url_start, headers=self.headers)
        self.stdout.write(results.url)
        #  Load into BeautifulSoup
        main_page = BeautifulSoup(results.content, features="lxml")
        # Get a category list
        category_list = BeautifulSoup(
            str(main_page.find('ul', attrs={'id': 'flexLftBuckt'})), features="lxml"
        ).findAll('li')
        #
        provincial_divs = main_page.find(
            'div', attrs={'id': 'wrapper'}
        ).findAll(
            'div', attrs={'class': 'bottom-keyword-wrapper'}
        )[1]

        locations = requests.get(
            self.location_url, headers=self.headers
        )
        locations_page = BeautifulSoup(locations.content, features="lxml")
        # locations_page = locations_page.find(
        #     'ul', attrs={'id': 'locations'}
        # )

        if str(provincial_divs).find('Provinces')!=-1:
            for word in str(provincial_divs).split('<a class="bottom-keyword"'):
                if word.find('href') != -1:
                    province = GumtreeProvince()
                    province.name = str(word).split('">')[1].split('</a>')[0]
                    province.link = str(word).split('p1"')[0].split("/")[1].replace("s-", "")
                    key = str(word).split('href="/')[1].split('"')[0].split("/")[1].replace("p1", "")
                    province.key = key.replace('v1', '')
                    province.save()


        for province in GumtreeProvince.objects.all():

            province_url = self.url_start + '/s-' + province.link + '/v1' + province.key + "p1"
            provincial_locations = requests.get(province_url, headers=self.headers)
            self.stdout.write(str(province_url))
            self.stdout.write(str(provincial_locations.url))
            self.stdout.write(str(province_url == provincial_locations.url))
            if province_url == provincial_locations.url:
                locations_page = BeautifulSoup(provincial_locations.content, features="lxml")
                locations_links = locations_page.find(
                    'li', attrs={
                        'class': 'location-filter'
                    }
                ).find_all('a')

                for a_tag in locations_links:

                    key = str(a_tag).split(
                        '<a href="/s-'
                    )[1].split('"')[0].split("/")[1]
                    key = key.replace("v1", "").replace("p1", "")

                    link = str(a_tag).split(
                        '<a href="/s-'
                    )[1].split('"')[0].split("/")[0]
                    name = str(a_tag).split('title="')[1].split('"')[0]
                    check = GumtreeLocation.objects.filter(link=link)

                    if check.count() == 0:

                        if name != "South Africa":

                            area_location = add_location(self, name, link, key, province, None)

                            area_url = self.url_start + '/s-' + link + '/v1' + key + "p1"
                            area_locations = requests.get(area_url, headers=self.headers)
                            area_locations = BeautifulSoup(area_locations.content, features="lxml")
                            try:

                                area_links = area_locations.find(
                                    'li', attrs={
                                        'class': 'location-filter'
                                    }
                                ).find_all('a')

                            except:
                                area_links = []

                            if len(area_links) > 2:

                                for a_tag in area_links:
                                    key = str(a_tag).split(
                                        '<a href="/s-'
                                    )[1].split('"')[0].split("/")[1]
                                    key = key.replace("v1", "").replace("p1", "")

                                    link = str(a_tag).split(
                                        '<a href="/s-'
                                    )[1].split('"')[0].split("/")[0]
                                    name = str(a_tag).split('title="')[1].split('"')[0]
                                    province_check = GumtreeProvince.objects.filter(name=name)
                                    check = GumtreeLocation.objects.filter(link=link)
                                    exluded = ['South Africa', 'Gauteng']
                                    if check.count() == 0 and province_check.count() == 0 and name not in exluded:
                                        self.stdout.write(str((name)))
                                        area_sub_location = add_location(self, name, link, key, province, area_location)

        for a in category_list:

            try:
                if str(a).find('<h3 class="label">') != -1:
                    label = GumtreeCategoryLabel()
                    label.name = str(a).split('<h3 class="label">')[1].split('</h3>')[0].replace("&amp;", "and")
                    label.link = str(a).split('href="/')[1].split('/')[0].replace("s-", "")
                    key = str(str(a).split('href="/')[1]).split('"')[0].split("/")[1].replace("s-", "")
                    label.key = key.replace('v1', '').replace('p1', '')
                    label.save()
            except:
                pass

            try:
                categories = BeautifulSoup(str(a), features="lxml").find('ul').find_all('a')
                for cat in categories:
                    category = GumtreeCategory()
                    category.label = label
                    category.name = str(cat).split('">')[1].split('</a>')[0].replace("&amp;", "and")
                    category.link = str(cat).split('href="/')[1].split("/")[0].replace("s-", "")
                    key = str(cat).split('<a href="/')[1].split('"')[0].split("/")[1]
                    category.key = key.replace('v1', '').replace('p1', '').replace("s-", "")
                    category.save()
            except:
                pass


        self.stdout.write(str(GumtreeCategoryLabel.objects.all().count()))
        self.stdout.write(str(GumtreeCategory.objects.all().count()))
        self.stdout.write(str(GumtreeProvince.objects.all().count()))
        self.stdout.write(str(GumtreeLocation.objects.all().count()))
        self.stdout.write("Gumtree ready...")
