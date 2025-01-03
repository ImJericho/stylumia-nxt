import os
import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
import json
from neo4j import GraphDatabase
import ast
from tqdm import tqdm
import networkx as nx
import plotly.graph_objects as go
import time
from streamlit_plotly_events import plotly_events
import ast
from dotenv import load_dotenv
from remove_fields_from_json import remove_fields_from_json

# import sys

# sys.path.append("/C:/IITISM/Dev/Stylumia/stylumia-nxt/web-scraper-engine")

# import post_scraper
from top100_bs import top100
from profile_scraper import profiles_scraper
from posts_scraper import all_posts_info

load_dotenv()


# Page 5:Social Trends page
def social_trends_page():

    st.title("Social Trends")
    st.write("Social Trends extracted from Instagram")
    if st.button("Get the List of Top 100 Insta Influencers"):
        top100_list = top100()
        st.write("Here is the list:")
        st.write(top100_list)

    if st.button("Get the profiles of Top 100 Insta Influencers"):
        posts_urls_list = profiles_scraper()
        st.write("Here is the list:")
        st.write(posts_urls_list)

    if st.button("Posts of Top 100"):
        # image_urls_list = [
        #     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1lIMq-ex44_W0z5WTCOgDDrqpYaSZ1LQOkA&s",
        #     "https://dist.neo4j.com/wp-content/uploads/20210621234221/0EdRw_utw9F-Hd7MW.png",
        # ]
        image_urls_list = all_posts_info()
        st.write("Here are the image URLs and the images:")
        for url in image_urls_list:
            st.image(url, caption=f"Image from {url}", use_column_width=True)


social_trends_page()