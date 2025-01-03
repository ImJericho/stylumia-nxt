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
load_dotenv() 
from config import NEOCONN

# Page 4: Ontology Page
def ontology_page(neo4j_conn):
    st.title("Verified Ontology")
    
    # Get verified entities
    conn = sqlite3.connect('verified_ontology.db')
    verified_df = pd.read_sql_query("SELECT * FROM verified_entities", conn)
    conn.close()
    
    # Display verified entities with Neo4j counts
    for entity_type in ['superclass', 'subclass', 'subsubclass', 'category']:
        st.subheader(f"Verified {entity_type}")
        entities = verified_df[verified_df['entity_type'] == entity_type]
        
        for _, row in entities.iterrows():
            # Get count from Neo4j
            # query = f"""
            # MATCH (n:{entity_type} {{name: $name}})<-[:HAS_{entity_type.upper()}]-(p)
            # RETURN count(p) as count
            # """
            # result = neo4j_conn.query(query, parameters={'name': row['entity_value']})
            # count = result[0]['count'] if result else 0
            
            st.write(f"{row['entity_value']}")
    
    # Display other verified entities
    for entity_type in ['style_attribute', 'feature_list']:
        st.subheader(f"Verified {entity_type}")
        entities = verified_df[verified_df['entity_type'] == entity_type]
        for _, row in entities.iterrows():
            st.write(row['entity_value'])

ontology_page(NEOCONN)