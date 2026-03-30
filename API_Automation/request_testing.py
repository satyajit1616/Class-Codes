import requests
base_url = "https://jsonplaceholder.typicode.com"
#get methods
'''def get_all_data():
    url = base_url+'/posts'
    response = requests.get(url)
    data = response.json()

    for i in data:
        if i['userId']==1 and i['id']==3:
            print(i)
print(get_all_data())'''
#get method fetch the perticular data
'''def get_perticular_data(num):
    url = base_url + '/posts'
    response = requests.get(url, params={'id': num})
    if response.status_code == 200:
        return response.json()

print(get_perticular_data(3))'''
#create post method
'''def create_post():
url = base_url+'/posts'
headers= {'Content-Type': 'application/json'}
payload = {
"userId": 11,
"title": "Hello Iran",
"body": "Khamini All Huasar"
}
response = requests.post(url,headers=headers,json=payload)
assert response.status_code == 201
return response.json()
print(create_post())'''
#update with put method
def update_with_put(id):
    url = base_url+'/posts'+f'/{id}'
    headers= {'Content-Type': 'application/json'}
    payload = {
                "id":id,
                "title": "Hello Iran",
                "body": "Khamini All Huasar"
                }
    response = requests.put(url,headers=headers,json=payload)
    print(response.status_code)
    return response.json()
    if response.status_code == 200:
        return response.json()
print(update_with_put(78))
'''#delete method for particular data
def delete_perticular_data(num):
    url = base_url + f'/posts/{num}'
    response = requests.delete(url)

    if response.status_code == 200:
        return response.status_code

print(delete_perticular_data(3))'''

#update with patch method (partial update)
def update_with_patch(id):
    url = base_url + f'/posts/{id}'
    headers = {'Content-Type': 'application/json'}
    payload = {

        "body": "Steel"
    }

    response = requests.patch(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()

print(update_with_patch(3))