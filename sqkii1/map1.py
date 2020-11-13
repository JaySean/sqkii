import gmplot
import joblib
import requests
import json
from shapely.geometry import Point, Polygon
import os
from api_token import API_KEY
from sqkii1.supermarket.supermarket import get_supermarket
from sqkii1.mrt.mrt import get_mrt
from sqkii1.town.town import get_town
from sqkii1.hist_site.hist_site import get_hist_site


def supermarket(gmap, supermarket_list):

    # Remove supermarkets without a geographic coodinate
    supermarket_list = list(filter(None, list(supermarket_list.values())))

    # Create list of latitudes and longitudes
    supermarkets_lat, supermarkets_lng = zip(*list(supermarket_list))

    # Plot radius for each supermarket
    gmap.scatter(supermarkets_lat, supermarkets_lng, color='#3B0B39', size=500, marker=False)

    return gmap


def mrt(gmap, mrt_list):

    # Draws a marker for each MRT station.
    # The marker is red if the station is less than 40 mins from Changi Airport.
    # The marker is green if the station is at least 40 mins from Changi Airport.

    for mrt_name, (mrt_loc, mrt_time) in mrt_list.items():

        # Sort into < 40 mins (red) and >= 40 mins (green) and draw marker
        marker_colour = 'red' if mrt_time < 40 else 'green'
        gmap.marker(mrt_loc[0], mrt_loc[1], color=marker_colour, title=mrt_name)

    return gmap


def town(gmap, town_list, hist_site_list):

    def get_center(polygon):
        lats, lngs = list(zip(*polygon))
        # Find the center of a polygon shape by finding the center of its bounding rectangle
        lat_center = min(lats) + (max(lats) - min(lats)) / 2
        lng_center = min(lngs) + (max(lngs) - min(lngs)) / 2
        return lat_center, lng_center

    # Plot each historical historical site as a marker and create a Shapely Point
    site_points = []
    for hist_site in hist_site_list.items():
        gmap.marker(hist_site[1][0], hist_site[1][1], color='gray', title=hist_site[0])
        site_points.append(Point(hist_site[1]))

    # Plot towns with a historical site
    for town_name, town_loc in town_list.items():
        # Check if town contains a historical site
        for site_point in site_points:
            if Polygon(town_loc).contains(site_point):
                # Plot town polygon shape and centre of town marker
                gmap.polygon([town_loc], color='cornflowerblue', edge_width=3)
                lat_center, lng_center = get_center(town_loc)
                gmap.marker(lat_center, lng_center, color='cornflowerblue', title=town_name)
                break

    return gmap


def main():

    # Plot Google Map centred on Singapore
    gmap = gmplot.GoogleMapPlotter(1.3521, 103.8198, 12, apikey=API_KEY)

    # # Load supermarket data
    supermarket_list = get_supermarket()
    mrt_list = get_mrt()
    town_list = get_town()
    hist_site_list = get_hist_site()

    # Visualise each of the 3 clues
    gmap = mrt(gmap, mrt_list)
    # gmap = town(gmap, town_list, hist_site_list)
    # gmap = supermarket(gmap, supermarket_list)

    # Answer: 45 Jurong West Street 42
    gmap.marker(1.3518808, 103.7168932, color='white', title='Sqkii')

    # Draw the map:
    gmap.draw('map1.html')


if __name__ == "__main__":
    main()
