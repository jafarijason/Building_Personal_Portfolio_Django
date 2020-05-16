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
-----------------------------------



at this time we want to start by admin.py 


```
from django.contrib import admin
from .models import Job


# Register your models here.

admin.site.register(Job)
```


----------------------------------------


crating model object via admin panel
django



------





# How-to-bind-multiple-domains-ports-80-and-443-to-docker-contained-applications

I Re post  [this](https://www.digitalocean.com/community/questions/how-to-bind-multiple-domains-ports-80-and-443-to-docker-contained-applications) document for my personal usage.

The most basic way to expose a web app running a docker container to the outside is to bind port 80 in the container to port 80 on the host system 

```
docker run  -d  --name appacheapp1  -p 80:80 coreos/apache /usr/sbin/apache2ctl -D FOREGROUND 

```



Though when you are running multiple app that you can’t have them all listen on the same port. One way to get around this would be to set up an Nginx reverse proxy in front of the containers.

For example, say you have two different app. Bind them to a random port on the local host:


```
docker run -d  --name appacheapp1 -p 127.0.0.1:3000:80 coreos/apache /usr/sbin/apache2ctl -D FOREGROUND
docker run -d  --name appacheapp1 -p 127.0.0.1:5000:80 coreos/apache /usr/sbin/apache2ctl -D FOREGROUND

```


Then you can configure an Nginx sconfiguration that looks something like this:

```
upstream app-a {
    server 127.0.0.1:3000;
}

upstream app-b {
    server 127.0.0.1:5000;
}

server {
        listen 80;
        server_name test.com www.test.com;

        location / {
            proxy_pass         http://app-a;
            proxy_redirect     off;
            proxy_set_header   Host $host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Host $server_name;

        }
}

server {
        listen 80;
        server_name example.com www.example.com;

        location / {
            proxy_pass         http://app-b;
            proxy_redirect     off;
            proxy_set_header   Host $host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Host $server_name;

        }
}

```


This would direct all requests to test.com to the web app running in the first Docker container and all requests to example.com to the second Docker container.
----------------

In this time i want to rund one djano web site on docker

for impelimenting Djanog by docker we should make Dockerfile 

```
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
```

This Dockerfile starts with a Python 3 parent image. The parent image is modified by adding a new code directory. The parent image is further modified by installing the Python requirements defined in the requirements.txt file.

Save and close the Dockerfile.

Create a requirements.txt in your project directory.

This file is used by the RUN pip install -r requirements.txt command in your Dockerfile.

Add the required software in the file.

```
Django>=3.0,<=3.0

```
Create a file called docker-compose.yml in your project directory.

The docker-compose.yml file describes the services that make your app. In this example those services are a web server and database. The compose file also describes which Docker images these services use, how they link together, any volumes they might need mounted inside the containers. Finally, the docker-compose.yml file describes which ports these services expose. See the docker-compose.yml reference for more information on how this file works.

Add the following configuration to the file.

```
version: '3'

services:
  
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    
```



Create a Django project
In this step, you create a Django starter project by building the image from the build context defined in the previous procedure.

Change to the root of your project directory.

Create the Django project by running the docker-compose run command as follows.

```

sudo docker-compose run web   .
```


If you are running Docker on Linux, the files django-admin created are owned by root. This happens because the container runs as the root user. Change the ownership of the new files.

```
sudo chown -R $USER:$USER .
```

These settings are determined by the postgres Docker image specified in docker-compose.yml.

Save and close the file.

Run the docker-compose up command from the top level directory for your project.


docker-compose up

```
docker-compose up

```
docker rename portfolio-project_web_1 certificate.jasonjafari

 

 make 
 sudo nano /etc/nginx/conf.d/certificate.jasonjafari.conf

 
upstream  certificate.jasonjafari.com {
    server 127.0.0.1:8000;
}

server {
        listen 80;
        server_name certificate.jasonjafari.com ;

        location / {
            proxy_pass         http://certificate.jasonjafari.com;
            proxy_redirect     off;
            proxy_set_header   Host $host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Host $server_name;

        }
}



sudo service nginx restart


docker rename  certificate.jasonjafari   certificate.jasonjafari.com