import requests
import json

api_url = requests.get("https://restcountries.com/v3.1/all").content

def get_countries():
    def get_info(api_url):
        data = json.loads(api_url)
        result = []
        for country in data:
            try:
                country_info = {
                    "country": country["name"]["common"][0],
                    "capital": country["capital"][0],
                    "reigon": country["reigon"],
                    "flag": country["flags"]["png"]["alt"],
                    "currency": country["currencies"][0]["name"]
                }
                result.append(country_info)
            except KeyError:
                pass
        return result

    def display_info(api_url):
        data = json.loads(api_url)
        country_info = {
            "country_name": data["name"],
            "native_name": data["nativeName"],
            "capial": data["capital"],
            "reigon": data["reigon"],
            "flag": data["flags"]["png"],
            "currency": data["currencies"][0]["name"]
        }
        return country_info