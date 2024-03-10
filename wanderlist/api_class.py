import requests


class GetCountry():
    def __init__(self):
        self.my_api = "https://restcountries.com/v3.1/region/"
        self.country_api = "https://restcountries.com/v2/name/"