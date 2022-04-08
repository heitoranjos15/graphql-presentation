import json
import random
from faker import Faker
fake = Faker()

categories = ['food', 'news', 'kids', 'sport']

def generate_customers():
    customers = list()
    for i in range(10):
        customers.append({
            'id': i+1,
            'name': fake.name(),
            'email': fake.email(),
            'address': fake.address(),
            })
    return customers

def generate_videos(customers):
    videos = list()
    for i in range(100):
        videos.append({
            'id': i+1,
            'name': f'Video {i}',
            'description': fake.text(),
            'author_id': random.choice(customers)['id'],
            'created_at': fake.date(),
            'duration': random.randint(1, 60),
            'category': random.choice(categories),
            'views': random.randint(50, 1000),
            'likes': random.randint(50, 1000),
            })
    return videos

def generate_comments(customers, videos):
    comments = list()
    for i in range(1000):
        comments.append({
            'id': i+1,
            'text': fake.text(),
            'author_id': random.choice(customers)['id'],
            'video_id': random.choice(videos)['id'],
            'likes': random.randint(1, 1000),
            })
    return comments

def generate_recommendations(customers, videos):
    recommendations = list()
    for i in range(1000):
        recommendations.append({
            'customer_id': random.choice(customers)['id'],
            'video_id': random.choice(videos)['id'],
            'video': random.choice(videos),
            })
    return recommendations

def generate_customer_views(customers, videos):
    views = list()
    for i in range(1000):
        views.append({
            'customer_id': random.choice(customers)['id'],
            'video': random.choice(videos),
            })
    return views


def generate_content():
    customers = generate_customers()
    videos = generate_videos(customers)
    comments = generate_comments(customers, videos)
    recommendations = generate_recommendations(customers, videos)
    views = generate_customer_views(customers, videos)
    return { 
            'customers': customers,
            'videos': videos,
            'comments': comments,
            'recommendations': recommendations,
            'views': views,
            }


with open("database/data.json", "w") as file1:
    database_content = generate_content()
    file1.write(json.dumps(database_content))
