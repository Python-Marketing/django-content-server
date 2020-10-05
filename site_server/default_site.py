from django.contrib.sites.models import Site
from .settings import CMS_TEMPLATES
from django.contrib.auth.models import User

# Default page settings Not used for installation
# Content for adding a page
# Still under development
title = 'Django CMS setup'
description = 'Open Source programming at its best'

template = CMS_TEMPLATES[0][0]
language = 'en'
menu_title = title
slug = title.lower().replace(" ", "-")
meta_description = description
created_by = User.objects.get(id=1).get_full_name()
in_navigation = True
published = True
site = Site.objects.get(id=1)


xframe_options = 3
page_title = title

image_path = 'site_server/static/site-images/'

# Content can be added here for initial setup
blogs = {
    'Blog1': {
        'title':'Manage',
        'subtitle': 'This content was added with the setup_content_server.py script',
        'abstract': '<section class="features-section-8 relative background-light"><div class="container"><div class="row section-separator"><div class="col-md-12"><p class="mb-4"><img alt="" class="img-fluid" src="/static/images/background-1.jpg" width="96%" /></p><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis, eius mollitia suscipit, quisquam doloremque distinctio perferendis et doloribus unde architecto optio laboriosam porro adipisci sapiente officiis nemo accusamus ad praesentium? Esse minima nisi et. Dolore perferendis, enim praesentium omnis, iste doloremque quia officia optio deserunt molestiae voluptates soluta architecto tempora.</p><p>Molestiae cupiditate inventore animi, maxime sapiente optio, illo est nemo veritatis repellat sunt doloribus nesciunt! Minima laborum magni reiciendis qui voluptate quisquam voluptatem soluta illo eum ullam incidunt rem assumenda eveniet eaque sequi deleniti tenetur dolore amet fugit perspiciatis ipsa, odit. Nesciunt dolor minima esse vero ut ea, repudiandae suscipit!</p><h2 class="mb-3 mt-5">Molestiae cupiditate inventore animi, maxime sapiente optio</h2><p>Temporibus ad error suscipit exercitationem hic molestiae totam obcaecati rerum, eius aut, in. Exercitationem atque quidem tempora maiores ex architecto voluptatum aut officia doloremque. Error dolore voluptas, omnis molestias odio dignissimos culpa ex earum nisi consequatur quos odit quasi repellat qui officiis reiciendis incidunt hic non? Debitis commodi aut, adipisci.</p><p>Quisquam esse aliquam fuga distinctio, quidem delectus veritatis reiciendis. Nihil explicabo quod, est eos ipsum. Unde aut non tenetur tempore, nisi culpa voluptate maiores officiis quis vel ab consectetur suscipit veritatis nulla quos quia aspernatur perferendis, libero sint. Error, velit, porro. Deserunt minus, quibusdam iste enim veniam, modi rem maiores.</p><p>Odit voluptatibus, eveniet vel nihil cum ullam dolores laborum, quo velit commodi rerum eum quidem pariatur! Quia fuga iste tenetur, ipsa vel nisi in dolorum consequatur, veritatis porro explicabo soluta commodi libero voluptatem similique id quidem? Blanditiis voluptates aperiam non magni. Reprehenderit nobis odit inventore, quia laboriosam harum excepturi ea.</p><p>Adipisci vero culpa, eius nobis soluta. Dolore, maxime ullam ipsam quidem, dolor distinctio similique asperiores voluptas enim, exercitationem ratione aut adipisci modi quod quibusdam iusto, voluptates beatae iure nemo itaque laborum. Consequuntur et pariatur totam fuga eligendi vero dolorum provident. Voluptatibus, veritatis. Beatae numquam nam ab voluptatibus culpa, tenetur recusandae!</p><p>Voluptas dolores dignissimos dolorum temporibus, autem aliquam ducimus at officia adipisci quasi nemo a perspiciatis provident magni laboriosam repudiandae iure iusto commodi debitis est blanditiis alias laborum sint dolore. Dolores, iure, reprehenderit. Error provident, pariatur cupiditate soluta doloremque aut ratione. Harum voluptates mollitia illo minus praesentium, rerum ipsa debitis, inventore?</p><div class="tag-widget post-tag-container mb-5 mt-5">&nbsp;</div></div></div></div></section>',
        'image':'one.jpg',
        'image_path': image_path,

    },
    'Blog2': {
        'title': 'Django CMS',
        'subtitle': 'Now point and click and edit me',
        'abstract': '<section class="features-section-8 relative background-light"><div class="container"><div class="row section-separator"><div class="col-md-12"><p class="mb-4"><img alt="" class="img-fluid" src="/static/images/background-2.jpg" width="96%" /></p><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis, eius mollitia suscipit, quisquam doloremque distinctio perferendis et doloribus unde architecto optio laboriosam porro adipisci sapiente officiis nemo accusamus ad praesentium? Esse minima nisi et. Dolore perferendis, enim praesentium omnis, iste doloremque quia officia optio deserunt molestiae voluptates soluta architecto tempora.</p><p>Molestiae cupiditate inventore animi, maxime sapiente optio, illo est nemo veritatis repellat sunt doloribus nesciunt! Minima laborum magni reiciendis qui voluptate quisquam voluptatem soluta illo eum ullam incidunt rem assumenda eveniet eaque sequi deleniti tenetur dolore amet fugit perspiciatis ipsa, odit. Nesciunt dolor minima esse vero ut ea, repudiandae suscipit!</p><h2 class="mb-3 mt-5">Molestiae cupiditate inventore animi, maxime sapiente optio</h2><p>Temporibus ad error suscipit exercitationem hic molestiae totam obcaecati rerum, eius aut, in. Exercitationem atque quidem tempora maiores ex architecto voluptatum aut officia doloremque. Error dolore voluptas, omnis molestias odio dignissimos culpa ex earum nisi consequatur quos odit quasi repellat qui officiis reiciendis incidunt hic non? Debitis commodi aut, adipisci.</p><p>Quisquam esse aliquam fuga distinctio, quidem delectus veritatis reiciendis. Nihil explicabo quod, est eos ipsum. Unde aut non tenetur tempore, nisi culpa voluptate maiores officiis quis vel ab consectetur suscipit veritatis nulla quos quia aspernatur perferendis, libero sint. Error, velit, porro. Deserunt minus, quibusdam iste enim veniam, modi rem maiores.</p><p>Odit voluptatibus, eveniet vel nihil cum ullam dolores laborum, quo velit commodi rerum eum quidem pariatur! Quia fuga iste tenetur, ipsa vel nisi in dolorum consequatur, veritatis porro explicabo soluta commodi libero voluptatem similique id quidem? Blanditiis voluptates aperiam non magni. Reprehenderit nobis odit inventore, quia laboriosam harum excepturi ea.</p><p>Adipisci vero culpa, eius nobis soluta. Dolore, maxime ullam ipsam quidem, dolor distinctio similique asperiores voluptas enim, exercitationem ratione aut adipisci modi quod quibusdam iusto, voluptates beatae iure nemo itaque laborum. Consequuntur et pariatur totam fuga eligendi vero dolorum provident. Voluptatibus, veritatis. Beatae numquam nam ab voluptatibus culpa, tenetur recusandae!</p><p>Voluptas dolores dignissimos dolorum temporibus, autem aliquam ducimus at officia adipisci quasi nemo a perspiciatis provident magni laboriosam repudiandae iure iusto commodi debitis est blanditiis alias laborum sint dolore. Dolores, iure, reprehenderit. Error provident, pariatur cupiditate soluta doloremque aut ratione. Harum voluptates mollitia illo minus praesentium, rerum ipsa debitis, inventore?</p><div class="tag-widget post-tag-container mb-5 mt-5">&nbsp;</div></div></div></div></section>',
        'image': 'two.jpg',
        'image_path': image_path,
    },
    'Blog3': {
        'title': 'Django Blog',
        'subtitle': 'All content is a blog post and comments can be enabled',
        'abstract': '<section class="features-section-8 relative background-light"><div class="container"><div class="row section-separator"><div class="col-md-12"><p class="mb-4"><img alt="" class="img-fluid" src="/static/images/background-4.jpg" width="96%" /></p><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis, eius mollitia suscipit, quisquam doloremque distinctio perferendis et doloribus unde architecto optio laboriosam porro adipisci sapiente officiis nemo accusamus ad praesentium? Esse minima nisi et. Dolore perferendis, enim praesentium omnis, iste doloremque quia officia optio deserunt molestiae voluptates soluta architecto tempora.</p><p>Molestiae cupiditate inventore animi, maxime sapiente optio, illo est nemo veritatis repellat sunt doloribus nesciunt! Minima laborum magni reiciendis qui voluptate quisquam voluptatem soluta illo eum ullam incidunt rem assumenda eveniet eaque sequi deleniti tenetur dolore amet fugit perspiciatis ipsa, odit. Nesciunt dolor minima esse vero ut ea, repudiandae suscipit!</p><h2 class="mb-3 mt-5">Molestiae cupiditate inventore animi, maxime sapiente optio</h2><p>Temporibus ad error suscipit exercitationem hic molestiae totam obcaecati rerum, eius aut, in. Exercitationem atque quidem tempora maiores ex architecto voluptatum aut officia doloremque. Error dolore voluptas, omnis molestias odio dignissimos culpa ex earum nisi consequatur quos odit quasi repellat qui officiis reiciendis incidunt hic non? Debitis commodi aut, adipisci.</p><p>Quisquam esse aliquam fuga distinctio, quidem delectus veritatis reiciendis. Nihil explicabo quod, est eos ipsum. Unde aut non tenetur tempore, nisi culpa voluptate maiores officiis quis vel ab consectetur suscipit veritatis nulla quos quia aspernatur perferendis, libero sint. Error, velit, porro. Deserunt minus, quibusdam iste enim veniam, modi rem maiores.</p><p>Odit voluptatibus, eveniet vel nihil cum ullam dolores laborum, quo velit commodi rerum eum quidem pariatur! Quia fuga iste tenetur, ipsa vel nisi in dolorum consequatur, veritatis porro explicabo soluta commodi libero voluptatem similique id quidem? Blanditiis voluptates aperiam non magni. Reprehenderit nobis odit inventore, quia laboriosam harum excepturi ea.</p><p>Adipisci vero culpa, eius nobis soluta. Dolore, maxime ullam ipsam quidem, dolor distinctio similique asperiores voluptas enim, exercitationem ratione aut adipisci modi quod quibusdam iusto, voluptates beatae iure nemo itaque laborum. Consequuntur et pariatur totam fuga eligendi vero dolorum provident. Voluptatibus, veritatis. Beatae numquam nam ab voluptatibus culpa, tenetur recusandae!</p><p>Voluptas dolores dignissimos dolorum temporibus, autem aliquam ducimus at officia adipisci quasi nemo a perspiciatis provident magni laboriosam repudiandae iure iusto commodi debitis est blanditiis alias laborum sint dolore. Dolores, iure, reprehenderit. Error provident, pariatur cupiditate soluta doloremque aut ratione. Harum voluptates mollitia illo minus praesentium, rerum ipsa debitis, inventore?</p><div class="tag-widget post-tag-container mb-5 mt-5">&nbsp;</div></div></div></div></section>',
        'image': 'three.jpg',
        'image_path': image_path,
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

AllowedSearchDomains = {

    'nationalgeographic.com': {
        'class_names': '',
        'id_names': 'article__body'
    },
    'en.wikipedia.org': {
            'class_names': '',
            'id_names': 'mw-content-text'
    },
    'spaceplace.nasa.gov': {
            'class_names': '',
            'id_names': 'bodyContent'
    },
    'www.britannica.com': {
        'class_names': '',
        'id_names': 'ref1'
    },
    'www.space.com': {
        'class_names': 'content-wrapper',
        'id_names': ''
    },
    'www.sciencealert.com': {
        'class_names': 'responsive-articlepage',
        'id_names': ''
    },

    'spacecenter.org': {
        'class_names': 'single-post format-standard',
        'id_names': ''
    },
    'www.livescience.com': {
        'class_names': 'content-wrapper',
        'id_names': ''
    },
    'phys.org': {
        'class_names': 'news-article',
        'id_names': ''
    },
    'www.dw.com': {
        'class_names': '',
        'id_names': 'bodyContent'
    },
    'www.sun.org': {
        'class_names': 'white-field',
        'id_names': ''
    },
    'lco.global': {
        'class_names': 'section maincontent',
        'id_names': ''
    },
    'edition.cnn.com': {
        'class_names': 'pg-rail-tall__body',
        'id_names': ''
    },
    'www.bbc.com': {
        'class_names': 'column--primary',
        'id_names': ''
    },
    'www.nytimes.com': {
        'class_names': 'StoryBodyCompanionColumn',
        'id_names': ''
    },
}