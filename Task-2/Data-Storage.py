import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['Al-Mayadeen']
collection = db['Articles']

json_files = [
    'articles_2024_01.json',
    'articles_2024_02.json',
    'articles_2024_03.json',
    'articles_2024_05.json',
    'articles_2024_06.json',
    'articles_2024_07.json',
    'articles_2024_08.json',
]
for file in json_files:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        collection.insert_many(data)

print("All data inserted successfully.")
