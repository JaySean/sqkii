import json


def get_hist_site():

    with open('hist_site/hist_site.json') as json_file:
        return json.load(json_file)