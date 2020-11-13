import requests
import pandas as pd
import json
import os


def get_supermarket():

    if not os.path.isfile('supermarket/supermarket.json'):

        # Read dataset csv into pandas dataframe
        df = pd.read_csv('supermarket/list-of-supermarket-licences.csv')
        licenses = df['licence_num'].values.tolist()
        postal_codes = df['postal_code'].values.tolist()

        supermarkets = {}

        # Covert each postal code into a geographic coordinate (latitude, longitude)
        for license, postal_code in zip(licenses, postal_codes):

            coord_url = f'https://developers.onemap.sg/commonapi/search?searchVal={postal_code}' \
                        f'&returnGeom=Y&getAddrDetails=Y&pageNum=1 '

            coord_req = requests.get(coord_url)

            if coord_req.ok and coord_req.json() != 'The request you have just typed is not allowed!':
                coord_json = coord_req.json()
            else:
                coord_json = None

            if coord_json and coord_json['results']:
                lat, lng = coord_json['results'][0]['LATITUDE'], coord_json['results'][0]['LONGITUDE']

                supermarkets[license] = (lat, lng)

        # Save to file
        with open('supermarket/supermarket.json', 'w') as outfile:
            json.dump(supermarkets, outfile)

    with open('supermarket/supermarket.json') as json_file:
        return json.load(json_file)

