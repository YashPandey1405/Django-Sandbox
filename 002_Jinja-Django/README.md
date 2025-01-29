
# Jinja in Django - Learning App

## What is Jinja?

Jinja is a templating engine for Python, used to create dynamic HTML pages. It allows you to embed Python-like expressions inside HTML files. With Jinja, you can create reusable templates, define blocks for content insertion, and extend layouts to maintain consistent structure across different pages.

## Using Jinja in Django

In Django, Jinja is used to create a base layout for your HTML files, which can be extended by other templates. This helps in maintaining a consistent design and structure across the application.

### Example:

```html
{% extends "layout.html" %}
{% block title %}Home Page{% endblock %}
{% block content %}
<h1>Welcome To HomePage Of Learning-Jinja App</h1>
{% endblock %}
```

The above template extends the `layout.html` file and defines blocks for `title` and `content`. Other templates can inherit from this base and override these blocks with specific content.

## Create a Django App

To create a Django app, run the following command:

```bash
python manage.py startapp <AppName>
```

This command creates a new app directory with the necessary files to get started with your Django project.
