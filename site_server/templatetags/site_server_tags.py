from django import template
from django.utils.html import format_html

from api.models import Donation, Testimonial, Video
from djangocms_blog.models import Post
from cms.models import Page, ImproperlyConfigured, reverse, get_language, os, Q, PageUser

register = template.Library()


def query_lookup(query='', filter=[], pages=[]):
    results = []
    for q in query:
        for v in filter:
            if q.title.find(v) != -1 and v not in pages:
                results.append(q)
    return results


@register.simple_tag
def query_filter(query={}, value='', random=False, number=False):

    pages = [
        "Home", "Projects", "News", "Gallery", "Videos", "About", "Contact", "Events"
    ]

    values = value.split(',')
    results = query_lookup(query, values, pages)

    if len(results) == 0:
        search = Q()
        for value in values:
            search.add(Q(translations__title__icontains=value), Q.OR)


        query = Post.objects.filter(search)#.exclude(translations__title=value).exclude(translations__title__in=pages)
        results = query_lookup(query, values)

    if number:
        return results[0]

    # if len(results) == 1:
    #     if value not in pages:
    #         return results[0]

    if random:
        try:
            import random
            results = random.choice(results)
        except:
            pass

    return results

@register.simple_tag
def random_background(page_list={}, list=''):
    images = ['blank.jpg']

    from random import randrange
    random_index = randrange(len(images))


    import random
    result = random.choice(images)
    return images[random_index]

@register.simple_tag
def render_navigation(page_list={}, list=''):

    active_pages = list.split(',')
    links = ['<a class="nav-item-child nav-item-hover active" href="#Home">Home</a>']
    for page in page_list:
        if page.title in active_pages:
            links.append('<a class="nav-item-child nav-item-hover" href="#{}">{}</a>'.format(
                '', page.title.replace(' ', ''), page.title)
            )

    html = ''
    for link in links:
        html += '<li class="nav-item">'
        html += link
        html += '</li>'

    return format_html(html)
