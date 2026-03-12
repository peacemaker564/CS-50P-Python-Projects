import requests

def main():
    try:
        response = requests.get("https://api.artic.edu/api/v1/artworks/search")
        content = response.json()

    except requests.RequestException:
        print("Probable network issue.")

    else:
        for artwork in content["data"]:
            print(f"*{artwork['title']}")

main()
