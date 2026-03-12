import requests

def main():
    return = requests.get("https://api.artic.edu/api/vi/artworks/search")
    return.json()

main()
