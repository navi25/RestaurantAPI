RestaurantAPI
=============

Online Restaurant API system using flask, flask-restful, sqlalchemy,
marshmallow

The project has been developed using Flask- A python Micro-web framework
and other additional packages describe below in Tech Stack Section.

Github link for the project - <https://github.com/navi25/RestaurantAPI>

Also checkout <https://github.com/navi25/GoColumbus> for the implementation of same project using Go Language.

Installation
------------

Before we begin, kindly install following on your system:-

-   [python3.x](http://www.python.org)
-   [Virtualenv](https://virtualenv.pypa.io/en/stable/)

How to Run the App?
-------------------

-   cd path/to/workspace
-   git clone <https://github.com/navi25/RestaurantAPI>
-   cd RestaurantAPI
-   virtualenv -p ‘which python3’ venv
-   source venv/bin/activate
-   pip install -r requirements.txt
-   python3 run.py

Everything should be ready. In your browser open
<http://127.0.0.1:5000/>

Since Redis-Server is used for database optimisation
After running the app, type in following in terminal to establish
redis-connection

- redis-server

REST Endpoints
--------------

There are three major objects in the app:-

-   Restaurants
-   Menu
-   Food Items (Menu Items)

The endpoints and the corresponding REST operations are defined as
follows:-

-   **RESTAURANTS**
    -   <http://127.0.0.1:5000/api/v1.0/restaurants/>
        -   **GET** : This method on above URL returns all the
            restaurants available in the database in json format
        -   **POST** : This method posts a new restaurant and accept
            *application/JSON* format for the operation with "name" as
            the only and the required parameter for the JSON.
        -   **PUT** : Same as POST with additional feature of updating
            the restaurant object too.
        -   **Delete** : This method deletes the given restaurant if the
            *restaurant\_id* exists.
-   **Menu**
    -   <http://127.0.0.1:5000/api/v1.0/menus/>
        -   **GET** : This method on above URL returns all the menu
            available in the database in json format
        -   **POST** : This method posts a new menu and accept
            *application/JSON* format for the operation with "name" and
            "restaurant\_id" as the required parameter for the JSON.
        -   **PUT** : Same as POST with additional feature of updating
            the menu object too.
        -   **Delete** : This method deletes the given menu if the
            *menu\_id* exists.
-   **Food**
    -   <http://127.0.0.1:5000/api/v1.0/foods/>
        -   **GET** : This method on above URL returns all the foods
            available in the database in json format
        -   **POST** : This method posts a new food and accept
            *application/JSON* format for the operation with "name" and
            "restaurant\_id" as the required parameter for the JSON.
        -   **PUT** : Same as POST with additional feature of updating
            the menu object too.
        -   **Delete** : This method deletes the given menu if the
            *food\_id* exists.

Unit Testing Endpoints
----------------------

The Tests for all the modules are located in **tests** directory and can be fired
in two ways:-
- Individually by running their individual test modules
- All at once by running TestAll module which look for all the available modules
in the directory and fires the test cases one by one.

The [Flask's Unittest modules](http://flask.pocoo.org/docs/0.12/testing/) were used for developing the testcases.

Additional endpoints
--------------------

 -   [http://127.0.0.1:5000/api/v1.0/restaurants/{id}](http://127.0.0.1:5000/api/v1.0/restaurants/{id})

     Returns the particular restaurant with id = id if it exists

 -   [http://127.0.0.1:5000/api/v1.0/restaurants/{id}/foods](http://127.0.0.1:5000/api/v1.0/restaurants/{id}/foods)

     Returns all the foods available in the particular restaurant with
     id = id, if the restaurant it exists

 -   [http://127.0.0.1:5000/api/v1.0/restaurants/{id}/foods/{food\_id}](http://127.0.0.1:5000/api/v1.0/restaurants/{id}/foods/{food_id})

     Returns the particular food with id = food\_id in the particular
     restaurant with id = id if it exists.

 -   [http://127.0.0.1:5000/api/v1.0/restaurants/{id}/menus](http://127.0.0.1:5000/api/v1.0/restaurants/{id}/menus)

     Returns all the menus available in the particular restaurant with
     id = id, if the restaurant it exists

 -   [http://127.0.0.1:5000/api/v1.0/restaurants/{id}/menus/{menu\_id}](http://127.0.0.1:5000/api/v1.0/restaurants/{id}/menus/{menu_id})

     Returns the particular menu with id = menu\_id in the particular
     restaurant with id = id if it exists.

Tech stack
----------

-   [Flask](http://flask.pocoo.org/) - Web Microframework for Python
-   [Flask-restful](https://flask-restful.readthedocs.io/en/latest/) -
    Extension for flask for quickly building REST APIs
-   [Swagger](https://swagger.io/) - Automatic Documentation for the
    REST endpoints
-   [Flask-migrate](https://flask-migrate.readthedocs.io/en/latest/) -
    An extension that handles SQLAlchemy database migrations for Flask
    applications using Alembic.
-   [Marshmallow](https://marshmallow.readthedocs.io) - A serializer and
    deserializer framework for converting complex data types, such as
    objects to and from native Python data types.
-   [Flask-sqlalchemy](http://flask-sqlalchemy.pocoo.org/) - This is an
    extension of flask that add supports for SQLAlchemy
-   [Flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) - An integration layer for flask and marshmallow.
-   [Marshmallow-sqlalchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/) - This adds additional features to marshmallow.
-   [Sqlite3](https://www.sqlite.org/index.html) - Database for the
    project. It comes built in with python.
-   [RedisDB](https://redis.io/) - Key-Value based No-SQL DB to optimize relational
database by improving Read by caching data efficiently.
-   [Flask-Redis](https://github.com/underyx/flask-redis) - An flask extension of [RedisPy](http://redis-py.readthedocs.io/en/latest/)
    to use Redis with Python and Flask easily.

Development Thought process
---------------------------

-   Used Micro service Architecture for proper decoupling of service.
-   Documentation is hard, hence used an automatic document generating
    tool – Swagger to ease out the process.
-   Test driven development is useful and leads to less errors in later
    stages of development.
-   Dependency injection helps a lot in Test driven development and also
    in making the project more modular and flexible. Though couldn’t use
    in the current project but would surely update the project using
    flask-injector.
-   RedisDB is used as caching layer to improve read efficiency.
-   Used Flask because it’s flexible and can be plugged with all the
    necessary modules on the go.


