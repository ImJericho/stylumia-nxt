import instaloader
from datetime import datetime
from dateutil.relativedelta import relativedelta
from top100_bs import top100
import time


def extract_instagram_post_urls_for_profile(profile_name, session_username):
    loader = instaloader.Instaloader()

    today = datetime.now()
    one_month_ago = today - relativedelta(days=1)
    one_month_ago_timestamp = int(one_month_ago.timestamp())

    try:
        loader.load_session_from_file(session_username)
        profile = instaloader.Profile.from_username(loader.context, profile_name)
        post_urls = []
        for post in profile.get_posts():
            post_url = f"https://www.instagram.com/p/{post.shortcode}/"
            post_date = post.date
            post_date_timestamp = post_date.timestamp()
            post_urls.append(post_url)
            if post_date_timestamp < one_month_ago_timestamp:
                break

        return post_urls

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"The profile '{profile_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def profiles_scraper():
    post_urls_for_all_profiles = [
        "https://www.instagram.com/p/DGQw9PJxNLD/",
        "https://www.instagram.com/p/DGQIEqJA8dg/",
        "https://www.instagram.com/p/DGOQEk2N1Er/",
        "https://www.instagram.com/p/DGRBdFHyaVy/",
        "https://www.instagram.com/p/DGRFfhBycAo/",
        "https://www.instagram.com/p/DGQlwEgJwyU/",
        "https://www.instagram.com/p/DCzGDOxxMua/",
        "https://www.instagram.com/p/DGOF7Olvv6I/",
        "https://www.instagram.com/p/DGEzQKStB71/",
        "https://www.instagram.com/p/DGQg7AVJgat/",
    ]
    instagram_profile_links = top100()
    print(instagram_profile_links)
    session_username = "testingaccount004"
    c = 0
    for profile_name in instagram_profile_links:
        post_urls_for_one_profile = extract_instagram_post_urls_for_profile(
            profile_name, session_username
        )
        if post_urls_for_one_profile:
            print(
                f"Extracted {len(post_urls_for_one_profile)} post URLs from {profile_name}:"
            )
            for url in post_urls_for_one_profile:
                print(url)
            post_urls_for_all_profiles.extend(post_urls_for_one_profile)
        time.sleep(5)
        c += 1
        if c == 1:
            break

    return post_urls_for_all_profiles


# profiles_scraper()
