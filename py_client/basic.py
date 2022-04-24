import requests

endpoint = "http://localhost:8000/api/"

# get_response = requests.get(endpoint, params={"test":"matthew"}, json={"query": "Hello, world!"})
get_response = requests.post(endpoint, json={"metthew":"is_it key really?", "title": "Abc123", "content": "Hello world", "price": "100"})

print(get_response.json())