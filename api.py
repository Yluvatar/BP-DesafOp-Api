import requests
import json

url = 'https://reqres.in/api/users'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def imprime_mensaje(mensaje):
    print("\n", mensaje.json(), "\n")
    print(mensaje.status_code)


users_data = requests.get(url)

print("\n", json.dumps(users_data.json(), sort_keys=True, indent=2), "\n")
print(users_data.status_code)

data = {
    'nombre': 'Ignacio',
    'trabajo': 'Profesor'
}

created_user = requests.post(url, json=data, headers=headers)

imprime_mensaje(created_user)

data = {'residence': 'Zion'}

updated_user = requests.put(url + "/username=morpheus", json=data, headers=headers)

imprime_mensaje(updated_user)

deleted_user = requests.delete(url + "/username=Tracey")

print("\n", deleted_user.status_code, "\n\n")
