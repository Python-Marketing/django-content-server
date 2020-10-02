# Django Content Server

So you have it running what now?

* [Link](DJANGOSETTINGS.md) Django Settings [Documentation](https://docs.djangoproject.com/en/3.1/)
* [Link](SETUPSCRIPT.md) Setup script : setup_content_server.py
* [Link](DJANGOALLAUTH.md) Django All Auth - [Documentation](https://django-allauth.readthedocs.io/en/latest/)
* [Link](DJANGOCMS.md) Django CMS - [Documentation](https://readthedocs.org/projects/django-cms/)
* [Link](DJANGOBLOG.md)Django Blog - [Documentation](https://djangocms-blog.readthedocs.io/en/latest/)
* [Link](DJANGORESTAPI.md) Built in Django restAPI - [Documentation](https://www.django-rest-framework.org/)
* Secure - [Read More](https://docs.djangoproject.com/en/3.1/topics/security/)
* [Link](TRACKER.md) Story, Task and Time tracker - [Code Base](https://pypi.org/project/django-tasktracker/)
* [Link](INVOICING.md) Invoicing on Time tracker - (in development) - [Code Base](https://pypi.org/project/django-invoicing/)

## Django Settings

###Why Django
Django is the most popular framework in Python for building web applications. It uses the Model View Template (MVT) pattern, which is a slightly modified version of the Model View Controller (MVC) pattern, in which the View works more like the Controller, and the Template acts as the View. Such a solution offers a flexible way of separating context and business logic - each layer has its own responsibilities.

Django helps developers by speeding up the development process. It includes its own Object Relation Mapping (ORM) layer for handling database access, sessions, routing, and multi-language support. It also takes care of security while handling requests. It includes an admin panel (called django-admin) for managing models data by default.

###Who's using it
It’s valued equally among startups, blue chip companies like Google, Quora, Netflix, and Spotify, and government organizations like NASA. Yet few people know why Python is one of the top programming languages for website development.

###Backbone
Python offers many features by default, with standard libraries that cover almost any programming task. From scientific calculations to image processing, operating system interfaces, and protocols, Python saves developers’ time and effort by presenting them with solutions they would otherwise have to build manually.


#### Under the hood settings.py

We are just going through the important settings related to the important packages.

[Django Settings](https://docs.djangoproject.com/en/3.1/ref/settings/) for more details...

This helps specify what's going on and where logging is stored

```
ENV = "DEVELOPMENT"
```

This SECRET_KEY for development isn't that important but for production keep it secret make it unique.
```
SECRET_KEY = 'Make me unique again'
```

#### Debugging

This display errors instead of a error page. In production this must be False

```
DEBUG = True
```

IP addresses you can use with the application, better than localhost as devices can connect.

```
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.3', '10.42.0.1', '10.42.0.122']
```

#### Site Configuration

When going live give the site a better name and use the domain name instead of 127.0.0.1 or localhost

```
SITE_ID = 1
SITE_NAME = 'localhost'
SITE_URL = 'http://127.0.0.1'
```

####NB change this IP address to the one you are using in ALLOWED_HOSTS.

Multiple sites can be created in the admin section.

####Databases

Database details. We only use sqlight but any database can be used!

```
DATABASE_NAME = 'project.db'

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': DATABASE_NAME,
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}
```

#### Installed Apps

This looks worse than it is. But all the applications are initiated here.

You can add applications to the end.

```

INSTALLED_APPS = [
    # make the admin section sparkle
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',

    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    # Main application
    'site_server',
    'django.contrib.sites',

    # Authentication modules from social media platforms
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.auth0',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.linkedin_oauth2',

    # Easy to get lost in the applications
    # But each of these give more functionality
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'mptt',
    'easy_thumbnails',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'djangocms_file',
    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',

    # App hooks
    'aldryn_apphooks_config',
    'parler',
    'taggit',
    'taggit_autosuggest',
    'meta',
    'sortedm2m',
    'djangocms_blog',
    'rest_framework',
    'rest_framework.authtoken',
    # Custom API
    'api',
    'shell_plus',
    'favicon',
    # Start of invoicing module
    'invoicing',
    'tracker',
    'widget_tweaks'

]
```

## Default Content : setup_content_server.py

In default_site.py we store some data we can use during installation:

```
# Content can be added here for initial setup
blogs = {
    'Blog1': {
        'title':'Manage',
        'subtitle': 'This content was added with the setup_content_server.py script',
        'abstract': '<section class="features-section-8 relative background-light"><div class="container"><div class="row section-separator"><div class="col-md-12"><p class="mb-4"><img alt="" class="img-fluid" src="/static/images/background-1.jpg" width="96%" /></p><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis, eius mollitia suscipit, quisquam doloremque distinctio perferendis et doloribus unde architecto optio laboriosam porro adipisci sapiente officiis nemo accusamus ad praesentium? Esse minima nisi et. Dolore perferendis, enim praesentium omnis, iste doloremque quia officia optio deserunt molestiae voluptates soluta architecto tempora.</p><p>Molestiae cupiditate inventore animi, maxime sapiente optio, illo est nemo veritatis repellat sunt doloribus nesciunt! Minima laborum magni reiciendis qui voluptate quisquam voluptatem soluta illo eum ullam incidunt rem assumenda eveniet eaque sequi deleniti tenetur dolore amet fugit perspiciatis ipsa, odit. Nesciunt dolor minima esse vero ut ea, repudiandae suscipit!</p><h2 class="mb-3 mt-5">Molestiae cupiditate inventore animi, maxime sapiente optio</h2><p>Temporibus ad error suscipit exercitationem hic molestiae totam obcaecati rerum, eius aut, in. Exercitationem atque quidem tempora maiores ex architecto voluptatum aut officia doloremque. Error dolore voluptas, omnis molestias odio dignissimos culpa ex earum nisi consequatur quos odit quasi repellat qui officiis reiciendis incidunt hic non? Debitis commodi aut, adipisci.</p><p>Quisquam esse aliquam fuga distinctio, quidem delectus veritatis reiciendis. Nihil explicabo quod, est eos ipsum. Unde aut non tenetur tempore, nisi culpa voluptate maiores officiis quis vel ab consectetur suscipit veritatis nulla quos quia aspernatur perferendis, libero sint. Error, velit, porro. Deserunt minus, quibusdam iste enim veniam, modi rem maiores.</p><p>Odit voluptatibus, eveniet vel nihil cum ullam dolores laborum, quo velit commodi rerum eum quidem pariatur! Quia fuga iste tenetur, ipsa vel nisi in dolorum consequatur, veritatis porro explicabo soluta commodi libero voluptatem similique id quidem? Blanditiis voluptates aperiam non magni. Reprehenderit nobis odit inventore, quia laboriosam harum excepturi ea.</p><p>Adipisci vero culpa, eius nobis soluta. Dolore, maxime ullam ipsam quidem, dolor distinctio similique asperiores voluptas enim, exercitationem ratione aut adipisci modi quod quibusdam iusto, voluptates beatae iure nemo itaque laborum. Consequuntur et pariatur totam fuga eligendi vero dolorum provident. Voluptatibus, veritatis. Beatae numquam nam ab voluptatibus culpa, tenetur recusandae!</p><p>Voluptas dolores dignissimos dolorum temporibus, autem aliquam ducimus at officia adipisci quasi nemo a perspiciatis provident magni laboriosam repudiandae iure iusto commodi debitis est blanditiis alias laborum sint dolore. Dolores, iure, reprehenderit. Error provident, pariatur cupiditate soluta doloremque aut ratione. Harum voluptates mollitia illo minus praesentium, rerum ipsa debitis, inventore?</p><div class="tag-widget post-tag-container mb-5 mt-5">&nbsp;</div></div></div></div></section>',

    },
    'Blog2': {
        'title': 'Django CMS',
        'subtitle': 'Now point and click and edit me',
        'abstract': '<section class="features-section-8 relative background-light"><div class="container"><div class="row section-separator"><div class="col-md-12"><p class="mb-4"><img alt="" class="img-fluid" src="/static/images/background-2.jpg" width="96%" /></p><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis, eius mollitia suscipit, quisquam doloremque distinctio perferendis et doloribus unde architecto optio laboriosam porro adipisci sapiente officiis nemo accusamus ad praesentium? Esse minima nisi et. Dolore perferendis, enim praesentium omnis, iste doloremque quia officia optio deserunt molestiae voluptates soluta architecto tempora.</p><p>Molestiae cupiditate inventore animi, maxime sapiente optio, illo est nemo veritatis repellat sunt doloribus nesciunt! Minima laborum magni reiciendis qui voluptate quisquam voluptatem soluta illo eum ullam incidunt rem assumenda eveniet eaque sequi deleniti tenetur dolore amet fugit perspiciatis ipsa, odit. Nesciunt dolor minima esse vero ut ea, repudiandae suscipit!</p><h2 class="mb-3 mt-5">Molestiae cupiditate inventore animi, maxime sapiente optio</h2><p>Temporibus ad error suscipit exercitationem hic molestiae totam obcaecati rerum, eius aut, in. Exercitationem atque quidem tempora maiores ex architecto voluptatum aut officia doloremque. Error dolore voluptas, omnis molestias odio dignissimos culpa ex earum nisi consequatur quos odit quasi repellat qui officiis reiciendis incidunt hic non? Debitis commodi aut, adipisci.</p><p>Quisquam esse aliquam fuga distinctio, quidem delectus veritatis reiciendis. Nihil explicabo quod, est eos ipsum. Unde aut non tenetur tempore, nisi culpa voluptate maiores officiis quis vel ab consectetur suscipit veritatis nulla quos quia aspernatur perferendis, libero sint. Error, velit, porro. Deserunt minus, quibusdam iste enim veniam, modi rem maiores.</p><p>Odit voluptatibus, eveniet vel nihil cum ullam dolores laborum, quo velit commodi rerum eum quidem pariatur! Quia fuga iste tenetur, ipsa vel nisi in dolorum consequatur, veritatis porro explicabo soluta commodi libero voluptatem similique id quidem? Blanditiis voluptates aperiam non magni. Reprehenderit nobis odit inventore, quia laboriosam harum excepturi ea.</p><p>Adipisci vero culpa, eius nobis soluta. Dolore, maxime ullam ipsam quidem, dolor distinctio similique asperiores voluptas enim, exercitationem ratione aut adipisci modi quod quibusdam iusto, voluptates beatae iure nemo itaque laborum. Consequuntur et pariatur totam fuga eligendi vero dolorum provident. Voluptatibus, veritatis. Beatae numquam nam ab voluptatibus culpa, tenetur recusandae!</p><p>Voluptas dolores dignissimos dolorum temporibus, autem aliquam ducimus at officia adipisci quasi nemo a perspiciatis provident magni laboriosam repudiandae iure iusto commodi debitis est blanditiis alias laborum sint dolore. Dolores, iure, reprehenderit. Error provident, pariatur cupiditate soluta doloremque aut ratione. Harum voluptates mollitia illo minus praesentium, rerum ipsa debitis, inventore?</p><div class="tag-widget post-tag-container mb-5 mt-5">&nbsp;</div></div></div></div></section>',

    },
    'Blog3': {
        'title': 'Django Blog',
        'subtitle': 'All content is a blog post and comments can be enabled',
        'abstract': '<section class="features-section-8 relative background-light"><div class="container"><div class="row section-separator"><div class="col-md-12"><p class="mb-4"><img alt="" class="img-fluid" src="/static/images/background-4.jpg" width="96%" /></p><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis, eius mollitia suscipit, quisquam doloremque distinctio perferendis et doloribus unde architecto optio laboriosam porro adipisci sapiente officiis nemo accusamus ad praesentium? Esse minima nisi et. Dolore perferendis, enim praesentium omnis, iste doloremque quia officia optio deserunt molestiae voluptates soluta architecto tempora.</p><p>Molestiae cupiditate inventore animi, maxime sapiente optio, illo est nemo veritatis repellat sunt doloribus nesciunt! Minima laborum magni reiciendis qui voluptate quisquam voluptatem soluta illo eum ullam incidunt rem assumenda eveniet eaque sequi deleniti tenetur dolore amet fugit perspiciatis ipsa, odit. Nesciunt dolor minima esse vero ut ea, repudiandae suscipit!</p><h2 class="mb-3 mt-5">Molestiae cupiditate inventore animi, maxime sapiente optio</h2><p>Temporibus ad error suscipit exercitationem hic molestiae totam obcaecati rerum, eius aut, in. Exercitationem atque quidem tempora maiores ex architecto voluptatum aut officia doloremque. Error dolore voluptas, omnis molestias odio dignissimos culpa ex earum nisi consequatur quos odit quasi repellat qui officiis reiciendis incidunt hic non? Debitis commodi aut, adipisci.</p><p>Quisquam esse aliquam fuga distinctio, quidem delectus veritatis reiciendis. Nihil explicabo quod, est eos ipsum. Unde aut non tenetur tempore, nisi culpa voluptate maiores officiis quis vel ab consectetur suscipit veritatis nulla quos quia aspernatur perferendis, libero sint. Error, velit, porro. Deserunt minus, quibusdam iste enim veniam, modi rem maiores.</p><p>Odit voluptatibus, eveniet vel nihil cum ullam dolores laborum, quo velit commodi rerum eum quidem pariatur! Quia fuga iste tenetur, ipsa vel nisi in dolorum consequatur, veritatis porro explicabo soluta commodi libero voluptatem similique id quidem? Blanditiis voluptates aperiam non magni. Reprehenderit nobis odit inventore, quia laboriosam harum excepturi ea.</p><p>Adipisci vero culpa, eius nobis soluta. Dolore, maxime ullam ipsam quidem, dolor distinctio similique asperiores voluptas enim, exercitationem ratione aut adipisci modi quod quibusdam iusto, voluptates beatae iure nemo itaque laborum. Consequuntur et pariatur totam fuga eligendi vero dolorum provident. Voluptatibus, veritatis. Beatae numquam nam ab voluptatibus culpa, tenetur recusandae!</p><p>Voluptas dolores dignissimos dolorum temporibus, autem aliquam ducimus at officia adipisci quasi nemo a perspiciatis provident magni laboriosam repudiandae iure iusto commodi debitis est blanditiis alias laborum sint dolore. Dolores, iure, reprehenderit. Error provident, pariatur cupiditate soluta doloremque aut ratione. Harum voluptates mollitia illo minus praesentium, rerum ipsa debitis, inventore?</p><div class="tag-widget post-tag-container mb-5 mt-5">&nbsp;</div></div></div></div></section>',

    },
}

# Usefull when adding images from the front end
image_sizes = {
    'Small': {
        'width': '400',
        'height': '300',
    },
    'Medium': {
        'width': '800',
        'height': '600',
    },
    'Large': {
        'width': '1024',
        'height': '768',
    }
}

developer = {
    'first_name': 'Jody',
    'last_name': 'Beggs',
}

```

This makes it easier to add the content we need for the site.

TODO : Add All Auth applications to the script

###Super User

Superuser details, this is just for convenience, not secure to store password like this.

```
    # Edit these details for you use cas
    superuser = 'developer'
    superuser_email = 'django.python.pro@gmail.com'
    superuser_password = 'password'
```
#####So remember to empty it.

### Runserver

Runserver just runs the application wait until installation is complete or use (ctrl - c) to cancel

```
    # Setup the django handling
    # only use this if not using Pycharm or another way of running the server
    runserver = False
```

###Database Updates and Migrations

For a new installation must be set to true or if models are changed

```
    # Do you need to migrate the database? Safer to leave True
    # if you have changed models it must be True
    migrate = True
```

###Sqlight Database Backup

This only works for sqlight databases in development

```
    # Do you need to backup the database? Safer to leave True (We are using sqlight)
    backup = True
    # How many as in how many copies since script is run.
    no_backups = 1
```

# PIP requirements installation

Install requirements in needed for new installations and updates to pip packages

```
    # Get pip involved?
    install_requirements = True
```

## Reset

Sometimes deleting everything and starting again is best. This creates a backup of the current db with the ext .reset

```
    # This deletes the database creating a reset copy on the last database
    # Use wisely...
    reset = True
```

###Initialise CMS

Love django, now we can add default content.

under `site_server/management/commands` in `initialize_cms.py`

```
    # This runs the custom script in site_server/management initialize_cms.py
    add_default_content = True

```

Again this is for convenience. We can add default content and site settings during installation.


### Logging

`/var/log/` is used to store log files but anywhere can be chosen.

```

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
try:
    LOG_DIR = "/var/log/" + ENV
except:
    LOG_DIR = "/var/log/" + ENV

```

The `ENV` variable allows easy management of environments!


## Django All Auth

###NB Only work on All Auth when you have a url to work with.

Otherwise you end up creating two applications for everything...

In the settings.py file you will find this block of code you will find 3 providers :

Google, Facebook and LinkedIn - All that's needed is an application from each social media platform and the client_id and secret.

```# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '',
            'secret': '',
            'key': ''
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_GB',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.5',
        'APP': {
            'client_id': '',
            'secret': '',
            'key': ''
        }
    },
    'linkedin': {
        'HEADERS': {
            'x-li-src': 'msdk'
        },
        'SCOPE': [
            'r_basicprofile',
            'r_emailaddress'
        ],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'picture-url',
            'public-profile-url',
        ],
        'APP': {
            'client_id': '',
            'secret': '',
            'key': ''
        }
    }
}
```

To enable social login we need to add the client_id and secret for the providers in the settings.py file.

###Then under the admin section for Social Account

`/admin/socialaccount/socialapp/`
 
enable the social login by adding the details there.

Login url is `/accounts/social_login/`

These settings pertain to Social Login
```
LOGIN_REDIRECT_URL = "/?social_login=true"
LOGOUT_REDIRECT_URL = "/"
LOGIN_URL = '/accounts/social_login/'

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False  # a personal preference. True by default. I don't want users to be interrupted by logging in
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # a personal preference. I don't want to add 'i don't remember my username' like they did at Nintendo, it's stupid
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'myapp:email_success'  # a page to identify that email is confirmed
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7  # a personal preference. 3 by default
ACCOUNT_EMAIL_REQUIRED = True  # no questions here
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # as the email will be used for login
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True  # False by default
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True  # True by default
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_USERNAME_BLACKLIST = ['suka', 'blyat', ]  # :D
ACCOUNT_USERNAME_MIN_LENGTH = 4  # a personal preference
ACCOUNT_SESSION_REMEMBER = True  # None by default (to ask 'Remember me?'). I want the user to be always logged in
SOCIALACCOUNT_AVATAR_SUPPORT = True
LOGIN_ON_EMAIL_CONFIRMATION = True
```


For a list of providers

[List of Providers](https://django-allauth.readthedocs.io/en/latest/providers.html)

##Django CMS

First things first: djangoCMS is powered by Django. This means all the great advantages of it will be present on django-CMS.

It is backed by Divio, a Django-pioneer company — and our official partner. Divio offers world-class development tools for agencies and organizations.

###Admin UI

One of the strong points of djangoCMS is its user interface. The admin UI is and cleaner and better structured than the official Django admin site.

New users who have never used Django won’t have any difficulties in getting comfortable with djangoCMS. It’s really easy to understand!

Django CMS is a very robust yet simple and straightforward open source content management solution. It is so powerful that international organizations, brands, and companies including L’Oreal, National Geographic, and Parrot, have opted to use Django CMS to power its content management and delivery systems. Django CMS offers unparalleled versatility, ease of use, and that appeal to novices that attracts even the world’s leading content management professionals and developers.

Another highlight that is evident in Django CMS is that the platform is a very mature project. Hundreds of core developers are working tirelessly to improve the product and enhance user experience by adding new and useful features while eliminating bugs that hamper its performance.

We can specify multiple languages but site limited to one

```
CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'hide_untranslated': False,
            'public': True,
            'redirect_on_fallback': True,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

```

Default template loaded, added more templates here otherwise you cannot access them when you create pages.

```
# Default template used
CMS_TEMPLATES = (
    ('includes/home.html', 'Home'),
)

```

CMS placeholder configuration.

TODO : Expand
```
CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
    'content': {
        'name': gettext('Content'),
        'plugins': ['TextPlugin', 'LinkPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body': '<p>Great websites : %(_tag_child_1)s and %(_tag_child_2)s</p>'
                },
                'children': [
                    {
                        'plugin_type': 'LinkPlugin',
                        'values': {
                            'name': 'django',
                            'url': 'https://www.djangoproject.com/'
                        },
                    },
                    {
                        'plugin_type': 'LinkPlugin',
                        'values': {
                            'name': 'django-cms',
                            'url': 'https://www.django-cms.org'
                        },
                    },
                ]
            },
        ]
    }
}

```


##Django Blog



http://127.0.0.1:8000/

Will have many layers

http://127.0.0.1:8000/?edit to see the django CMS login

http://127.0.0.1:8000/admin for the django admin panel

Username and password are created during installation.

Lookin `setup_content_server.py`

Once logged in double click in any textbox and a popup will appear. You can add images and edit the content.