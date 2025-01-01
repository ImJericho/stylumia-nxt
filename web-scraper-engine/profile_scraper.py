import instaloader
from datetime import datetime
from dateutil.relativedelta import relativedelta


def extract_instagram_post_urls(profile_name, session_username):
    loader = instaloader.Instaloader()

    today = datetime.now()
    one_month_ago = today - relativedelta(months=1)
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


profile_name = "_arshdeep.singh__"
session_username = "shashvat_sj"
post_urls = extract_instagram_post_urls(profile_name, session_username)
if post_urls:
    print(f"Extracted {len(post_urls)} post URLs from {profile_name}:")
    for url in post_urls:
        print(url)
