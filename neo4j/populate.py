from typing import Dict, List, Optional
import pandas as pd
import json
from neo4j import GraphDatabase
import ast
from tqdm import tqdm
import logging
from transformers import pipeline
import os
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()
from data import objects


def getShortField(field):
    return field.replace(" ", "_")


class FashionOntologySystem:
    def __init__(self, uri: str, user: str, password: str):
        """Initialize the Fashion Ontology System with Neo4j credentials."""
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.setup_logging()

    def setup_logging(self):
        """Set up logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler("fashion_ontology.log"),
                logging.StreamHandler(),
            ],
        )
        self.logger = logging.getLogger(__name__)

    def load_data(self, objects: list[dict], batch_size: int = 1000):
        """Load data from Json Object into Neo4j."""
        self.logger.info(f"Loading data")

        with self.driver.session() as session:
            for obj in tqdm(objects):
                try:
                    # Create Cypher query
                    query = """
                    MERGE (p:Product {product_id: $product_id})
                    SET p.name = $product_name

                    MERGE (sc:Superclass {name: $superclass})
                    MERGE (p)-[:BELONGS_TO]->(sc)

                    MERGE (sbc:Subclass {name: $subclass})
                    MERGE (p)-[:BELONGS_TO]->(sbc)

                    MERGE (ssbc:Subsubclass {name: $subsubclass})
                    MERGE (p)-[:BELONGS_TO]->(ssbc)

                    MERGE (c:Category {name: $category})
                    MERGE (p)-[:BELONGS_TO]->(c)
                    """

                    # Add other relations if they exist
                    for key, value in obj.items():
                        if key not in [
                            "product name",
                            "sno",
                            "superclass",
                            "subclass",
                            "subsubclass",
                            "category",
                        ]:
                            query += (
                                f"""
                            MERGE (a"""
                                + getShortField(key)
                                + ":"
                                + getShortField(key)
                                + "{name: $"
                                + getShortField(key)
                                + """}) 
                            MERGE (p)-[:HAS]->(a"""
                                + getShortField(key)
                                + """)
                            """
                            )

                    # Execute query
                    session.run(
                        query,
                        product_id=obj["sno"],
                        product_name=obj["product name"],
                        superclass=obj["superclass"],
                        subclass=obj["subclass"],
                        subsubclass=obj["subsubclass"],
                        category=obj["category"],
                        **{
                            getShortField(key): obj[key]
                            for key in obj
                            if key
                            not in [
                                "product name",
                                "sno",
                                "superclass",
                                "subclass",
                                "subsubclass",
                                "category",
                            ]
                        },
                    )

                except Exception as e:
                    self.logger.error(f"Error processing row: {obj['product name']}")
                    self.logger.error(str(e))

    def close(self):
        """Close the Neo4j connection."""
        self.driver.close()


def main():
    URI = os.getenv("NEO4J_URI")
    USER = os.getenv("NEO4J_USERNAME")
    PASSWORD = os.getenv("NEO4J_PASSWORD")

    DIR = os.path.dirname(os.path.abspath(__file__))
    DATADIR = os.path.join(DIR, "..", "data")
    # Initialize system
    system = FashionOntologySystem(URI, USER, PASSWORD)

    try:

        DIR = os.path.dirname(os.path.abspath(__file__))

        # Process each CSV file
        Objects = objects

        system.load_data(Objects)

    finally:
        system.close()


if __name__ == "__main__":
    main()
