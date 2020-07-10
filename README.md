# flask-rest-playground
I built this simple REST API (a CRUD for countries) just to explore Flask and Python a little bit more :)

## Installation (Windows):
### Create and activate an environment for the app:
    $ py -3 -m venv venv
    $ venv\Scripts\activate

### Install dependencies:
    $ pip install -U -r requirements.txt

### Run the application:
    $ set FLASK_APP=flask-rest-playground.py
    $ python -m flask run
The app will start running on localhost:5000.

## Usage:
This API consists of 5 endpoints. You can import flask-rest-playground.postman_collection.json into Postman and try them out.