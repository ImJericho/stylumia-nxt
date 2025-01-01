import requests
from bs4 import BeautifulSoup


def extract_instagram_links(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for invalid HTTP responses

        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all anchor tags containing Instagram links
        links = soup.find_all("a", class_="user-id text-body d-block mb-1")

        # Filter links that contain 'instagram.com'
        # instagram_links = [
        #     link["href"] for link in links if "instagram.com" in link["href"]
        # ]
        instagram_links = [link.get_text(strip=True) for link in links]
        for i in range(len(instagram_links)):
            instagram_links[i] = "https://www.instagram.com/" + instagram_links[i]

        return instagram_links
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


# URL of the Viral Pitch page
url = "https://viralpitch.co/topinfluencers/instagram/top-100-instagram-influencers/"

# Extract Instagram profile links
instagram_profile_links = extract_instagram_links(url)

# Print the extracted Instagram links
print("Instagram Profile Links:")
for link in instagram_profile_links:
    print(link)
