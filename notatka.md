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
4. `python ./ecommerce/manage.py createsuperuser`
5. `python ./ecommerce/manage.py makemigrations` i `python ./ecommerce/manage.py migrate`
6. `python ./ecommerce/manage.py runserver admin`
   i odpalamy przeglądarkę w localhost:port/admin
7. `./ecommerce/store` dodajemy folder `templates` i w tym folderze dodajemy folder `store`
   dodajemy pliki html (main, cart, checkout, store)
   do widoku
8. do pliku `./ecommerce/store/views.py` dodajemy
   ```python
   def store(req):
    context = {}
    return render(req, 'store/store.html', context)

   def cart(req):
      context = {}
      return render(req, 'store/cart.html', context)

   def checkout(req):
      context = {}
      return render(req, 'store/checkout.html', context)
   ```
   dodajemy plik `./ecomerce/store/urls.py` z zawartością:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
      path('', views.store, name="store"),
      path('cart/', views.cart, name="cart"),
      path('checkout/', views.checkout, name="checkout"),
   ]
   ```
   do pliku `./ecommerce/urls.py` dodajemy
   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('store.urls')),
   ]
   ```
9. Dodajemy folder `static` w `./ecommerce/` i w nim tworzymy foldery `css` i `images` i tworzymy w `css` `main.css`
   do `./ecommerce/settings.py` dodajemy na górze
   ```python
   import os
   ```
   oraz na dole
   ```python
   STATICFILES_DIRS = [
      os.path.join(BASE_DIR, 'static'),
   ]
   ```

   i do pliku `main.html` dodajemy
   ```html
   {% load static %}
   <!DOCTYPE html>
   <html>
      <head>
         <meta charset="utf-8">
         <title>Store</title>
         <meta name="description" content="">
         <meta name="viewport" content="width=device-width, initial-scale=1">
         <link rel="stylesheet" href="">
         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
         <link rel="stylesheet" type="text/css" href="{% static 'css/main.css' %}">
      </head>
      <body>
         <h1>Menu</h1><br>
         <div class="container">
               {% block content %}

               {% endblock content %}
         </div>
         <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
      </body>
   </html>
   ```

   i do reszty plików html dodajemy
   ```html
   {% extends 'store/main.html' %}
   {% load static %}
   {% block content %}
      <h1>TYTUŁ</h1>
   {% endblock content %}
   ```
10. zamieniamy `<h1>menu</h1>` na przykład z bootstrapa i zamieniamy `...tetriary` na `navbar-dark bg-dark`
    usuwamy
    ```html
    <form class="d-flex" role="search">
                  <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                  <button class="btn btn-outline-success" type="submit">Search</button>
               </form>
    ```
    ```html
   <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Dropdown
                  </a>
                  <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="#">Action</a></li>
                      <li><a class="dropdown-item" href="#">Another action</a></li>
                      <li><hr class="dropdown-divider"></li>
                      <li><a class="dropdown-item" href="#">Something else here</a></li>
                    </ul>
                  </li>
    ```
    i linki
    ```html
   <li class="nav-item">
                     <a class="nav-link" href="#">Link</a>
                  </li>
    ```
    ```html
    <li class="nav-item">
                     <a class="nav-link disabled" aria-disabled="true">Disabled</a>
                  </li>
    ```
11. zamieniamy
   ```html
   <a class="navbar-brand" href="#">Navbar</a>
   ```
   na
   ```html
   <a class="navbar-brand" href="{% url 'store' %}">Store TPM3</a>
   ```

   oraz
    
   ```html
   <a class="nav-link active" aria-current="page" href="#">Home</a>
   ```
   na
   ```html
   <a class="nav-link active" aria-current="page" href="{% url 'cart' %}">Cart</a>
   ```
12. Ściągamy `main.css` z `http://losto.net/images/main.css` i podmieniamy go.

   Ściągamy też `https://losto.net/images/cart.png`.

13. Po
   ```html
   <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="{% url 'cart' %}">Cart</a>
                  </li>
                </ul>
   ```
   dodajemy
   ```html
   <div class="form-inline my-2 my-lg-0">
                    <a href="#" class="btn btn-warning">Login</a>

                    <a href="{% url 'cart' %}">
                        <img id="cart-icon" src="{% static 'images/cart.png' %}">
                    </a>

                    <p id="cart-total"> 0 </p>
                </div>
   ```
   a w `main.css` zamiemy `display` w `#cart-total` na `inline-block`.

   Pobieramy obrazek z `https://www.losto.net/images/placeholder.png`
12. W `store.html` zamieniamy `<h1>STORE</h1>` na
   ```html
    <div class="row">
        <div class="col-lg-4">
            <div class="box-element product">
                <img class="thumbnail" src="{% static 'images/placeholder.png' %}">
            </div>
        </div>
        <div class="col-lg-4">
            <div class="box-element product">
                <img class="thumbnail" src="{% static 'images/placeholder.png' %}">
            </div>
        </div>
        <div class="col-lg-4">
            <div class="box-element product">
                <img class="thumbnail" src="{% static 'images/placeholder.png' %}">
            </div>
        </div>
    </div>
   ```
13. ściągamy `https://www.losto.net/images/arrow-down.png` i `https://www.losto.net/images/arrow-up.png`
   ze strony człuchowskiej strony.
14. w `cart.html` zamieniamy `<h1>CART</h1>` na
   ```html
   <div class="row">
        <div class="col=lg-12">
            <div class="box-element">
                <a class="btn btn-outline-dark" href="{% url 'store' %}">Continue shopping</a>
                <br>
                <table class="table">
                    <tr>
                        <th><h5>Items: <strong>4</strong></h5></th>
                        <th><h5>Total: <strong>200.00</strong></h5></th>
                        <th>
                            <a class="btn btn-success" href="{% url 'checkout' %}" style="float:right; margin: 5px;">checkout</a>
                        </th>
                    </tr>
                </table>
            </div>
            <br>
            <div class="box-element">
                <div class="cart-row">
                    <div style="flex:2;">
                        <strong>
                            <img width="200px" src="{% static 'images/placeholder.png' %}">
                        </strong>
                    </div>
                    <div style="flex:2;">
                        <strong>Produkt 1</strong>
                    </div>
                    <div style="flex:1;">
                        <strong>100.00 PLN</strong>
                    </div>
                    <div style="flex:1;">
                        <p class="quantity">2</p>
                        <div class="quantity">
                            <img class="chg-quantity" src="{% static 'images/arrow-up.png' %}">
                            <img class="chg-quantity" src="{% static 'images/arrow-down.png' %}">
                        </div>
                    </div>
                    <div style="flex:1;">
                        <strong>200.00 PLN</strong>
                    </div>
                </div>
                <div class="cart-row">
                    <div style="flex:2;">
                        <strong>
                            <img width="200px" src="{% static 'images/placeholder.png' %}">
                        </strong>
                    </div>
                    <div style="flex:2;">
                        <strong>Item</strong>
                    </div>
                    <div style="flex:1;">
                        <strong>Price</strong>
                    </div>
                    <div style="flex:1;">
                        <strong>Quantity</strong>
                    </div>
                    <div style="flex:1;">
                        <strong>Total</strong>
                    </div>
                </div>
            </div>
        </div>
    </div>
   ```
15. w `checkout.html` zamieniamy `<h1>CHECKOUT</h1>` na
    ```html
    <div class="row">
        <div class="col-lg-6">
            <div class="box-element">
                <form id="form">
                    <div class="user-info">
                        <div class="form-field">
                            <input required class="form-control" type="text" name="name" placeholder="Name...">
                        </div>
                        <div class="form-field">
                            <input required class="form-control" type="email" name="email" placeholder="Email...">
                        </div>
                    </div>
                    <div class="shipping-info">
                        <hr>
                            <p>Shipping info</p>
                        </hr>
                        <div class="form-field">
                            <input required class="form-control" type="address" name="email" placeholder="Address...">
                        </div>
                        <div class="form-field">
                            <input required class="form-control" type="city" name="email" placeholder="City...">
                        </div>
                        <div class="form-field">
                            <input required class="form-control" type="state" name="email" placeholder="State...">
                        </div>
                        <div class="form-field">
                            <input required class="form-control" type="zipcode" name="email" placeholder="Zip code...">
                        </div>
                        <div class="form-field">
                            <input required class="form-control" type="country" name="email" placeholder="Country...">
                        </div>
                    </div>

                    <hr>
                    <input id="form-button" class="btn btn-success btn-block" type="submit" value="Continue">
                </form>

                <hr>
                <div class="box-element hidden" id="payment-info">
                    <small>PayPal Options</small>
                </div>
            </div>
        </div>

        <div class="col-lg-6">
            <div class="box-element">
                <a class="btn btn-outline-dark" href="{% url 'cart' %}">Back to cart</a>
                <hr>
                <h3>Order summary</h3>
                <hr>
                <div class="cart-row">
                    <div style="flex: 2">
                        <img class="row-image" src="{% static 'images/placeholder.png' %}">
                    </div>
                    <div style="flex: 2">
                        Product 1
                    </div>
                    <div style="flex: 2">
                        20.00 PLN
                    </div>
                    <div style="flex: 2">
                        x2
                    </div>
                </div>
                <h5>Items: 2</h5>
                <h5>Total: 40.00 PLN</h5>
            </div>
        </div>
    </div>
    ```
16. # DODAWANIE MODELU
    do `ecomerce/store/models.py` dodajemy
    ```python
    class Customer(models.Model):
        user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
        name = models.CharField(max_length=200, null=True)
        email = models.CharField(max_length=200)

        
        def __str__(self):
            return self.name + ' ' + self.email
    
    class Product(models.Model):
        name = models.CharField(max_length=200)
        price = models.FloatField()
        digital = models.BooleanField(default=False, null=True, blank=True)

        def __str__(self):
            return self.name + " " + self.digital
    
    class Order(models.Model):
        customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
        date_ordered = models.DateTimeField(auto_now_add=True)
        complete = models.BooleanField(default=False)
        transaction_id = models.CharField(max_length=100, null=True)

        def __str__():
            return str(self.id)

    class OrderItem(models.Model):
        product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
        order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
        quantity = models.IntegerField(default = 0, null=True, blank=True)
        date_added = models.DateTimeField(auto_now_add=True)
    
    class ShippingAddress(models.Model):
        customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
        order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
        address = models.CharField(max_length=200, null=True)
        city = models.CharField(max_length=200, null=True)
        state = models.CharField(max_length=200, null=True)
        zipcode = models.CharField(max_length=200, null=True)
        country = models.CharField(max_length=200, null=True)
        date_added = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.address + " " + self.city
    ```
    
    do `ecomerce/store/admin` dodajemy
    ```python
    from .models import *

    admin.site.register(Customer)
    admin.site.register(Product)
    admin.site.register(Order)
    admin.site.register(OrderItem)
    admin.site.register(ShippingAddress)
    ```

    uruchamiamy `python ecommerce\manage.py makemigrations` i `python ecommerce\manage.py migrate`
17. # Dodawanie bazy
    po dodaniu postgres z hasłem postgres z domyślnymi ustawieniami
    ![zdj](./zdjęcia/Zrzut%20ekranu%20(1).png)
    ![zdj](./zdjęcia/Zrzut%20ekranu%20(2).png)
    ![zdj](./zdjęcia/Zrzut%20ekranu%20(3).png)
    ![zdj](./zdjęcia/Zrzut%20ekranu%20(4).png)
    ![zdj](./zdjęcia/Zrzut%20ekranu%20(5).png)
    ![zdj](./zdjęcia/Zrzut%20ekranu%20(6).png)
    ![zdj](./zdjęcia/Zrzut%20ekranu%20(7).png)
    ![zdj](./zdjęcia/Zrzut%20ekranu%20(8).png)

18. # Zmiana bazy w ustawieniach
    usuwamy `ecommerce/db.sqlite3`

    i zamieniamy w `ecommerce/ecommerce/settings.py`
    ```python
    DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```
    na
    ```python
    DATABASES = {
        'default': {
            'ENGINE'   : 'django.db.backends.postgresql_psycopg2',
            'NAME'     : "shop3",
            "USER"     : "postgres",
            "PASSWORD" : "postgres",
            "HOST"     : "localhost",
            "PORT"     : "5432"
        }
    }
    ```
    i uruchamiamy `python ecommerce/manage.py migrate` po makemigrations
    i odświerzamy dbeavera
    ![zdj](./zdjęcia/Zrzut%20ekranu%20(11).png)
    uruchamiamy `cd ecommerce` i `python manage.py createsuperuser`
    ![zdj](./zdjęcia/Zrzut%20ekranu%20(12).png)
    i ...
    ![zdj](./zdjęcia/Zrzut%20ekranu%20(13).png)
    ![zdj](./zdjęcia/Zrzut%20ekranu%20(14).png)
19. # Wstawianie prawdziwych danych na stronkach / Dynamiczne dane
    naprawiamy `ecommerce/models.py` i zamieniamy w klasie Product ... na 
    ```python
    def __str__(self):
        return ( "(d) " if self.digital else "") + self.name
    ```

    i w `ecommerce/store/views.py` dodajemy na górze
    ```python
    from .models import *
    ```

    i aktualizujemy widoki
    ```python
    def store(req):
        products = Product.objects.all()
        context = {'products' : products}
        return render(req, 'store/store.html', context)

    def cart(req):
        context = {}
        return render(req, 'store/cart.html', context)

    def checkout(req):
        context = {}
        return render(req, 'store/checkout.html', context)
    ```

    `store.html`
    ```html
    {% extends 'store/main.html' %}
    {% load static %}
    {% block content %}
        <div class="row">
            {% for product in products %}
            <div class="col-lg-4">
                <div class="box-element product">
                    <img class="thumbnail" src="{% static 'images/placeholder.png' %}">
                    <h6><strong> {{ product.name }} </strong></h6>
                    <p style="display: inline-block;"> {{ product.price }} </p>
                </div>
            </div>
            {% endfor %}
        </div>
    {% endblock content %}
    ```
    ![zdj](./zdjęcia/Zrzut%20ekranu%20(15).png)

20. #Dodawanie ststic img
    Dodajemy do `models.py` w Product
    ```python
    image = models.ImageField(null=True, blank=True)
    ```
    i pobieramy pillow
    
    Dodajemy w `settings.py`
    ```python
    MEDIA_URL = '/images/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
    ```

    W  `./ecommerce/urls.py` zamieniamy na
    ```python
    from django.contrib import admin
    from django.urls import path, include
    from django.conf.urls.static import static
    from django.conf import settings

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('store.urls')),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    ```

    do `models.py` dodajemy funkcję
    ```python
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    ```

    `store.html` = 
    ```html
    {% extends 'store/main.html' %}
    {% load static %}
    {% block content %}
        <div class="row">
            {% for product in products %}
            <div class="col-lg-4">
                <div class="box-element product">
                    <img class="thumbnail" src="{{ product.imageURL }}">
                    <h6><strong> {{ product.name }} </strong></h6>
                    <p style="display: inline-block;"> {{ product.price | floatformat:2 }} PLN</p>
                </div>
            </div>
            {% endfor %}
        </div>
    {% endblock content %}
    ```
21. #dodajemy zakup
    dodajemy customera
    dodajemy order
    dodajemy orderitem
    dodajemy 

23. podmieniamy views
    ```python
    def cart(req):
        if req.user.is_authenticated:
            customer = req.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items = {}
        context = {'items' : items, 'order' : order}
        return render(req, 'store/cart.html', context)
    ```

    i do `main.html` dodajemy
    ```html
        <script>
          var user = '{{ request.user }}'
        </script>
    ```

    oraz zamieniamy `cart.html` na 
    ```html
    {% extends 'store/main.html' %}
    {% load static %}
    {% block content %}
        <div class="row">
            <div class="col=lg-12">
                <div class="box-element">
                    <a class="btn btn-outline-dark" href="{% url 'store' %}">Continue shopping</a>
                    <br>
                    <table class="table">
                        <tr>
                            <th><h5>Items: <strong>{{ order.get_cart_items }}</strong></h5></th>
                            <th><h5>Total: <strong>{{ order.get_cart_total | floatformat:2 }} PLN</strong></h5></th>
                            <th>
                                <a class="btn btn-success" href="{% url 'checkout' %}" style="float:right; margin: 5px;">checkout</a>
                            </th>
                        </tr>
                    </table>
                </div>
                <br>
                <div class="box-element">
                    {% for item in items %}
                    <div class="cart-row">
                        <div style="flex:2;">
                            <strong>
                                <img width="200px" src="{{ item.product.imageURL }}">
                            </strong>
                        </div>
                        <div style="flex:2;">
                            <strong>{{ item.product.name }}</strong>
                        </div>
                        <div style="flex:1;">
                            <strong>{{ item.product.price | floatformat:2}} PLN</strong>
                        </div>
                        <div style="flex:1;">
                            <p class="quantity">{{ item.quantity }}</p>
                            <div class="quantity">
                                <img class="chg-quantity" src="{% static 'images/arrow-up.png' %}">
                                <img class="chg-quantity" src="{% static 'images/arrow-down.png' %}">
                            </div>
                        </div>
                        <div style="flex:1;">
                            <strong>{{ item.get_total | floatformat:2 }}</strong>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    {% endblock content %}
    ```
    
    i w models.py w Order dodajemy funkcje
    ```python
    @property
    def get_cart_total(self):
        orderitems = self.orderitems_set.all()
        total = sum([ item.get_total for item in orderitems ])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitems_set.all()
        total = sum([item.quantity for item in orderitems])
    ```

    i w OrderItems:
    ```python
    @property
    def get_total(self):
        return self.product.price * self.quantity
    ```