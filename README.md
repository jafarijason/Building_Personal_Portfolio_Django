# Portfolio Web Page By Django

I want to make a simple port folio project with Django 

Becuse of that  I need to install python 3 

we need to  make  virtualenv for this project so 

```
virtualenv .env
```

after installation we shoud ued the virtual enviroment

```
./env/Script/activate
```

and after that we shoud install django by pip

```
pip install django
```

after that we should use 

```
django-admin.exe startproject portfolio-project

```

after this section  you shoud go to the  folder project

```
cd portfolio-project
```


after if we want to start djago project we shoude use this command

```
python manage.py runserver
```
by ctrl + c 
 you can exit from project
------------------------------------------------------------------------------------------------------------


Now we need make one app for django 

```

django-admin.exe startapp jobs

```



after that we shoud open setting file and impeliment app in the :

```

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jobs'
]

```


------------------

after that we should define url to django 


```
from django.contrib import admin
from django.urls import path
import jobs.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jason/', jobs.views.jason,name='jason'),
]



```



after we should change the jobs/views.py and make jason function


some changes that you can finde in commite for view pages



-----------------------------------------------------------




at this section we want to work database

so we should  use the models

in the root of project open the models.py


```
class Job(models.Model):
    #Images
    image = models.ImageField(upload_to='images/')
    #summary 
    summary = models.CharField(max_length=200)
    
    
```

for working by images we should intall pillo


```
pip install pillow

```

django can work with a lot of databases 

but we want to install Postgrees

to want know more aboute Postgree data base you can go to this link





* [Postgresql](https://www.postgresql.org/docs/6.3/c0101.htm) - Toutorial


by at the moment i decide to use sqliteite



and try to makemigration

```
 python manage.py makemigrations
```

```
 python manage.py migrate
```


ok it is grate

by going to  /admin sectiom you will relize django have admin page

for making user for django admin you should type this command 

```
python manage.py createsuperuser
```








 