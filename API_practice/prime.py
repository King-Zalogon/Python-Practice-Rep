import requests

base_url = 'http://dogs.magnet.cl/api/v1/auth' # The APIs URL http://dogs.magnet.cl/api/v1/auth/
get_url = 'http://dogs.magnet.cl/api/v1/breeds/'

headers = {'Authorization': 'pl0erGQb'}

params = {'param1': 'value1', 'param2': 'value2'}

response = requests.post(base_url, headers=headers)

try:
    response = requests.get(get_url, headers=headers)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print('Request failed:', e)

if response.status_code == 200:
    data = response.json()
    # Process the response data
    print(data)
else:
    print('Request failed with status code:', response.status_code)


# for item in data:
#     print(item['name'])

    