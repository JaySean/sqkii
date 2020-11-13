from pykml import parser
import os
import json
import requests
from api_token import API_KEY


def get_mrt():
    if not os.path.isfile('mrt/mrt.json'):

        # Open and parse kml file
        with open('mrt/master-plan-2019-rail-station-name-layer-kml.kml') as f:
            doc = parser.parse(f).getroot()

        mrts = {}

        # KML file stores MRT location either as a Point or Line
        # For each MRT, add the name and coordinate point to dict
        for e in doc.Document.Folder.Placemark:
            mrt_name = str(e.name)
            if getattr(e, 'Point', None) is not None:
                mrt_loc = tuple(map(float, str(e.Point.coordinates).split(",")[1::-1]))
            if getattr(e, 'LineString', None) is not None:
                lines = [tuple(map(float, line.split(",")[1::-1])) for line in str(e.LineString.coordinates).split(" ")]
                # Take the center of the line as the coordinate point
                lines = [sum(line) / len(line) for line in list(zip(*lines))]
                mrt_loc = tuple(lines)
            time = get_time(mrt_loc)
            mrts[mrt_name] = mrt_loc, time
            print(mrts[mrt_name])

        # Save to file
        with open('mrt/mrt.json', 'w') as outfile:
            json.dump(mrts, outfile)

    with open('mrt/mrt.json') as json_file:
        return json.load(json_file)


def route_time(org, dst):
    # Queries Google Distance Matrix API to get the travel time between two locations
    times = requests.get(
        'https://maps.googleapis.com/maps/api/distancematrix/json?origins={},{}&destinations={},{}'
        '&mode=transit&transit_mode=train&key={}'.format(org[0], org[1], dst[0], dst[1], API_KEY)
    )
    times = json.loads(times.text)
    return times


def get_time(mrt_loc):
    changi_airport = (1.35747897447696, 103.98788356959)

    # Get the travel time to MRT station
    t = route_time(changi_airport, (mrt_loc[0], mrt_loc[1]))

    # Parse route time into the format "({} hour(s)) {} min(s)"
    t = t["rows"][0]["elements"][0]["duration"]["text"]

    # Convert route time into minutes
    if "hour" in t:
        if "hours" in t:
            hours, mins = t.split("hours")
        else:
            hours, mins = t.split("hour")
    else:
        hours = 0
        mins = t

    if "mins" in t:
        mins = mins.split("mins")[0]
    else:
        mins = mins.split("min")[0]

    t = int(hours) * 60 + int(mins)

    return t
