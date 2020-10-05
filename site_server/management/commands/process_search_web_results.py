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


def get_image_string(img):
    src = ''
    for i in img:
        try:
            src += i.get('src') + ","
        except:
            pass
        title = i.get('title')
    return src


def clean_soup(content):
    for tags in content.findAll(True):
        tags.attrs = {}
    return content


def save_search(self, soup, search, results, src):
    search_result = BeautifulGoogleResult()
    search_result.bgs = search
    try:
        title = soup.find('head').text
    except:
        title = "Errir"
    search_result.title = title
    search_result.subtitle = " ".join(str(results.get_text()).split()[:5])
    search_result.abstract = str(results.get_text())
    search_result.image = src
    search_result.save()
    return search_result


def create_blog_post(self, results, src, title, search):
    path = "media/"
    image = False
    # Google image search has limits
    google_search_images = False
    # We need a valid big image
    page_images = False
    # Manual search
    manual_search = True

    # Seems to be working but this whole file need adapting
    if manual_search:

        from urllib.request import Request, urlopen
        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'
        accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        req = Request(search.link, headers={
            'User-Agent': user_agent,
        })
        try:
            content = urlopen(req).read().decode('utf-8')
            html = BeautifulSoup(content, "html.parser")
        except:
            html = BeautifulSoup()

        for img in html.find_all("img"):

            try:
                src = str(img['src'])
            except:
                src = 'None'

            if src.find(".jpg") != -1 and src.find("http") != -1 or \
                    src.find(".png") != -1 and src.find("http") != -1:

                name = src.split("/")[-1]

                if name.find("?"):
                    name = name.split("?")[0]
                try:
                    opener = urllib.request.build_opener()
                    opener.addheaders = [('User-agent', user_agent), ('Accept', accept)]
                    urllib.request.install_opener(opener)

                    urllib.request.urlretrieve(src, path + name)
                    im = Image.open(path + name)
                except Exception as e:
                    self.stdout.write(str("test : " + str(e)))
                    continue

                width, height = im.size
                if width > 500 and height > 200:
                    with open(path + name, "rb") as f:
                        file_obj = File(f, name=name)
                        from django.contrib.auth.models import User
                        image = FilerImage.objects.create(owner=User.objects.get(id=1),
                                                          original_filename=path + name,
                                                          file=file_obj)
                        os.system("rm {}".format(path + name))
                        break
                else:
                    os.system("rm {}".format(path + name))

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

    if image:
        self.stdout.write(str("We have a image"))
        try:
            instance = BlogPost.objects.filter(translations__title=title)[0]
        except:
            instance = BlogPost()

        instance.author = User.objects.get(id=1)
        instance.title = title
        instance.subtitle = " ".join(str(results.get_text()).split()[:5])

        content = ""
        n = 0
        for c in results.find_all('p'):

            if len(str(c).split()) > 20:
                content += "<p>" + str(c) + "</p>"
            n += 1
            if n == 10:
                break

        read_more = '''
            <div class="btn-form">
                <a target="_blank" href="{}" class="btn btn-fill right-icon">Read More <i class="icon icons8-advance"></i></a>
            </div>
        '''.format(search.link)

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

        abstract = style
        instance.abstract = abstract
        instance.app_config = BlogConfig.objects.latest('id')
        instance.publish = True
        if image:
            instance.main_image = image
        try:
            instance.save()
        except:
            return False
        return instance
    return False


class Command(BaseCommand):

    def handle(self, **options):

        self.stdout.write("Initialize Web content CMS")
        searches = BeautifulGoogleSearch.objects.all()
        # Lets process the searches and save the results
        for search in searches:
            soup = BeautifulSoup(search.body, 'html.parser')

            img = soup.findAll('img')
            src = get_image_string(img)

            if search.allowed.class_names != '':
                self.stdout.write("Class : " + str(search.allowed.class_names))
                results = soup.find(class_=search.allowed.class_names)
            if search.allowed.class_names != '':
                self.stdout.write("ID : " + str(search.allowed.id_names))
            else:
                results = soup.find()

            if results:
                for s in soup.select('img'):
                    s.extract()

                results = clean_soup(results)
                saved_search_result = save_search(self, soup, search, results, src)
                post = create_blog_post(self, results, src, saved_search_result.title, search)

        self.stdout.write("Site ready")
