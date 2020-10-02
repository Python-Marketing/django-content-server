# Django Content Server

[Home](https://github.com/Python-Marketing/django-content-server)

## Django All Auth

### NB Only work on All Auth when you have a url to work with.

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

### Then under the admin section for Social Account

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

