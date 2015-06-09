Personal Webpage:
=================
Recently I have started learning Django. After finishing the awesome Django tutorial, I tried to build an app for myself. This repo contains code of my personal website.

Technology:
-----------
```
Back-end - Python 2.7  
Web Framework - Django 1.7  
Database - sqlite3  
Front-end - HTML/CSS/JavaScript  
Front-end tool - Bootstrap  
Operating System - Ubuntu 14.04  
```

Installation:
-------------
Clone the repo  

```
$ git clone git@github.com:pattu777/MySite.git
```

Change directory  

```
$ cd MySite/
```

Create and activate virtualenv(Strongly Recommended)  

```
$ virtualenv venv
$ source venv/bin/activate
```

Install the packages  

```
$ pip install -r requirements.txt
```

Run the Django server  

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver
```


Django Apps:
------------
1. Home  
2. Blog  

As I am learning Django, I thought spending too much time on front-end would be an overkill. So I have used some custom open source templates from StartBootstrap.

Home template - Grayscale Portfolio theme(http://startbootstrap.com/template-overviews/grayscale/).  
Blog template - Clean blog(http://startbootstrap.com/template-overviews/clean-blog/).  

TODO:
-----
1. ~~Host it on App engine or Heroku(Check out DigitalOcean too).~~
2. ~~Switch database to Postgresql or Mysql.~~
3. Add tests.
4. ~~Add resume.~~
5. ~~Build Contacts Page.~~
6. ~~Remove all non sense and Add personal content.~~
7. ~~Change Django admin password.~~
8. Use flake8 or Pylint for code check.
9. Add coverage.  
10. ~~Add a WSYWYG editor to Django admin interface.~~
