# Django Content Server

So you have it running what now?


* [Readme](installation) Installation [Documentation](https://docs.djangoproject.com/en/3.1/)
* [Readme](site_server) Django Settings [Documentation](https://docs.djangoproject.com/en/3.1/)
* [Readme](installation/SETUPSCRIPT.md) Setup script : setup_content_server.py
* [Readme](allauth) Django All Auth - [Documentation](https://django-allauth.readthedocs.io/en/latest/)
* [Readme](cms) Django CMS - [Documentation](https://readthedocs.org/projects/django-cms/)
* [Readme](djangocms_blog) Django Blog - [Documentation](https://djangocms-blog.readthedocs.io/en/latest/)
* [Readme](api) Built in Django restAPI - [Documentation](https://www.django-rest-framework.org/)
* Secure - [Read More](https://docs.djangoproject.com/en/3.1/topics/security/)
* [Readme](tracker) Story, Task and Time tracker - [Code Base](https://pypi.org/project/django-tasktracker/)
* [Readme](invoicing) Invoicing on Time tracker - (in development) - [Code Base](https://pypi.org/project/django-invoicing/)


## Features

Added web scraping capabilities. 

In the `site_server/management/commands` folder in `search_web.py`

```            
        # to search
        queries = [
            "science supernovae news 2020",
            "science Python Programming news 2020",
            "science evolution and paleontology 2020",
            "science rockets elon musk 2020",
            "science abiogenesis 2020",
        ]
```

Adds content on given search params. The more specific the search the better the results.


### NB still in development

Backend 90% complete still need to working on a descent front end to display content.
Started adding newsbit template.




 Compiled by Jody Beggs