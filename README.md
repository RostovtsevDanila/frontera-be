# frontera-be

### Build image
```shell
$ docker-compose -f docker/docker-compose.yml build --no-cache
```
### Up Container
```shell
$ docker-compose -f docker/docker-compose.yml up
```
Note: Use -d flag to up container in background

### Create superuser (admin)
```shell
$ docker exec -it frontera-be python manage.py createsuperuser
```
