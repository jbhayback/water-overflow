# water-overflow Calculator and Illustrator

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
    <li><a href="#assumptions-and-constraints">Assumptions and Constraints</a></li>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


## __About The Project__

**Water Overflow Calculator and Illustrator**

This project is a simple application for calculating and illustrating how much liquid is in the glass/container given its position when K liters of liquid is poured in the top most glass. There is a stack of water glasses in a form of triangle. Each glass has a 250mL capacity. When a liquid is poured into the top most glass any overflow is evenly distributed between the glasses in the next row. That is, half of the overflow pours into the left glass while the remainder of the overflow pours into the right glass.

## Built With
* [Django](https://www.djangoproject.com/) - Web
* [Bootstrap](https://getbootstrap.com/) - UI


## __Technical Design Document (TDD)__
 ![tdd-diagram](https://github.com/jbhayback/water-overflow/blob/main/water_overflow/calculator/static/images/TDD_WO.png)
 - The flow of the application is shown in the diagram above.
 - On the client side, user shall set the input data needed by the application for water overflow calculation.
 - The server will then validate the input data.
 - If the input data are valid based on the requirements, the calculation overflow content of the specified position of the glass/container will be displayed as well as the graphical illustration. Otherwise, an error message will be returned.


## __Getting Started__
- ## Prerequisites
  - Local
    * [Python](https://www.python.org/download/releases/3.0/) - at least 3.x.x
    * [Django](https://www.djangoproject.com/)
    * [Pytest](https://pypi.org/project/pytest/)
  - Docker and Docker Compose
    * [Docker](https://www.docker.com/)
      * [Installation](https://docs.docker.com/engine/install/)
    * [Docker compose](https://docs.docker.com/compose/)
      * [Installation](https://docs.docker.com/compose/install/)

- ## Setup
    - __IMPORTANT NOTE: Be sure to run these commands within the project root directory.__
    - ### __Local CLI__
        - Create any python virtual env and activate it.
        - Install required packages
        ```
        $ pip install -r requirements/local_cli_setup_requirements.txt
        ```
        - You can then proceed to functional testing.
        
    - ### __Local WebApp using Django__
        - Create any python virtual env and activate it.
        - Install required packages.
        ```
        $ pip install -r requirements/requirements.txt
        ```
        - Perform migration
        ```
        $ python ./water_overflow/manage.py migrate
        ```
        - Run webserver.
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

- ## Assumptions and Constraints
  - For the succeeding rows (2nd and beyond), the liquid will also overflow to the part where the upper layer glass is mounted.
  - Constraints:
    - 0.00 < __K__(input liquid volume) <= 1000.00 (K can handle up to hundredths decimal place with increment of 0.01)
    - 0 <= (__J__)Position <= Row(__i__) - Non-negative integers only


- ## Testing
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
