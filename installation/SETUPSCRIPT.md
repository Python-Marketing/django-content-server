# Django Content Server

[Home](https://github.com/Python-Marketing/django-content-server)

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

### Super User

Superuser details, this is just for convenience, not secure to store password like this.

```
    # Edit these details for you use cas
    superuser = 'developer'
    superuser_email = 'django.python.pro@gmail.com'
    superuser_password = 'password'
```
##### So remember to empty it.

### Runserver

Runserver just runs the application wait until installation is complete or use (ctrl - c) to cancel

```
    # Setup the django handling
    # only use this if not using Pycharm or another way of running the server
    runserver = False
```

### Database Updates and Migrations

For a new installation must be set to true or if models are changed

```
    # Do you need to migrate the database? Safer to leave True
    # if you have changed models it must be True
    migrate = True
```

### Sqlight Database Backup

This only works for sqlight databases in development

```
    # Do you need to backup the database? Safer to leave True (We are using sqlight)
    backup = True
    # How many as in how many copies since script is run.
    no_backups = 1
```

## PIP requirements installation

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

```
    # scrape the web
    add_web_content = True

```

Added this to start scraping content. There is so much, lets use it.