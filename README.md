# stylumia-nxt
Our solution for the hackathon



MODEL BUILDING:
	TEXT2TEXT MDOEL    : DESCRIPTION+FEATURE_MAP+.. => STYLE_ATTRIBUTES
	IMAGE2TEXT MDOEL   : IMAGE OF THE PRODUCT => STYLE_ATTRIBUTES
	ATTRIBUTE SELECTION MODEL/ONTOLOGY CREATION MDOEL :   STYLE_ATTRIBUTES => ONTOLOGY MAPPING (REQURE THE NEO4J INTEGRATION SUPPORT)

NEO4J BUILDING:
	CREATE AN ONTLOGY MAP/GRAPH IN THE NEO4J    : MANNUAL UPDATION
	CREATE A DATASET IN THE NEO4J 				: AUTOMATED CREATION 
	CREATE A QUERY / AI SIMULATION ENGINE		: RUN QUERIES 

INSTAGRAM CELEBERTIES EXTRACTION ENGINE:
	MAKE LIST OF 100 CELEBS
	EXTRACT THE IMAGE FROM IG POST OF THOSE CELEBS
	ANALYSE THE CLOTHING
	MAP THAT CLOTHING STYLE TO THE ONTOLOGY -> UPDATE THE ONTOLOGY (SUGGESTIONS ONLY)
	TREND ANALYSIS ENGINE:
		COMMENT SCRAPE   :SCRAP THE COMMENTS AND FIND THE SENTIMENT
		FREQUENCY ANALYSIS : BASED ON THE RECENT SUGGESTION IN THE ONTOLOGY

INTEGRATION:
	NA	






Bathroom -> Features list all good, Attributes all good
Shirts -> Features list all null, Attributes all good
Tshirts -> Features list all null, Attributes all good
Watches -> Features list 80%good, Attributes all good
Saree -> Features list 5% good, Attributes 10% good
Kurtis -> Features list 0% good, Attributes 0% good
Jeans -> Features list all null, Attributes all good
Earring -> Features 95%good, Attributes 95% good
Dresses -> Features all good
Sneakers -> Features list all null, Attributes all good



Fashion Ontology

1. Garment
	•	Category
	•	Jeans
	•	Shirts
	•	Tops
	•	Skirts
	•	Outerwear
	•	Pants

2. Attributes
	•	General Properties
	•	Color
	•	Size
	•	Style
	•	Pattern Type
	•	Fit Type
	•	Concept
	•	Features
	•	Material Properties
	•	Material
	•	Composition
	•	Fabric
	•	Lining
	•	Coating
	•	Design & Construction
	•	Length
	•	Waist Line
	•	Closure Type
	•	Neckline
	•	Sleeve Length
	•	Sleeve Type
	•	Hem Shaped
	•	Pockets
	•	Belt
	•	Placket
	•	Special Design
	•	Jeans Style
	•	Bottom Type
	•	Waist Rise
	•	Detailed Description
	•	Special Features

3. Functional Attributes
	•	Care Instructions
	•	Lined for Added Warmth
	•	Sheer
	•	Temperature Suitability
	•	Number of Pieces
	•	Chest Pad

4. Contextual Properties
	•	Imported
	•	Body Type
	•	Concept


Product Name  (=Node)
Properties:
	k,v (value=Node) (key=relation)