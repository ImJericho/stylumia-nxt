import httpx
import json
from typing import Dict
from urllib.parse import quote
import wget

INSTAGRAM_DOCUMENT_ID = "8845758582119845"  # contst id for post documents instagram.com


def scrape_post(url_or_shortcode: str) -> Dict:
    """Scrape single Instagram post data"""
    if "http" in url_or_shortcode:
        shortcode = url_or_shortcode.split("/p/")[-1].split("/")[0]
    else:
        shortcode = url_or_shortcode
    print(f"scraping instagram post: {shortcode}")

    variables = quote(
        json.dumps(
            {
                "shortcode": shortcode,
                "fetch_tagged_user_count": None,
                "hoisted_comment_id": None,
                "hoisted_reply_id": None,
            },
            separators=(",", ":"),
        )
    )
    body = f"variables={variables}&doc_id={INSTAGRAM_DOCUMENT_ID}"
    url = "https://www.instagram.com/graphql/query"

    result = httpx.post(
        url=url,
        headers={"content-type": "application/x-www-form-urlencoded"},
        data=body,
    )
    data = json.loads(result.content)
    return data["data"]["xdt_shortcode_media"]


# Example usage:
posts = scrape_post("https://www.instagram.com/p/CuE2WNQs6vH/")
# posts = scrape_post("https://www.instagram.com/p/DD7oBI2RtAR/")
link = ""
if posts["is_video"] == True:
    link = posts["video_url"]
    # response = requests.get(link, stream=True)
    # file = open("video.mp4", "wb")
    # for chunk in response.iter_content(chunk_size=1024):
    #   if chunk:
    #     file.write(chunk)
    response = wget.download(link, "video.mp4")
else:
    link = posts["display_url"]
    response = wget.download(link, "image.jpg")

caption = posts["edge_media_to_caption"]["edges"][0]["node"]["text"]
comments_count = posts["edge_media_to_parent_comment"]["count"]
likes_count = posts["edge_media_preview_like"]["count"]
comments_list = []
for p in posts["edge_media_to_parent_comment"]["edges"]:
    comments_list.append(
        {
            "comment": p["node"]["text"],
            "username": p["node"]["owner"]["username"],
            "likes": p["node"]["edge_liked_by"]["count"],
        }
    )
