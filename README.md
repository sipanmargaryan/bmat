# bmat

## Setup

Make sure you have `docker` and `docker-compose` installed on your machine.

Create `.env` file using `.env_template`.

Commands

To build the project

    make

To run the project

    make run

To jump into container migrate database and create superuser

    $ make shell
    root@<containerid>:/project# python3 manage.py migrate
    root@<containerid>:/project# python3 manage.py createsuperuser

To stop running containers

    make stop
