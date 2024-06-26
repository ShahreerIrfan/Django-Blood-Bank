import subprocess

# List of global packages to install
global_packages = [
    'asgiref==3.7.2',
    'black==23.12.1',
    'certifi==2024.2.2',
    'cffi==1.16.0',
    'charset-normalizer==3.3.2',
    'click==8.1.7',
    'colorama==0.4.6',
    'crispy-bootstrap5==2023.10',
    'cryptography==42.0.5',
    'defusedxml==0.7.1',
    'dj-database-url==2.1.0',
    'Django==5.0.1',
    'django-allauth==0.61.1',
    'django-bootstrap5==23.4',
    'django-cors-headers==4.3.1',
    'django-crispy-forms==2.1',
    'django-environ==0.11.2',
    'django-filter==23.5',
    'django-tailwind==3.8.0',
    'django-widget-tweaks==1.5.0',
    'djangorestframework==3.14.0',
    'djangorestframework-jwt==1.11.0',
    'djangorestframework-simplejwt==5.3.1',
    'httpie==3.2.2',
    'idna==3.6',
    'Markdown==3.5.2',
    'markdown-it-py==3.0.0',
    'mdurl==0.1.2',
    'multidict==6.0.5',
    'mypy-extensions==1.0.0',
    'oauthlib==3.2.2',
    'packaging==23.2',
    'pathspec==0.12.1',
    'pillow==10.2.0',
    'platformdirs==4.1.0',
    'psycopg2==2.9.9',
    'psycopg2-binary==2.9.9',
    'pycparser==2.22',
    'Pygments==2.17.2',
    'PyJWT==1.7.1',
    'PySocks==1.7.1',
    'python-dotenv==1.0.1',
    'python3-openid==3.2.0',
    'PythonTurtle==0.3.2',
    'pytz==2023.3.post1',
    'requests==2.31.0',
    'requests-oauthlib==2.0.0',
    'requests-toolbelt==1.0.0',
    'rich==13.7.0',
    'sqlparse==0.4.4',
    'typing_extensions==4.10.0',
    'tzdata==2023.4',
    'urllib3==2.2.0'
]

# Install each global package into the virtual environment
for package in global_packages:
    subprocess.run(['pip', 'install', package])