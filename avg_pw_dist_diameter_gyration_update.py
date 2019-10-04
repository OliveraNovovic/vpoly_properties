import numpy as np
from geopy.distance import geodesic
import json

def vpoly_centroid(i):
    vpoly_centroids = open("/home/olivera/Documents/data/milano-vornoipoly-centroids-EPSG-4326.geojson", 'r')
    data = json.load(vpoly_centroids)
    for feature in data['features']:
        v_cid = feature['properties']['cid']
        lon = feature['properties']['xcoord']
        lat = feature['properties']['ycoord']
        if v_cid == i:
            #print("vpoly central point ", lon, lat)
            return lat, lon    #geopy uses lat, lon order
    vpoly_centroids.close()



def pw_dist(a, b, da):
    dst = geodesic(a, b).meters
    da.append(dst)
    return da


def adg2(i):
    vpoly = "vpoly_" + str(i) + ".txt"
    file_path = "/home/olivera/Documents/data/vpoly_centroids/" + vpoly
    file = open(file_path, 'r')
    b = vpoly_centroid(i)
    dst_array = []
    #points = []
    lines = file.readlines()
    for line in lines:
        el = line.split(" ")
        lon = float(el[1][1:])
        lat = float(el[2][:-2])
        a = (lat, lon)      #geopy uses order lat, lon
        #point = (lon, lat)  #shapely uses order lon, lat
        dist_array = pw_dist(a, b, dst_array)
        #points.append(point)
    file.close()

    avg = np.mean(dist_array)
    diameter = np.max(dist_array)
    gyration = np.std(dist_array)

    res = (avg, diameter, gyration)
    return res




