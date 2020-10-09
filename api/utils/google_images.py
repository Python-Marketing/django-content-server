import os
import urllib.request

from PIL import Image
# This will create a page with the settings in default_site.py
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.core.files import File
from django.core.management.base import BaseCommand
from filer.models import Image as FilerImage

from api.models import *
from djangocms_blog.cms_appconfig import BlogConfig
from djangocms_blog.models import Post as BlogPost

def create_blog_post(self, results, src, title, search):
    supported_images = [".gif", ".png", ".jpg", ".jpeg"]
    path = "media/"
    image = False
    # Google image search has limits
    google_search_images = False
    # We need a valid big image
    page_images = False
    # Manual search
    manual_search = True

    # First attempted not really working
    if page_images:
        for url in src.split(","):
            if url.find("http") != -1:
                name = url.split("/")[-1]

                try:
                    urllib.request.urlretrieve(url, path + name)
                    im = Image.open(path + name)
                except:
                    os.system("rm {}".format(path + name))
                    continue

                width, height = im.size
                if width > 850 and height > 400:
                    with open(path + name, "rb") as f:

                        file_obj = File(f, name=name)
                        image = FilerImage.objects.create(owner=User.objects.get(id=1),
                                                          original_filename=path + name,
                                                          file=file_obj)
                        os.system("rm {}".format(path + name))
                        break

                else:
                    os.system("rm {}".format(path + name))


    # Not in use limited requests
    if google_search_images:

        api_key = "AIzaSyBr5FSmPl_RffFM_X_bLQXGFOBm8DborDY"
        from google_images_search import GoogleImagesSearch

        # you can provide API key and CX using arguments,
        # or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
        gis = GoogleImagesSearch(api_key, "ff9add50d98a394d6")

        # define search params:
        _search_params = {
            'q': title,
            'num': 1,
            # 'safe': 'off', #high|medium|off
            # 'fileType': 'png', #jpg|gif|png
            # 'imgType': 'photo', #clipart|face|lineart|news|photo
            'imgSize': 'XXLARGE',  # huge|icon|large|medium|small|xlarge|xxlarge
            # 'imgDominantColor': 'white', #black|blue|brown|gray|green|pink|purple|teal|white|yellow
            # 'rights': '' #cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived
        }

        gis.search(search_params=_search_params)
        for image in gis.results():
            try:
                image.download('media/')
                with open(image.path, "rb") as f:

                    file_obj = File(f, name=image.path.split('/')[1])
                    image = FilerImage.objects.create(owner=User.objects.get(id=1),
                                                      original_filename=image.path,
                                                      file=file_obj)
                break
            except:
                pass
                image = False