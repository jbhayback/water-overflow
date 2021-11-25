# water-overflow Calculator

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
      <a href="#technical-design-document">Technical Design Document (TDD)</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#setup">Setup</a></li>
      </ul>
    </li>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


## __About The Project__

**Water Overflow Calculator**

This project is a simple application for calculating and illustrating how much liquid is in the glass/container given its position when K liters of liquid is poured in the top most glass.

## Built With
* [Django](https://www.djangoproject.com/) - Web
* [Bootstrap](https://getbootstrap.com/) - UI


## __Technical Design Document (TDD)__
 ![tdd-diagram](https://github.com/jbhayback/water-overflow/blob/main/water_overflow/calculator/static/images/TDD_WO.png)
 - The flow of the application is shown in the diagram above.
 - On the client side, user shall set the input data needed by the application for water overflow calculation.
 - The server will then validate the input data.
 - If the input data are valid based on the requirements, the calculation overflow content of the specified position of the glass/container will be displayed. Other wise, an error message will be returned.

## __Getting Started__
- ## Prerequisites
  - Docker and Docker Compose
    * [Docker](https://www.docker.com/)
      * [Installation](https://docs.docker.com/engine/install/)
    * [Docker compose](https://docs.docker.com/compose/)
      * [Installation](https://docs.docker.com/compose/install/)

- ## Setup (__Be sure to run these commands inside the project root directory__)
    - ### __Local CLI__
        - Create virtual env and activate it.
        - Install required packages
        ```
        $ pip install -r requirements/requirements.txt
        ```
        - You can immediately perform the functional testing.
        
    - ### __Local WebApp using Django__
        - Create virtual env and activate it.
        - Install required packages
        ```
        $ pip install -r requirements/requirements.txt
        ```
        - Perform migration
        ```
        $ python ./water_overflow/manage.py migrate
        ```
        - Run server
        ```
        $ python ./water_overflow/manage.py runserver
        ```
        - You can then access the app via port 8000.
        ```
        http://localhost:8000/
        ```
    - ### __Docker and Docker Compose__
        - Build `web` image
        ```
        $ docker-compose build
        ```
        - Once build is successful, run the application.
        ```
        $ docker-compose up -d
        ```
        - You can then access the app via port 8001.
        ```
        http://localhost:8001/
        ```

 ## Testing
 - ### Unit Testing
    - Local CLI
    ```
    $ pytest -v water_overflow/calculator/tests.py
    ```
    - Local WebApp using Django
    ```
    $ python ./water_overflow/manage.py test calculator
    ```
    - Docker and Docker Compose setup
    ```
    $ docker-compose run web python ./water_overflow/manage.py test calculator
    ```

- ### Functional Testing
    - Access
        * http://localhost:8000/ - if local webapp using Django setup
        * http://localhost:8001/ - if docker and docker-compose webapp setup
            - Sample Images:
                - ![django-sample](https://github.com/jbhayback/water-overflow/blob/main/water_overflow/calculator/static/images/functional_test_using_django.jpg)
    - For local CLI, you can perform this command: python main.py {liquid_volume_input} {row} {position}
        - example:
        ```
        $ python main.py 3 1 1
        ```
        - Sample image
            - ![cli-sample](https://github.com/jbhayback/water-overflow/blob/main/water_overflow/calculator/static/images/functional_test_using_cli.jpg)

 ## Contact
- You can contact me via email: jbhayback@gmail.com for more info or if there are errors during the setup.
