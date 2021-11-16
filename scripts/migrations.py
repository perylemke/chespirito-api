import json

from pymongo import MongoClient
from decouple import config

MONGO_URI = config('DB_URI', default='localhost', cast=str)
client = MongoClient(MONGO_URI)


def insert_data_general():
    db_general = client['generaldb']

    with open('./migrations/general/actors.json') as actors_file:
        file_data = json.load(actors_file)

    actors_data = db_general.actors.insert_many(file_data)
    print(actors_data.inserted_ids)

    with open('./migrations/general/actresses.json') as actresses_file:
        file_data = json.load(actresses_file)

    actresses_data = db_general.actors.insert_many(file_data)
    print(actresses_data.inserted_ids)


def insert_data_chaves():
    db_chaves = client['chavesdb']

    with open('./migrations/general/episodes1972.json') as episode_file:
        file_data = json.load(episode_file)

    episodes_data = db_chaves.actors.insert_many(file_data)
    print(episodes_data.inserted_ids)


if __name__ == '__main__':
    insert_data_general()
    insert_data_chaves()
