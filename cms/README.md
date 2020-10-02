# Django Content Server

[Home](..)

## Django CMS

First things first: djangoCMS is powered by Django. This means all the great advantages of it will be present on django-CMS.

It is backed by Divio, a Django-pioneer company — and our official partner. Divio offers world-class development tools for agencies and organizations.

### Admin UI

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