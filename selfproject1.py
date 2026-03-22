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
        response.raise_for_status()

    except requests.HTTPError:
        print("Unable to extract data from the server. Request Failed.")

    else:
        data = response.json()
        print(f"Title: {data.get('title')}")
        print(f"URL: {data.get('url')}")


main()




