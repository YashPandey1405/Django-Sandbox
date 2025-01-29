# Django-Basics

This is a simple Django project to get started with web development using Django. Django simplifies the web development process, allowing developers to focus on building their applications rather than reinventing the wheel. Django’s robust ecosystem, combined with its emphasis on reusability and rapid development, makes it a popular choice for developers worldwide.

## Uses Of Django

Django is widely used for developing robust and scalable web applications. It Django is used for building secure, scalable web applications quickly. It provides built-in features like an admin panel, ORM, authentication, and URL routing, which streamline development. Ideal for data-driven websites, content management systems, and APIs, Django emphasizes security and rapid development, making it suitable for projects of all sizes.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps to Install

1. Clone the repository or download the project files.
2. Navigate to the project directory in your terminal.
3. Create a virtual environment:

   ```bash
   pip install virtualenv
   python -m virtualenv --version
   python -m virtualenv env
   ```

4. Activate the virtual environment On Windows:

   ```bash
   .\env\Scripts\activate
   ```

5. Install the required dependencies:

   ```bash
   pip install Django
   ```

## Setup

1. To start a new Django project, run (Only 1st Time):

   ```bash
   django-admin startproject <File-Name>
   ```

2. Navigate into the project directory:

   ```bash
   cd <File-Name>
   ```

3. To start the Django development server, run:

   ```bash
   python manage.py runserver
   ```

4. Open a browser and go to `http://127.0.0.1:8000/` to view the Django welcome page.

## Usage

- After setting up the project, you can start building Django applications.
- You can create new Django apps using:

  ```bash
  python manage.py startapp <app_name>
  ```

- To apply migrations and create the database schema, run:

  ```bash
  python manage.py migrate
  ```
