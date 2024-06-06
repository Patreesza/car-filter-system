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


## Sample run 

Manual Test:

![CFS-Manual-Test](https://github.com/Patreesza/car-filter-system/assets/35329479/9e446ded-c857-4e4d-9ff7-021bb369e123)

Unit test result: 

![Screenshot 2024-06-07 025210](https://github.com/Patreesza/car-filter-system/assets/35329479/d0999d98-1aee-4c09-9898-e0bf29d957c4)


## Authors

Patreesza Marie Pantojan
[@Patreesza](https://github.com/Patreesza)
[LinkedIn](https://www.linkedin.com/in/patreesza-marie-pantojan/)
