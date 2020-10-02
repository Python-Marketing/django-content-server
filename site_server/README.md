# Django Content Server

[Home](../)

## Django Settings

### Why Django
Django is the most popular framework in Python for building web applications. It uses the Model View Template (MVT) pattern, which is a slightly modified version of the Model View Controller (MVC) pattern, in which the View works more like the Controller, and the Template acts as the View. Such a solution offers a flexible way of separating context and business logic - each layer has its own responsibilities.

Django helps developers by speeding up the development process. It includes its own Object Relation Mapping (ORM) layer for handling database access, sessions, routing, and multi-language support. It also takes care of security while handling requests. It includes an admin panel (called django-admin) for managing models data by default.

### Who's using it
It’s valued equally among startups, blue chip companies like Google, Quora, Netflix, and Spotify, and government organizations like NASA. Yet few people know why Python is one of the top programming languages for website development.

### Backbone
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

#### Databases

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