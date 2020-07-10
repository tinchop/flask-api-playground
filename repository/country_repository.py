from tinydb import TinyDB, Query
from model.country import Country
from model.city import City
import json

class CountryRepository:
    
    def __init__(self):
        self.db = TinyDB('db.json')
        self.query = Query()

    def get_all(self):
        return self.db.all()

    def get_by_name(self, name):
        return self.db.search(self.query.name == name)

    def create(self, name):
        country = Country(name)
        self.db.insert(self.__serialize(country))

    def add_city(self, country_name, city_name):
        country = self.get_by_name(country_name)[0]
        cities = country['cities']
        cities.append(City(city_name))
        self.db.update({'cities': self.__serialize(cities)}, self.query.name == country_name)

    def remove(self, name):
        self.db.remove(self.query.name == name)

    def __serialize(self, objekt):
        return json.loads(json.dumps(objekt, default=lambda o: o.__dict__))