# bmat

## Setup

Make sure you have `docker` and `docker-compose` installed on your machine.

Create `.env` file using `.env_template`.

Commands on linux and macos  enviroments

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

### Part1:

To run execute code.

    $ make shell
    root@<containerid>:/project# python3 manage.py works_metadata
    
Questions answers
    
    1. ISWC could be enough to identify	a work. If no ISWC is provided, title and at least one contributor should be the same. In case there are	different sets of contributors from different inputs, you could take the union of them.
    2. if I understand question right. Then we can make an endpoint where users can send data we will create celery worker to add data into database.  
    
### Part2:
    $ make run 
    
    go by this link http://localhost:8000/api-docs/ you will se the endpoint
    
Questions answers

    1. 2 If we add database index for iswc field response time will be almost the same.