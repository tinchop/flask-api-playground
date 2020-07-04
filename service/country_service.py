from model.city import City
from model.country import Country

class CountryService:

    def get_countries(self):
        argentina = Country('Argentina')
        buenos_aires = City('Buenos Aires')
        salta = City('Salta')
        ushuaia = City('Ushuaia')
        argentina.add_city(buenos_aires)
        argentina.add_city(salta)
        argentina.add_city(ushuaia)

        indonesia = Country('Indonesia')
        jakarta = City('Jakarta')
        indonesia.add_city(jakarta)

        return [argentina, indonesia]