import os
import sys
import time
import daemon
# This will create a page with the settings in default_site.py
from random import randint

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from rest_framework.utils import json

from api.models import AllowedDomain, BeautifulGoogleSearch, BeautifulGoogleResult, BeautifulGumtreeResult, \
    BeautifulGumtreeSearch, BeautifulGumtreeQuery, GumtreeCategoryLabel, GumtreeCategory, GumtreeProvince
from djangocms_blog.cms_appconfig import BlogConfig
from djangocms_blog.models import Post as BlogPost


def clean_string(string):
    return string.replace(" ", "+").lower()


def build_url(self, n):

    if n == 1:
        pageURL = '{}/s-{}/{}/v1{}{}p{}?q={}+{}'.format(
            self.url_start,
            self.category.link,
            self.location.link,
            self.category_key,
            self.location_key,
            n,
            clean_string(self.query.term),
            ''
        )

    else:
        pageURL = '{}/s-{}/{}/page-{}/v1{}{}p{}'.format(
            self.url_start,
            self.category.link,
            self.location.link,
            n,
            self.category_key,
            self.location_key,
            n,
            #clean_string(self.query.term)
        )

    self.stdout.write("pageURL : ".format(str(pageURL)))
    return pageURL


def get_abstract(link, content):
    read_more = '''
        <div class="btn-form">
            <a target="_blank" href="{}" class="btn btn-fill right-icon">Read More <i class="icon icons8-advance"></i></a>
        </div>
    '''.format(link)

    style = '''
        <section class="features-section-8 relative background-light">
            <div class="container">
                <div class="row section-separator">
                    {}
                    <div class="col-md-12">
                        <div class="tag-widget post-tag-container mb-5 mt-5">
                            {}
                        </div>
                    </div>
                </div>
            </div>
        </section>
    '''.format(read_more, content)

    return style


def html_parser(self, results):
    self.stdout.write("HTML Parser")
    gtsoup = BeautifulSoup(results.content, features="lxml")

    try:
        add_count = gtsoup.find(
            'span', attrs={'class': 'ads-count'}
        ).text.split("Ads")[0].replace(" ", "").replace(",","")
    except:
        add_count = 1

    if int(add_count) == 0:
        self.stdout.write("Stopping nothing found...")
        self.done = True

    gt_li = gtsoup.findAll('div', attrs={'class': 'related-item'})

    for node in gt_li:

        if self.done:
            self.stdout.write("Stopping : {}".format('done'))
            continue

        if len(node.contents) > 0:

            title = node.find('div', attrs={'class': 'title'}).text

            text_descption = node.find('span', attrs={'class': 'description-text'}).text
            location_date = node.find('div', attrs={'class': 'location-date'}).text
            img_src = str(node.find('img', attrs={'class': 'lazyload'})).split('data-src="')[1].split('"')[0]
            link_main_ad = self.url_start + str(node.find('a', attrs={'class': 'related-ad-title'})).split('href="')[1].split('"')[0]

            main_page = requests.get(link_main_ad, headers=self.headers)
            main_page = BeautifulSoup(main_page.content, features="lxml")

            try:
                general_details = main_page.find('div', attrs={'class': 'vip-general-details'}).text
            except:
                general_details = False

            gallery_images = main_page.findAll('picture')
            #gallery_images = str(gallery_images[0]) + str(gallery_images[1])

            domain = link_main_ad

            try:
                old_search = BeautifulGumtreeSearch.objects.get(term=self.terms, link=link_main_ad)
            except:
                old_search = False

            if not old_search:
                # Create an instance of the search and move on
                bg_search = BeautifulGumtreeSearch()
                bg_search.allowed = self.allowed
                bg_search.term = self.terms
                bg_search.link = link_main_ad
                bg_search.body = main_page.prettify()
                bg_search.save()

                search_result = BeautifulGumtreeResult()
                search_result.bgs = bg_search

                search_result.title = title
                search_result.subtitle = text_descption
                search_result.abstract = get_abstract(link_main_ad, location_date)
                search_result.image = gallery_images
                search_result.price = ""

                try:
                    search_result.location_id = self.location.id
                    search_result.province_id = self.location.province.id
                except:
                    search_result.province_id = self.location.id
                    search_result.location_id = self.location.id

                search_result.category_id = self.category.id
                try:
                    search_result.label_id = self.category.label.id
                except:
                    search_result.label_id = self.category.id

                # location = models.ForeignKey(GumtreeLocation, blank=True, on_delete=models.CASCADE)
                # label = models.ForeignKey(GumtreeCategoryLabel, blank=True, on_delete=models.CASCADE)
                # category = models.ForeignKey(GumtreeCategory, blank=True, on_delete=models.CASCADE)
                # province = models.ForeignKey(GumtreeProvince, blank=True, on_delete=models.CASCADE)
                # location = models.ForeignKey(GumtreeLocation, blank=True, on_delete=models.CASCADE)


                search_result.cell = ""
                search_result.email = ""
                search_result.query = self.query

                search_result.save()


def scrape_gumtree_page_n(self, n):

    self.stdout.write("scrape_gumtree_page : {}".format(n))

    url = build_url(self, n)

    self.stdout.write("pageURL : {}".format(url))
    # Added for control later
    try:
        allowed = AllowedDomain.objects.filter(domain=url).latest('id')
    except:
        allowed = AllowedDomain()
        allowed.name = url
        allowed.domain = url
        allowed.term = self.terms
        allowed.page_name = "Gumtree"
        allowed.class_names = ''
        allowed.id_names = ''
        allowed.save()

    self.allowed = allowed

    results = requests.get(url, headers=self.headers)

    return_url = str(results.url)

    if return_url != url and n != 1:
        self.stdout.write("url : {}".format(url))
        self.stdout.write("return_url : {}".format(return_url))
        self.next = True

    return results


def gumtree_search(self, num=0, stop=0, pause=0):
    self.stdout.write("Terms : {}".format(self.terms))

    for n in range(1, num+1):

        if n == stop or self.done:
            self.stdout.write("Stopping : {}".format(stop))
            break

        self.stdout.write("n : {}".format(n))

        # try:
        scraped = scrape_gumtree_page_n(self, n)

        if self.next:
            self.stdout.write("Next : {}".format(self.next))
            break

        html_parser(self, scraped)
        # except Exception as e:
        #     self.stdout.write(str(sys.exc_info()))
        #     self.stdout.write(str(e))
        #     self.stdout.write("error {}".format(self.terms))

        if pause != 0:
            self.stdout.write("Pausing : {}".format(pause))
            time.sleep(pause)

    # self.query.running = False
    # self.query.save()

    return True


def run_daemon(self):

    if self.query.location.all().count() == 0 and self.query.category.all().count() == 0:
        self.stdout.write("Easiest search...")
        self.location = self.query.province
        self.category = self.query.label.link
        self.location_key = self.query.province.key
        self.category_key = self.query.label.key
        gumtree_search(self, num=50, stop=50, pause=3)

    elif self.query.location.all().count() == 0:
        self.stdout.write("No Locations...")
        self.location = self.query.province
        self.location_key = self.query.province.key
        self.category_key = self.query.label.key
        for category in self.query.category.all():
            self.category = category
            self.done = False
            self.next = False
            gumtree_search(self, num=50, stop=50, pause=3)

    elif self.query.category.all().count() == 0:
        self.stdout.write("No Categories...")
        self.category = self.query.label
        self.category_key = self.query.label.key
        for location in self.query.location.all():
            self.location_key = self.location.key
            self.location = location
            self.done = False
            self.next = False
            gumtree_search(self, num=50, stop=50, pause=3)

    else:
        self.stdout.write("No province going through locations...")
        for location in self.query.location.all():
            self.location = location
            self.location_key = location.key
            for category in self.query.category.all():
                self.category = category
                self.category_key = category.key
                self.done = False
                self.next = False
                gumtree_search(self, num=50, stop=50, pause=3)
    return 1


class Command(BaseCommand):

    def __init__(self, **args):
        super().__init__()

        self.terms = ""
        self.page = ""
        self.category = "s-all-the-ads"
        self.done = False
        self.next = False
        self.url_start = 'https://www.gumtree.co.za'
        self.location = ''
        self.query = False

        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'
        accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        self.headers = {'User-agent': user_agent, 'Accept': accept}

    def handle(self, **options):

        self.stdout.write("Initialize Web content CMS")

        queries = BeautifulGumtreeQuery.objects.filter(running=False)[:1]

        for query in queries:
            query.running = True
            query.save()

            self.query = query
            self.done = False
            self.next = False
            self.page = None
            self.terms = clean_string(self.query.term)
            self.stdout.write("Before daemon")

            run_daemon(self)

            query.running = False
            query.save()
            self.stdout.write("After daemon")

        self.stdout.write("Site nearly ready, one more step.")
