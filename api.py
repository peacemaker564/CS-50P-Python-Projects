import requests

def main():
    try:

        print("Search the artworks of artists u like.")

        artist = input("Artist: ")

        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist} #q is the specific keyword mentioned on the UOC website
                           #to access a particular artists's work.
            )
        content = response.json()
        response.raise_for_status()

    except requests.HTTPError:
        print("Failed to complete the request.")

    else:
        for artwork in content["data"]:
            print(f"*{artwork['title']}")

main()
