# frontera-be

## Local start app
### Docker
#### Build image
```shell
$ docker-compose -f docker/docker-compose.yml build --no-cache
```
#### Up Container
```shell
$ docker-compose -f docker/docker-compose.yml up
```
Note: Use -d flag to up container in background

#### Create superuser (admin)
```shell
$ docker exec -it frontera-be python manage.py createsuperuser
```

### Start app without docker
```shell
$ pip3 install -r requirements/requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
$ python3 manage.py runserver 0.0.0.0:8000
```

Enjoy:) Go to http://localhost:8000/