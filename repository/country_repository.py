from tinydb import TinyDB, Query
from model.country import Country
from model.city import City

class CountryRepository:
    
    def __init__(self):
        print('creating CountryRepository...')
        self.db = TinyDB('db.json')
        countries = self.db.all()
        if len(countries) == 0:
            print('init db...')
            self.init_db()


    def get_all(self):
        return self.db.all()

    def init_db(self):
        print('initializing db...')
        argentina = Country('Argentina')
        buenos_aires = City('Buenos Aires')
        salta = City('Salta')
        ushuaia = City('Ushuaia')
        argentina.add_city(buenos_aires)
        argentina.add_city(salta)
        argentina.add_city(ushuaia)

        self.db.insert(argentina.to_JSON())

        indonesia = Country('Indonesia')
        jakarta = City('Jakarta')
        indonesia.add_city(jakarta)

        self.db.insert(indonesia.to_JSON())
        print('2 documents inserted')