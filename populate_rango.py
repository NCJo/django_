# Make sure this file locate in the correct folder or it will throw import error

import os
# Very important or errors throw when try to import models
os.environ['DJANGO_SETTINGS_MODULE'] = 'tango_withdjango_project.settings'

import django
django.setup()
from rango.models import Category, Page

def populate():
    # First we create lists of dictionaries containing the pages we want to add into each category
    # Then we will create a dictionary of dictionaries for our categories
    # It allows us to iterate through each data structure and add the data to our models

    # Add categories and pages here

    python_pages = [
        {"title": "Official Python Tutorial", "url": "http://doc.python.org/2/tutorial/"},
        {"title":"How to think like a computer scientist", "url":"http://www.greenteapress.com/thinkpython/"},
        {"title":"Learn Python in 10 Minutes", "url":"http://www.korokithakis.net/tutorials/python/"}
    ]

    django_pages = [
        {"title":"Official Django Tutorial", "url":"http://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title":"Django Rocks", "url":"http://www.djangorocks.com/"},
        {"title":"How to tango with django", "url":"http://tangowithdjango.com"}
    ]

    other_pages = [
        {"title":"Bottle", "url":"http://bottlepy.org/docs/dev/"},
        {"title":"Flask", "url":"http://flask.pocoo.org"},
    ]

    cats = {
        "Python": {"pages": python_pages, "views": 128, "likes": 64},
        "Django": {"pages": django_pages, "views": 64, "likes": 32},
        "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}
    }

    # Go through cats dictionary -> add each category  -> add all the associated pages for that category
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])
    
    # Print out category added
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c

# Start execution here
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()