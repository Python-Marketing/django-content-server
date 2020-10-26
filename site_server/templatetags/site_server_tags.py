from django import template
from django.utils.html import format_html

from api.models import BeautifulGumtreeQuery, GumtreeLocation, GumtreeProvince, GumtreeCategory, GumtreeCategoryLabel
from cms.models import Q
from djangocms_blog.models import Post
from tracker.models import Story

register = template.Library()


@register.simple_tag
def get_location_results_count(query, location):
    return query.get_results_by_location_count(location)


@register.simple_tag
def get_category_results_count(query, category):
    return query.get_results_by_category_count(category)


def query_lookup(query='', filter=[], pages=[]):
    results = []
    for q in query:
        for v in filter:
            if q.title.find(v) != -1 and v not in pages:
                results.append(q)
    return results


@register.simple_tag
def search_locations(request):
    locations = GumtreeLocation.objects.filter(parent__isnull=False).order_by('name').exclude(parent__name="South Africa")
    select = '<option>Please Select</option>'
    for l in locations:
        select += "<option class='{} {}' value='{}'>{}</option>".format(str(l.province.link).replace('+', '-'),str(l.parent.link).replace('+', '-'), l.id, l.name)
    return select


@register.simple_tag
def search_provinces(request):
    province = GumtreeProvince.objects.all()
    select = '<option>Please Select</option>'
    for p in province:
        select += "<option value='{}'>{}</option>".format(p.link, p.name)
    return select


@register.simple_tag
def search_categories(request):
    categories = GumtreeCategory.objects.all()
    select = '<option>Please Select</option>'
    for c in categories:
        select += "<option style='display:none;' class='{}' value='{}'>{}</option>".format(c.label.link, c.id, c.name)
    return select


@register.simple_tag
def search_areas(request):
    locations = GumtreeLocation.objects.filter(parent__isnull=True).order_by('name').exclude(parent__name="South Africa")
    select = '<option>Please Select</option>'
    for l in locations:
        select += "<option class='{} {}' value='{}'>{}</option>".format(str(l.province.link).replace('+', '-'), l.link, l.link, l.name)
    return select


@register.simple_tag
def search_label(request):
    labels = GumtreeCategoryLabel.objects.all()
    select = '<option>Please Select</option>'
    for l in labels:
        select += "<option value='{}'>{}</option>".format(l.link, l.name)
    return select


@register.simple_tag
def gumtree_query(request):
    return BeautifulGumtreeQuery.objects.all()


@register.simple_tag
def query_filter(request, query={}, value='', random=False, number=False):

    values = value.split(',')
    search = Q()
    for value in values:
        search.add(Q(translations__title__icontains=value), Q.OR)

    query = Post.objects.filter(search).exclude(publish=False).exclude(main_image__isnull=True)
    results = query_lookup(query, values)

    if number:
        return results[0]

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


@register.simple_tag
def render_productivity():
    est = 0
    html = ""
    for story in Story.objects.all():
        html += "<tr>"
        html += "<td>{}</td>".format(story.id)
        html += "<td>{}</td>".format(story)
        completed = story.get_completed_tasks()
        style = 'text-success'
        if int(completed) == 0:
            style = 'text-danger'
        html += "<td class='{}'>{}</td>".format(style, completed)
        todo = story.get_todo_tasks()
        if int(todo) == 0:
            todo = ''
        html += "<td class='text-danger'>{}</td>".format(todo)
        html += "<td class=''><button onclick='add_task({})' class='btn btn-success'>Task</button></td>".format(
            story.id)
        html += "</tr>"

    return format_html(html)


@register.simple_tag
def render_portfolio_building():
    return Story.objects.all()
