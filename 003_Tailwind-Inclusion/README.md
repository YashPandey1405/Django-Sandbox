# Django Tailwind Setup

This guide helps you set up Tailwind CSS in a Django project using `django-tailwind`.

## Steps to Install and Set Up Tailwind-CSS in Django

### 1. Install Django-Tailwind
Run the following commands to install the `django-tailwind` package:

```bash
pip install django-tailwind
pip install 'django-tailwind[reload]'
```

### 2. Initialize Tailwind in Django Project
Once the installation is complete, run the following command to initialize Tailwind in your project:

```bash
python manage.py tailwind init
```

**Note:** You might need to set the `NPM_BIN_PATH` environment variable to the location of your npm. For example:

```bash
set NPM_BIN_PATH=r"C:\Program Files\nodejs\npm.cmd"
```

### 3. Install Tailwind Dependencies
To install the necessary Tailwind CSS dependencies, run the following command:

```bash
python manage.py tailwind install
```

This will install Tailwind CSS and other required dependencies.

### 4. Configuration (Optional)
Make sure to follow any additional configuration instructions specific to your project setup (e.g., adding `tailwind` to `INSTALLED_APPS`).

### 5. Running the Development Server
Run the development server to see Tailwind in action:

```bash
python manage.py runserver
```

Now you can start building your Django application with Tailwind CSS.

## Troubleshooting

- If you encounter any issues with Node.js or npm installation, ensure that they are correctly installed and the environment variable `NPM_BIN_PATH` is set properly.
- For any `django-tailwind` specific issues, refer to the official documentation.

---

