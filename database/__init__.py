import json

def load_data(data_type = None):
    with open("./database/data.json", 'r') as file:
        file_data = file.read()
    
    database = json.loads(file_data)
    if data_type:
        return database.get(data_type)
    return database

