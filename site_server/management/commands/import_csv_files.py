import csv
import os
import xml.etree.ElementTree as ET

from django.core.management.base import BaseCommand
from django.core.validators import validate_email
from api.models import *
'''Path to my CSV'''
path = os.path.abspath(os.getcwd()) + "/site_server/management/commands/"


class Command(BaseCommand):

    def __init__(self):
        super().__init__()
        self.max_depth = 0

    def handle(self, **options):
        self.stdout.write("Initialize Import")

        file = path + 'api_gumtreeprovince.csv'

        '''We open the CSV from the file'''
        with open(file) as csvfile:

            do = GumtreeProvince.objects.all().count()
            if not do:
                GumtreeProvince.objects.all().delete()
                for line in csvfile:
                    values = line.split(',')
                    province = GumtreeProvince()
                    province.name = values[1]
                    province.link = values[2]
                    province.key = values[3]
                    province.save()

        file = path + 'api_gumtreecategorylabel.csv'

        '''We open the CSV from the file'''
        with open(file) as csvfile:
            do = GumtreeCategoryLabel.objects.all().count()
            if not do:
                GumtreeCategoryLabel.objects.all().delete()
                for line in csvfile:
                    values = line.split(',')
                    label = GumtreeCategoryLabel()
                    label.name = values[1]
                    label.link = values[2]
                    label.key = values[3]
                    label.save()

        file = path + 'api_gumtreecategory.csv'

        '''We open the CSV from the file'''
        with open(file) as csvfile:
            GumtreeCategory.objects.all().delete()
            for line in csvfile:
                values = line.split(',')
                cat = GumtreeCategory()
                cat.name = values[1]
                cat.link = values[2]
                cat.key = values[3]
                cat.label = GumtreeCategoryLabel.objects.get(id=values[4])
                cat.save()


        file = path + 'api_gumtreelocation.csv'

        '''We open the CSV from the file'''
        with open(file) as csvfile:
            GumtreeLocation.objects.all().delete()
            for line in csvfile:
                values = line.split(',')
                loc = GumtreeLocation()
                loc.name = values[1]
                loc.link = values[2]
                loc.key = values[3]
                self.stdout.write("Initialize Import")
                self.stdout.write(str(values[1]))
                self.stdout.write(str(values[4]))
                loc.province = GumtreeProvince.objects.get(id=values[4])
                loc.save()