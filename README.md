# django-rest-react-boilerplate

Use this to create new django rest and react projects.

## Current version

* v.01 - initial setup

## Pending Tasks

* Install react

## Getting Started

### Prerequisites

```
Python 3.6.8

# pip log
pip install django==3.0.3
pip install django-rest-framework
pip install django-rest-knox
```

### **Installing**

1. Clone repository into a python virtual environment
2. Install packages\
`pip install -r requirements.txt`
3. Optional: rename project\
`python manage.py rename <yourprojectname> <newprojectname>`

#### Checklist
* Secret Key settings:
    * SECRET_KEY:
        * changed?
        * hidden?
* TEMPLATES:
    * Default:
        * 'DIRS': [],
    * Options:
        * 'DIRS: [BASE_DIR + '/templates/'],
        * 'DIRS': ['../../static_root/project_root/templates/'],
* STATIC FILES:
    * STATICFILES_DIRS = [os.path.join('../../static_root/project_root/static'),]

## Accessing the user models

To be completed ...\
**profiles.models.Profile** extends the **django.contrib.auth.models.User**

```
from django.contrib.auth import get_user_model
USER = get_user_model()
from accounts.models import Profile  
```

## Deployment

To be completed ...

## Coding Style

HTML elements, classes, and filenames typically use "-" instead of a "_" naming convention for spaces.

```
Example: To be completed ...
```

NOTE: The 'django.contrib.auth.urls' HTML template overwrites follow the "_" naming convention.

## Authors

* **Ilbum Kwak** - [ilbum](https://github.com/ilbum)

## License

MIT License\
To be completed ...
