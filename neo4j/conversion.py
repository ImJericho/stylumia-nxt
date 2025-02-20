from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable, AuthError
from pyvis.network import Network
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


# Step 1: Connect to Neo4j AuraDB
def fetch_graph_from_aura(uri, user, password):
    try:
        driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=True)
        with driver.session() as session:
            query = "MATCH (a)-[r]->(b) RETURN a.name AS source, b.name AS target"
            result = session.run(query)
            nodes = set()
            edges = []
            for record in result:
                nodes.add(record["source"])
                nodes.add(record["target"])
                edges.append((record["source"], record["target"]))
            return nodes, edges
    except ServiceUnavailable:
        print(
            "Error: Unable to connect to the database. Please check your network or IP allowlist."
        )
    except AuthError:
        print("Error: Authentication failed. Verify your username and password.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if driver:
            driver.close()


def create_pyvis_graph(nodes, edges):
    net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
    for node, label in nodes:
        net.add_node(node, label=label)
    for source, target in edges:
        net.add_edge(source, target)
    return net


st.title("Neo4j Graph Visualization")
uri = st.text_input("AuraDB URI", "bolt://<YOUR_AURA_DB_URI>")
user = st.text_input("Username", "neo4j")
password = st.text_input("Password", type="password")
# query = st.text_area(
#     "Cypher Query",
#     """
#     MATCH (a)-[r]->(b)
#     RETURN a.name AS source, b.name AS target, labels(a)[0] AS source_label, labels(b)[0] AS target_label
#     """,
# )

if st.button("Fetch and Display Graph"):
    try:
        nodes, edges = fetch_graph_from_aura(uri, user, password)
        net = create_pyvis_graph(nodes, edges)
        net.save_graph("graph.html")

        # Display the graph in Streamlit
        with open("graph.html", "r") as f:
            html_code = f.read()
        st.components.v1.html(html_code, height=750)
    except Exception as e:
        st.error(f"Error: {e}")
