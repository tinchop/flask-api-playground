from flask import Flask, jsonify
from repository.country_repository import CountryRepository

app = Flask(__name__)

country_repository = CountryRepository()

@app.route('/countries', methods = ['GET'])
def countries():
    return jsonify(country_repository.get_all())

@app.route('/country/<name>', methods = ['GET'])
def country_by_name(name):
    return jsonify(country_repository.get_by_name(name))

@app.route('/country/<name>', methods = ['POST'])
def create_country(name):
    country_repository.create(name)
    return 'Country ' + name + ' created successfully.'

@app.route('/country/<name>/city/<city>', methods = ['PATCH'])
def add_city(name, city):
    country_repository.add_city(name, city)
    return 'City ' + city + ' successfully added to country ' + name + '.'

@app.route('/country/<name>', methods = ['DELETE'])
def remove_country(name):
    country_repository.remove(name)
    return 'Country ' + name + ' removed successfully.'