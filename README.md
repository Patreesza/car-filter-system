# Project Title

IT Test task Django developer

## Description

As a customer I want a web application where where I can search for cars given by certain criteria.
There should be the possibility to download the result list in xml format.

Requirements:
    Domain object is a car with length, weight, velocity, color
    Web search which respects all criteria at the same time
    Result list can be downloaded as xml

## Getting Started

### Dependencies

- Framework: Django 4.2
- DB: MySql 

### Installing

Step by step to setup:

- Install virtualenv for python
- Activate virtualenv and install requirements.txt (`pip install -r car/requirements.txt`)
- Create mysql database
- Create .env file and copy content from .env.template
- Setup database credential in .env 
- Create root user with `python car/manage.py createsuperuser`
- Load fixtures `python car/manage.py loaddata car_app/migrations/fixtures/car_initial.json`

### Executing program

- Run Django server `python car/manage.py runserver` 


## Authors

Patreesza Marie Pantojan
[@Patreesza](https://github.com/Patreesza)
[LinkedIn @Patreesza](https://www.linkedin.com/in/patreesza-marie-pantojan/)
