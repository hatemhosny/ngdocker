# A basic Angular app that connects to Flask API, with Docker setup for development and production workflow

Clone the repo:

`$ git clone https://github.com/hatemhosny/ngdocker.git`

`$ cd ngdocker`

## Development workflow

`$ docker-compose up`

runs the frontend Angular app at: http://docker-machine-ip:4200

and Flask API at: http://docker-machine-ip:3001

with live reload for both.

hint: you can find the `docker-machine-ip` by running:

`$ docker-machine ip`

To stop and delete both containers, run:

`$ docker-compose down`



## Production workflow

`$ docker-compose -f docker-compose.prod.yml up`

builds the frontend Angular app for production and serves it with NGINX at: http://docker-machine-ip:3000

and Flask API at: http://docker-machine-ip:3001

with NO live reload.

To rebuild after changes, run:

`$ docker-compose -f docker-compose.prod.yml up --build`

To stop and delete both containers, run:

`$ docker-compose -f docker-compose.prod.yml down`

## TODO:
- Serve Flask API in production by Gunicorn
- Add MongoDB
- Run tests
- Continuous integration
- Continuous Deployment
