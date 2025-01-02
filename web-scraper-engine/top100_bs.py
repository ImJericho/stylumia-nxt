import requests
from bs4 import BeautifulSoup


def extract_instagram_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        links = soup.find_all("a", class_="user-id text-body d-block mb-1")

        # instagram_links = [
        #     link["href"] for link in links if "instagram.com" in link["href"]
        # ]
        instagram_links = [link.get_text(strip=True) for link in links]

        return instagram_links
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def top100():
    url = (
        "https://viralpitch.co/topinfluencers/instagram/top-100-instagram-influencers/"
    )
    instagram_profile_links = extract_instagram_links(url)

    print("Instagram Profile Links:")
    for link in instagram_profile_links:
        print(link)
        break

    return instagram_profile_links


top100()
