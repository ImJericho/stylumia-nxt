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

load_dotenv()


# Initialize databases
def init_sqlite_db():
    # Create verified ontology database
    conn_verified = sqlite3.connect("verified_ontology.db")
    c = conn_verified.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS verified_entities
                 (entity_type TEXT, entity_value TEXT, PRIMARY KEY (entity_type, entity_value))"""
    )
    conn_verified.commit()
    conn_verified.close()

    # Create unverified ontology database
    conn_ontology = sqlite3.connect("ontology.db")
    c = conn_ontology.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS unverified_entities
                 (entity_type TEXT, entity_value TEXT, PRIMARY KEY (entity_type, entity_value))"""
    )
    conn_ontology.commit()
    conn_ontology.close()


class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]


# Page 1: Neo4j Query Page
def neo4j_query_page(neo4j_conn):
    st.title("Neo4j Query Explorer")

    # Search box
    search_query = st.text_input("Enter Cypher Query:")

    if st.button("Execute Query"):
        if search_query:
            try:
                results = neo4j_conn.query(search_query)
                st.write("Query Results:")
                df = pd.DataFrame([dict(record) for record in results])
                st.dataframe(df)

                # Create network graph visualization
                G = nx.Graph()
                for record in results:
                    # Add nodes and edges based on query results
                    # This is a simplified version - adjust based on your data structure
                    for key, value in dict(record).items():
                        G.add_node(str(value))

                # Create plotly figure
                pos = nx.spring_layout(G)
                edge_x = []
                edge_y = []
                for edge in G.edges():
                    x0, y0 = pos[edge[0]]
                    x1, y1 = pos[edge[1]]
                    edge_x.extend([x0, x1, None])
                    edge_y.extend([y0, y1, None])

                node_x = [pos[node][0] for node in G.nodes()]
                node_y = [pos[node][1] for node in G.nodes()]

                fig = go.Figure()
                fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode="lines"))
                fig.add_trace(
                    go.Scatter(
                        x=node_x,
                        y=node_y,
                        mode="markers+text",
                        text=list(G.nodes()),
                        textposition="top center",
                    )
                )

                st.plotly_chart(fig)

            except Exception as e:
                st.error(f"Error executing query: {str(e)}")


# Page 2: Trend Analysis
def trend_analysis_page():
    st.title("Trend Analysis")

    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    if uploaded_file:
        # Show progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()

        # Process file
        df = pd.read_csv(uploaded_file)
        processed_rows = []
        processed_data = []
        graph_placeholder = st.empty()
        required_columns = ["superclass", "class", "type", "variant", "style"]
        for index, row in df.iterrows():
            # Update progress
            progress = (index + 1) / len(df)
            progress_bar.progress(progress)
            status_text.text(f"Processing row {index + 1} of {len(df)}")

            # Process row (implement your processing logic here)
            # processed_row = process_row(row)
            # processed_rows.append(processed_row)

            for col in required_columns:
                processed_data.append(row[col])
            processed_rows.append(row)
            if index % 10 == 0 or index == len(df) - 1:
                frequency_df = pd.DataFrame(processed_data, columns=["value"])
                frequency_counts = frequency_df["value"].value_counts().reset_index()
                frequency_counts.columns = ["Value", "Frequency"]

                # Generate the graph
                fig = px.bar(
                    frequency_counts,
                    x="Value",
                    y="Frequency",
                    title="Frequency Analysis",
                    labels={"Value": "Category", "Frequency": "Count"},
                    text="Frequency",
                )
                graph_placeholder.plotly_chart(fig, use_container_width=True)

            time.sleep(0.1)  # Simulate processing time

        # Create DataFrame from processed rows
        processed_df = pd.DataFrame(processed_rows)

        # Show processed data
        st.subheader("Processed Data")
        st.dataframe(processed_df)

        # Create frequency graphs
        # create_frequency_graphs(processed_df)

        # Update databases
        # update_databases(processed_df)


def process_row(row):
    # Implement your row processing logic here
    return {
        "superclass": "example_superclass",
        "subclass": "example_subclass",
        "subsubclass": "example_subsubclass",
        "category": "example_category",
        "feature_list": ["feature1", "feature2"],
        "style_attributes": {"attr1": "value1"},
    }


def create_frequency_graphs(df):
    # Create graphs for class hierarchies
    for column in ["superclass", "subclass", "subsubclass", "category"]:
        fig = px.bar(df[column].value_counts(), title=f"{column} Distribution")
        st.plotly_chart(fig)

    # Create graph for features
    feature_counts = {}
    for features in df["feature_list"]:
        for feature in features:
            feature_counts[feature] = feature_counts.get(feature, 0) + 1

    fig = px.bar(pd.Series(feature_counts), title="Feature Distribution")
    st.plotly_chart(fig)

    # Create graph for style attributes
    style_counts = {}
    for attrs in df["style_attributes"]:
        for key in attrs:
            style_counts[key] = style_counts.get(key, 0) + 1

    fig = px.bar(pd.Series(style_counts), title="Style Attributes Distribution")
    st.plotly_chart(fig)


# Page 3: Verification Page
def verification_page():
    st.title("Entity Verification")

    # Get unverified entities
    conn = sqlite3.connect("ontology.db")
    unverified_df = pd.read_sql_query("SELECT * FROM unverified_entities", conn)
    conn.close()

    # Display unverified entities
    st.subheader("Unverified Entities")
    for entity_type in [
        "superclass",
        "subclass",
        "subsubclass",
        "category",
        "style_attribute",
        "feature_list",
    ]:
        st.write(f"\n{entity_type}:")
        entities = unverified_df[unverified_df["entity_type"] == entity_type]

        for _, row in entities.iterrows():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(row["entity_value"])
            with col2:
                if st.button(f"Verify {row['entity_value']}"):
                    verify_entity(row["entity_type"], row["entity_value"])
                    st.experimental_rerun()


def verify_entity(entity_type, entity_value):
    # Move entity from unverified to verified database
    conn_verified = sqlite3.connect("verified_ontology.db")
    c_verified = conn_verified.cursor()
    c_verified.execute(
        "INSERT INTO verified_entities VALUES (?, ?)", (entity_type, entity_value)
    )
    conn_verified.commit()
    conn_verified.close()

    conn_ontology = sqlite3.connect("ontology.db")
    c_ontology = conn_ontology.cursor()
    c_ontology.execute(
        "DELETE FROM unverified_entities WHERE entity_type=? AND entity_value=?",
        (entity_type, entity_value),
    )
    conn_ontology.commit()
    conn_ontology.close()


# Page 4: Ontology Page
def ontology_page(neo4j_conn):
    st.title("Verified Ontology")

    # Get verified entities
    conn = sqlite3.connect("verified_ontology.db")
    verified_df = pd.read_sql_query("SELECT * FROM verified_entities", conn)
    conn.close()

    # Display verified entities with Neo4j counts
    for entity_type in ["superclass", "subclass", "subsubclass", "category"]:
        st.subheader(f"Verified {entity_type}")
        entities = verified_df[verified_df["entity_type"] == entity_type]

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
    for entity_type in ["style_attribute", "feature_list"]:
        st.subheader(f"Verified {entity_type}")
        entities = verified_df[verified_df["entity_type"] == entity_type]
        for _, row in entities.iterrows():
            st.write(row["entity_value"])


def main():
    st.set_page_config(page_title="Fashion Analytics", layout="wide")

    URI = os.getenv("NEO4J_URI")
    USER = os.getenv("NEO4J_USERNAME")
    PASSWORD = os.getenv("NEO4J_PASSWORD")

    # Initialize databases
    init_sqlite_db()

    # Initialize Neo4j connection
    neo4j_conn = Neo4jConnection(uri=URI, user=USER, password=PASSWORD)

    # Sidebar navigation
    page = st.sidebar.selectbox(
        "Select Page", ["Neo4j Query", "Trend Analysis", "Verification", "Ontology"]
    )

    if page == "Neo4j Query":
        neo4j_query_page(neo4j_conn)
    elif page == "Trend Analysis":
        trend_analysis_page()
    elif page == "Verification":
        verification_page()
    else:  # Ontology
        ontology_page(neo4j_conn)


if __name__ == "__main__":
    main()
