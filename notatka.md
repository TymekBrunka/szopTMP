# Notatka

1. .venv
2. django setup
   ![mvc](./mvc.png)
   **Utworzenie projektu:**
   
   1. `django-admin startproject ecommerce`
   
   **Uruchomienie serwera:**
   
   1. `cd ecomerce`
   2. `python manage.py runserver`
   3. `python manage.py startapp store`

3. dodajemy w settings.py w INSTALLED_APPS **'store.apps.StoreConfig',**
4. python ./ecommerce/manage.py createsuperuser
5. python ./ecommerce/manage.py makemigrations i python ./ecommerce/manage.py migrate
