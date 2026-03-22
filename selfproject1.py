#Making a program to pull off astrology image of the date data from the nasa website.
#1. Asking the user for the date of which to grab the image url.
#2. Using requests.get
import requests


def main():
    try:
        Date = input("Date(YYYY-MM-DD): ")
        API_KEY = 'f4QMMo67hOf8fpbd41IxWWC9o37FPmIojIFAcrMF'
        url = 'https://api.nasa.gov/planetary/apod'

        params = {
            'api_key' : API_KEY,
            'date' : Date
        }

        response = requests.get(url, params = params)
        






