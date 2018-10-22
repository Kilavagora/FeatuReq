Feature Requests
================

A simple feature requests tracking application built using [Flask](http://flask.pocoo.org/)/[PostgreSQL](https://www.postgresql.org/), [ES6](https://www.ecma-international.org/ecma-262/6.0/index.html), [Bootstrap](https://getbootstrap.com/), some CSS4 and a lot of fun.

Getting Started
---------------

To start the application install [docker](https://store.docker.com/search?type=edition&offering=community) and run in shell

```bash
docker-compose up -d
```

If it is the first launch, also run the following to create DB schema:

```bash
docker-compose run flask flask dbcreate
```

and then visit [http://localhost:8080/](http://localhost:8080/).

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
