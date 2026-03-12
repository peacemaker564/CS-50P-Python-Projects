import requests

def main():
    response = requests.get("https://api.artic.edu/api/vi/artworks/search")
    content = response.json()
    print(content)

main()
