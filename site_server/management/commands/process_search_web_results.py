import os
import urllib.request

from PIL import Image
# This will create a page with the settings in default_site.py
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.core.files import File
from django.core.management.base import BaseCommand
from filer.models import Image as FilerImage

from api.models import BeautifulGoogleResult, Gallery, BeautifulGoogleSearch
from djangocms_blog.cms_appconfig import BlogConfig
from djangocms_blog.models import Post as BlogPost
from cms.models import Page

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
        title = soup.find('title').text
        search_result.title = title
        search_result.subtitle = " ".join(str(results.get_text()).split()[:10])
        search_result.abstract = str(results.get_text())
        search_result.image = src
        search_result.save()
        return search_result
    except:
        self.stdout.write("Title Not found, useless moving on")

    return False


'''Don't judge me...'''
def create_blog_post(self, results, src, title, search):
    supported_images = [".gif", ".png", ".jpg", ".jpeg"]
    path = "media/"
    image = False
    # Seems to be working but this whole file need adapting
    self.stdout.write(str("Lets create the blog post or edit it, if it exists!"))
    try:
        instance = BlogPost.objects.filter(translations__title=title)[0]
    except:
        instance = BlogPost()
    from django.contrib.auth.models import User

    instance.author = User.objects.get(id=1)
    instance.title = title
    instance.subtitle = " ".join(str(results.get_text()).split()[:5])

    n,content = 0, ""
    for c in results.find_all('p'):

        if len(str(c).split()) > 20:
            content += "<p>" + str(c) + "</p>"

        if n == 10:
            break
        n += 1
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
    instance.app_config = BlogConfig.objects.filter(namespace=search.allowed.page_name.lower())[0]
    instance.publish = True
    try:
        instance.save()
    except:
        return False

    html = BeautifulSoup(search.body, "html.parser")
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'
    accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"

    for img in html.find_all("img"):

        try:
            src = str(img['src'])
        except:
            src = 'None'

        # An attempt to ge more image url, seemed to work
        if src != "None":
            # Missing domains and other image url issues
            if src.find("http") == -1:
                data = search.link
                if src.find("//")!=-1:
                    src = "https:" + src
                else:
                    domain = data.split("//")
                    domain = domain[0] + "//" + domain[1].split("/")[0]
                    src = domain + src

        # For each supported image
        for supported in supported_images:
            # We need http or https
            if src.find(supported) != -1 and src.find("http") != -1:

                # Clean out name
                name = src.split("/")[-1]
                if name.find("?"):
                    name = name.split("?")[0]

                try:
                    # Copy image from the net with headers
                    opener = urllib.request.build_opener()
                    opener.addheaders = [('User-agent', user_agent), ('Accept', accept)]
                    urllib.request.install_opener(opener)
                    # Save the image
                    urllib.request.urlretrieve(src, path + name)
                    # Open the image to use
                    im = Image.open(path + name)
                except Exception as e:
                    self.stdout.write(str("Error : " + str(e)))
                    self.stdout.write(str(src))
                    im = False

                # Deal with an image
                if im:
                    width, height = im.size
                    # Check width and height
                    if width > 600 and height > 300:
                        with open(path + name, "rb") as f:
                            file_obj = File(f, name=name)
                            from django.contrib.auth.models import User
                            # Add to gallery for later access
                            gallery = Gallery()
                            gallery.blog_post = instance
                            gallery.caption = instance.title
                            gallery.image = FilerImage.objects.create(owner=User.objects.get(id=1),
                                                              original_filename=path + name,
                                                              file=file_obj)
                            gallery.save()
                            # Remove the file from os
                            os.system("rm {}".format(path + name))
                            # We still need to add an image to the blog post
                            image = gallery.image

                    else:
                        os.system("rm {}".format(path + name))
    # Check if gallery is available
    if instance.get_gallery_image():
        self.stdout.write(str("Saving Main Image"))
        instance.image = image
        instance.save()
        # Set image but run get_gallery_image to set image
        instance.get_gallery_image()

    return instance


class Command(BaseCommand):

    def handle(self, **options):
        self.stdout.write("Initialize Web content CMS")
        # Make sure that each pages application object is set and the application config added.
        searches = BeautifulGoogleSearch.objects.all()
        # Lets process the searches and save the results
        for search in searches:
            soup = BeautifulSoup(search.body, 'html.parser')

            img = soup.findAll('img')
            src = get_image_string(img)
            # Sites can be set with id's and classes to look for
            # Helps be more accurate
            if search.allowed.class_names != '':
                self.stdout.write("Class : " + str(search.allowed.class_names))
                results = soup.find(class_=search.allowed.class_names)
            if search.allowed.class_names != '':
                self.stdout.write("ID : " + str(search.allowed.id_names))
                results = soup.find(id=search.allowed.id_names)
            else:
                # Just going blind here
                results = soup.find()

            if results:

                results = clean_soup(results)
                # Save everything
                saved_search_result = save_search(self, soup, search, results, src)
                if saved_search_result:
                    # ugly function need to fix
                    post = create_blog_post(self, results, src, saved_search_result.title, search)

        self.stdout.write("Site ready")
