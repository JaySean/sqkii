from pykml import parser
import os
import json


def get_town():

    if not os.path.isfile('town/town.json'):

        # Open and parse kml file
        with open('town/planning-boundary-area.kml') as f:
            doc = parser.parse(f).getroot()

        towns = {}

        for e in doc.Document.Folder.Placemark:
            name = str(e.ExtendedData.SchemaData.SimpleData[0])
            polygon_str = str(e.Polygon.outerBoundaryIs.LinearRing.coordinates)
            polygon = polygon_str.split(" ")
            polygon = [tuple(map(float, point.split(",")[1::-1])) for point in polygon]
            towns[name] = polygon

        # Save to file
        with open('town/town.json', 'w') as outfile:
            json.dump(towns, outfile)

    with open('town/town.json') as json_file:
        return json.load(json_file)

