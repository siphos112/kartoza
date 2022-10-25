Django Point Geometry project:
==============================
A project implemented with the Django framework uses multiple Google APIs 
to register users, create profiles and locate them on a map.

1. cd to your development directory
2. Create kartoza directory: mkdir kartoza
3. cd to kartoza and create virtual environment: python -m venv ./venv
4. Create another directory Kartoza: mkdir kartoza
5. Clone repository to this directory[in step 4]
6. run: pip install -r requirements.txt
7. The settings.py file requires the following Google API keys for the app to work:
    GOOGLE_API_KEY = ""
    RECAPTCHA_PUBLIC_KEY = ""
    RECAPTCHA_PRIVATE_KEY = ""
        
8. run: python manage.py makemigrations
9. python manage.py migrate
10. python manage.py runserver
11. Make sure to always use 'localhost:<port>' eg: localhost:8000, so 
    that the API keys would work. '127.0.0.1:<port>' will not work for the 
    APIs unless you register 127.0.0.1 when you create the APIs.
    So, 'localhost:<port>' and enjoy!
