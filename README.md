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
7. The API keys will be there until the assessment has been done, then removed
    so in the near future they will not be there, so you will need to get 
    the necessary api keys from google:
        google_api_key, and recaptcha keys [see settings.py file]

8. run: python manage.py makemigrations
9. python manage.py migrate
10. python manage.py runserver
11. Make sure to always use 'localhost:<port>' eg: localhost:8000, so 
    that the API keys would work. '127.0.0.1:<port>' will not work for the 
    APIs.
    So, 'localhost:<port>' and enjoy!
