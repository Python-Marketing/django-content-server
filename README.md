# Django Content Server


### What is it?


Built on Django this collection on modules aims to simplify the creation and updating of content on a website or web application.


## Django

* Installation : [Read me](installation) - [Django Documentation](https://docs.djangoproject.com/en/3.1/)
* Django Settings : [Read me](site_server) - [Settings Documentation](https://docs.djangoproject.com/en/3.1/topics/settings/)

some reviews :

[Why Django is the Best Web Framework for Your Project](https://steelkiwi.com/blog/why-django-best-web-framework-your-project/)

[What is Django? Advantages and Disadvantages](https://hackr.io/blog/what-is-django-advantages-and-disadvantages-of-using-django)


### Content management

We can scrape content from the web or design it before hand.

Updating the same way, lets work smarter not harder.

### Setup script :  [Readme](installation/SETUPSCRIPT.md) setup_content_server.py

This adds 3 blogs to a page automatically

### Web Content :  [Readme](installation/SEARCHWEB.md) `python3 manage.py search_web`

Added web scraping capabilities. 

In the `site_server/management/commands` folder in `search_web.py`

```            
        # to search
        queries = {
            "Hubble": "Hubble images science news random",
        }
```

Adds content on given search params. The more specific the search the better the results.

But its not just Django.

## Django CMS and Django CMS Blog

On Django we have Django CMS and Django CMS Blog.

* Django CMS : [Readme](cms) - [Documentation](https://readthedocs.org/projects/django-cms/)
* Django Blog : [Readme](djangocms_blog) - [Documentation](https://djangocms-blog.readthedocs.io/en/latest/)

By default allows some amazing editing functionality.

### Rest API

* Built in Django restAPI : [Read me](api) - [Documentation](https://www.django-rest-framework.org/)

To help simplify the site requirements

### Social User Management

* Django All Auth : [Read me](allauth) - [Documentation](https://django-allauth.readthedocs.io/en/latest/)

### Secure

* Secure - [Read More](https://docs.djangoproject.com/en/3.1/topics/security/)

### NB still in development

Backend 90% complete still need to get working on a descent front end to display content.
Started adding newsbit template.


* [Readme](tracker) Story, Task and Time tracker - [Code Base](https://pypi.org/project/django-tasktracker/)
* [Readme](invoicing) Invoicing on Time tracker - (in development) - [Code Base](https://pypi.org/project/django-invoicing/)


## Features

### Some Packages used:

#### Google Search
google [Link](https://pypi.org/project/google/)

Easy access to a search result and then Beautiful Soup takes over

#### Beautiful Soup 4 webscraping
beautifulsoup4 [Link](https://pypi.org/project/BeautifulSoup/)

Easy to work with, just the different elements in countless websites to deal with.

#### I like this package 
but has low limits easy to get images

Google-Images-Search [Link](https://pypi.org/project/Google-Images-Search/)

Can be enabled and used...

#### Bootstrap 4 out of the box

djangocms-bootstrap4 [Link](https://pypi.org/project/djangocms-bootstrap4/)

Make styling simpler for a backend developer

#### Easily manage files and images

With Jango CMS and Filer everything is point and click

django-filer [Link](https://pypi.org/project/django-filer/)




 Compiled by Jody Beggs 
