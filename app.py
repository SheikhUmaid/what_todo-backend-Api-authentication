import requests
# dict to json
import json



def get_data(username, password):
    url = 'http://127.0.0.1:8000/login/'
    data = {
        'username': username,
        'password': password
    }
    response = requests.post(url, data=data)
    print(response.json()['token'])

    todos = requests.get('http://127.0.0.1:8000/api/', headers={'Authorization': 'Token ' + response.json()['token']})
    print(todos.json())

def post_data(username, password):
    url = 'http://127.0.0.1:8000/login/'
    dataa = {
        'username': username,
        'password': password
    }
    response = requests.post(url, data=dataa)
    print(response.json()['token'])

    todo ={
        "todo": "by Python App Request",
        "completed": False
    }
    todo_to_upload = requests.post(
        'http://127.0.0.1:8000/api/',
        headers={'Authorization': 'token ' + response.json()['token'], 'Content-Type': 'application/json'},
        data= json.dumps(todo))
    print(todo_to_upload.json())

def delete_data(username, password):
    url = 'http://127.0.0.1:8000/login/'
    dataa = {
        'username': username,
        'password': password
    }
    response = requests.post(url, data=dataa)
    print(response.json()['token'])

    url = 'http://127.0.0.1:8000/delete_api/24'
    response = requests.delete(url, headers={'Authorization': 'token ' + response.json()['token']})
    print(response.json())

# post_data("admin", "admin")
# get_data("admin", "admin")
delete_data("admin", "admin")