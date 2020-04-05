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
import jobs.views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jason/', jobs.views.jason),
]



```









a