To run demo:

- `git clone https://github.com/Gingertonic/temp-morris-django.git yummy-django`
- `cd yummy-django/`
- `pipenv shell`
- `pipenv install`
- `cd yummytown`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`

To access admin console:
- `python manage.py createsuperuser`
- login at `http://127.0.0.1:8000/admin`