from repository.country_repository import CountryRepository

class CountryService:

    def __init__(self):
        self.repository = CountryRepository()

    def get_countries(self):
        return self.repository.get_all()