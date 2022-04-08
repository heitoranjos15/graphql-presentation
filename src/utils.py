import json

def filter_by_options(content, category=None, last=None, top=None):
    print(category)
    if category:
        content = list(filter(lambda video: video.get('video').get('category') == category, content))
    if top: 
        return content[:last]
    if last:
        content.reverse()
        return content[:last]
    return content

def load_data(entity = None):
    with open("./database/data.json", 'r') as file:
        file_data = file.read()
    
    database = json.loads(file_data)
    if entity:
        return database.get(entity)
    return database
