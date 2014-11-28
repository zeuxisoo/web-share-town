# Installation

Install the dependency

    virtualenv --no-site-package venv
    source venv/bin/activate
    pip install -r requirements.txt

Run the application

    python manager.py runserver

OR

    make server

Open in browser

    http://localhost:5000/

Gunicorn

    # http://localhost:8000/
    gunicorn wsgi:app
