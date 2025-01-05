import sqlite3
import csv 

def create_db_file(db_path, table_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE {table_name} 
             (entity_id INTEGER PRIMARY KEY AUTOINCREMENT, image_url TEXT, image_caption TEXT)''')
    conn.commit()
    conn.close()

def insert_into_db(db_path, table_name, image_url, image_caption):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table_name} (image_url, image_caption) VALUES ('{image_url}', '{image_caption}')")
    conn.commit()
    conn.close()

def insert_csv_to_db(db_path, csv_path):
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i >= 1:
                insert_into_db(db_path, 'ingested_data', row[0], '')


def main():
    db_path = '/Users/vivek/Drive E/Hackathons/Stylumia/stylumia-nxt/backend/data_ingestion_engine/ingested_data.db'
    csv_path = '/Users/vivek/Drive E/Hackathons/Stylumia/stylumia-nxt/backend/data_ingestion_engine/ingested_data.csv'

    create_db_file(db_path, 'ingested_data')
    insert_csv_to_db(db_path, csv_path)


if __name__ == '__main__':
    main()