import requests
import json

def pprint(json_data):
    for json in json_data['@graph']:
        if json['schema:creator']:
            schema_creater = json['schema:creator']
            creater_name_ja = schema_creater['schema:name'][0]['@value']
            creater_name_en = schema_creater['schema:name'][1]['@value']
            # creater_birth_date = schema_creater['schema:birthDate']['@value']
            # creater_death_date = schema_creater['schema:deathDate']['@value']
        
            print(creater_name_ja)
            print(creater_name_en)
            # print(creater_birth_date)
            # print(creater_death_date)
            print('================================')

if __name__ == '__main__':
    url = 'https://museumcollection.tokyo/works/?keyword=japanese&output=json'
    response = requests.get(url)

    if response.status_code == 200:
        json_data = json.loads(response.text)
        # json_data = response.json()
        pprint(json_data)
    else:
        print('Error:', response.status_code)
