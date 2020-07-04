from flask import Flask
from service.country_service import CountryService
import json

app = Flask(__name__)

@app.route('/countries')
def countries():
    country_service = CountryService()
    return json.dumps(country_service.get_countries(), default=lambda o: o.__dict__, indent=4)
