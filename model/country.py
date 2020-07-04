from .place import Place

class Country(Place):

    def __init__(self, name):
        super().__init__(name)
        self.cities = []
        

    def add_city(self, city):
        self.cities.append(city)
