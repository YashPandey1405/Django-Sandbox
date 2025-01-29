# Django-Basics

This is a simple Django project to get started with web development using Django. Django simplifies the web development process, allowing developers to focus on building their applications rather than reinventing the wheel. Django’s robust ecosystem, combined with its emphasis on reusability and rapid development, makes it a popular choice for developers worldwide.

---

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
