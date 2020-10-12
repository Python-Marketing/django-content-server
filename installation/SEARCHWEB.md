# Django Content Server

[Home](https://github.com/Python-Marketing/django-content-server)

## Add Web Content
### NB : This removes any content on the site
Just wanted some good images to test against

run `python3 manage.py search_web`

### After this we need to configure the new pages created.

Log into the admin section http://127.0.0.1:9000/admin/cms/page/

The username and password are in `setup_content_server.py`

![Page](edit_page.jpg)

### Find the advanced options

![Page](advanced.jpg)

![Page](advanced2.jpg)

### Find the Application option

![Page](application.jpg)

### And change it then save the Page

![Page](application2.jpg)

### Publish Changes, hover over the blue dot then click publish

![Page](application3.jpg)

### Green is good

![Page](green.jpg)

## Ok hard work done

run `python3 manage.py process_search_web_results`


## This will process the following query and populate the site.


```
        queries = {
            "Hubble": "Hubble images science news random",
        }
```
