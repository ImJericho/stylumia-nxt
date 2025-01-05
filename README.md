# Fashion Ontology and Trend Analysis Platform

## Overview

Our solution is a cutting-edge AI-powered platform designed to revolutionize the fashion industry. By combining advanced machine learning models with a scalable graph database, we automate feature extraction, ontology creation, and trend analysis for fashion products. Our system ensures adaptability to emerging trends, providing unparalleled insights into the ever-changing fashion landscape.

### Key Features:
- **AI-Driven Models** for feature extraction from text and images.
- **Dynamic Ontology Framework** that evolves with incoming data.
- **Scalable Neo4j AuraDB** for efficient data storage and querying.
- **Interactive User Interface** for stakeholders and fashion experts.
- **Social Media Trend Analysis Engine** for identifying emerging styles.
![Screenshot 2025-01-05 183105](https://github.com/user-attachments/assets/67852dc5-7c1e-42f1-b32c-426837b64ee2)
![Screenshot (225)](https://github.com/user-attachments/assets/15bed628-d870-4dba-8828-d0fba96df9e8)

---

## Technical Implementation Details

### Models and Pipelines

#### 1. **Image-to-Text Model**:
   - **Purpose**: Extracts features from product images.
   - **Base Model**: LLaVA-3 (instruction-based extraction).
   - **Workflow**:
     - **Object Detection**: Identifies the primary product in the image.
     - **Detailed Analysis**: Extracts attributes and features for the identified product.

#### 2. **Text-to-Text Model**:
   - **Purpose**: Processes product descriptions and generates key-value pairs of style attributes in JSON format.
   - **Base Model**: LLaMA 3.2-Instruct-8B fine-tuned using Q-LoRA PEFT.
   - **Optimizations**: Quantized for minimal GPU usage during inference.

#### 3. **Text-to-Ontology Model**:
   - **Purpose**: Expands the ontology dynamically or fits data into existing structures.
   - **Phases**:
     - **Similarity Matching**: Calculates cosine similarity between new data and existing ontology classes.
     - **Class Generation**: Creates new classes if no match is found, ensuring generic applicability.

---

### Ontology Structure / Schema

#### Hierarchy:
1. **Superclass**: Broad categories (e.g., Shoes, Clothing).
2. **Class**: Subdivisions within a superclass (e.g., Pants, Tops).
3. **Type**: General physical form (e.g., Jeans, T-Shirts).
4. **Variant**: Specific variations (e.g., Distressed Jeans).
5. **Style**: Fine-grained descriptors (e.g., Graphic Print, Embroidered).
![ba35abb2-1c13-4b1b-98a5-d7b9204344d0](https://github.com/user-attachments/assets/d00de66c-8494-48cb-beaf-bb6c6f1b5827)

#### Features:
- **Adaptive Structure**: Flexible for growth and expansion.
- **Dynamic Classes**: AI-driven creation of new categories.
- **Cross-Aware Feature**: Enables cross-category comparisons (e.g., Dhoti vs. Jeans under "Bottom-wear").

#### Constraints and Extensibility:
- Dynamically generates new classes if no match exists.
- Requires human verification for updates to ensure accuracy.

---

## User Interface

### 1. **Query Page**:
- Filter and retrieve specific products based on ontology attributes.
- Display relationships between selected products and other entities.
![Screenshot (226)](https://github.com/user-attachments/assets/2ce3809a-098d-451d-9280-470b237a3b89)

### 2. **Trend Analysis Page**:
- Highlights trending products, styles, and categories.
- Tracks emerging trends based on patterns across social media.
![Screenshot (227)](https://github.com/user-attachments/assets/959d993f-4033-47b1-ad7a-ebdf2af638d8)

### 3. **Verification Page**:
- Human-in-the-loop validation to ensure ontology accuracy.
- Verified updates are automatically uploaded to Neo4j.
  ![Screenshot 2025-01-05 183829](https://github.com/user-attachments/assets/3eaf3b01-30b2-4e4d-a14a-c92095509897)

### 4. **Ontology Page**:
- Visualize hierarchical structures of fashion entities.
- Explore relationships and connections in an interactive panel.
![Screenshot (230)](https://github.com/user-attachments/assets/70d80644-09d8-48eb-b372-52df6e5879f2)
![Screenshot (229)](https://github.com/user-attachments/assets/7618087a-a202-4fcb-aa2a-f89d03a49bc9)
![Screenshot (228)](https://github.com/user-attachments/assets/94df344b-ef46-4c0c-a1a6-6c2e83007569)

### 5. **Social Trends Page**:
- Monitors top celebrity posts on platforms like Instagram.
- Extracts features and updates the ontology for statistical assessment.
![Screenshot 2025-01-05 183741](https://github.com/user-attachments/assets/0c7f2a66-4074-4e6a-8662-af517f810637)

---

## Data Storage and Performance

### Neo4j AuraDB
- **Two Databases**:
  - **Ontology Database**: Stores hierarchical structures and relationships.
  - **Product Database**: Contains product data with 80k+ data points.
- **Optimizations**:
  - Graph-based structure for fast retrieval.
  - Interactive visualization tools integrated with Neo4j.
 
  
![hippo](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWl1dDEyeHRuZGZhMmh5cml6aHUzb2E0cnk0M2todHc0bzJmbnIxayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7s7Vf07bdL1eQQ1vUQ/giphy.gif)


---

## Trend Analysis Engine

### Workflow:
1. Monitor top 100 celebrities' latest posts on social media (Instagram).
2. Extract product features using AI models.
3. Submit extracted features to verification.
4. Verified features are added to the ontology.
5. Analyze trends by detecting repeated patterns.

### Example:
- If multiple celebrities wear distressed jeans, the engine identifies it as a trend.
- Public interest analysis confirms its relevance in fast fashion.

---

## Why Our Solution Stands Out

### Key Advantages:
- **Scalability**: Handles large datasets with high efficiency.
- **Adaptability**: Dynamically evolves with trends.
- **Accuracy**: Ensures precise feature extraction and ontology updates.
- **Human-in-the-Loop**: Combines AI efficiency with expert oversight.

### Performance Metrics:
- **Model Accuracy**:
  - Image-to-Text: 92% feature extraction accuracy.
  - Text-to-Ontology: 95% class matching accuracy.
- **Database Query Performance**:
  - Sub-100ms response time for complex queries.
  - Scales seamlessly to millions of records.

---

## Take a look for yourself [here](https://stylumia-fashion.streamlit.app/) 
---

## Technologies Used

- **Neo4j**: Graph database for ontology storage and retrieval.
- **Streamlit**: Intuitive frontend for user interactions.
- **LLMs**: For feature extraction and trend analysis.
- **PyVis**: Visualization of relationships and hierarchies.
- **Python**: Core programming language for backend and model pipelines.

---

## How to Run the Solution Locally

### Prerequisites:
1. Python 3.9 or higher.
2. Neo4j AuraDB credentials.
3. Required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/ImJericho/stylumia-nxt
   ```
2. Set up Neo4j credentials in `.env`:
   ```env
   NEO4J_URI=bolt://<your-neo4j-uri>
   NEO4J_USER=<your-username>
   NEO4J_PASSWORD=<your-password>
   OLLAMA_URL=<your-ollama-url> // where all the fine-tunned model are hosted
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
4. Access the application at `http://localhost:8501`.

---

## Team

- **Shashvat Jain** (IIT Dhanbad)
- **Vivek Patidar** (IIT Dhanbad)
- **Pranay Pandey** (IIT Dhanbad)

---

## Our Efforts

* **Data prepration for model fine tunningtps** : [Kaggle Notebook](https://www.kaggle.com/code/vivecode/stylumia-ontology-generation-script)
* **Model-training**: [Kaggle Notebook](https://www.kaggle.com/code/vivecode/stylumia-model-training)
* **Data prepration for model fine tunning** : [Jupyter Notebook](https://github.com/ImJericho/stylumia-nxt/blob/main/text_model/data_processing.ipynb)
*
* * **Checkout the deployed frontend with limitted feature** : [(https://stylumia-fashion.streamlit.app)

