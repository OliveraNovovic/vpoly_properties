import os
import numpy as np
import geopandas as gpd
import matplotlib
import json

def vpoly_area(cid_array):
    vpoly_clusters_area = 0.0
    for c in cid_array:
        #Milano Vornoi polygons network
        vornoi = "/home/olivera/Documents/data/milano-vornoi-network-EPSG32632.geojson"
        with open(vornoi, 'r') as f:
            data = json.load(f)
            for feature in data['features']:
                v_cid = feature['properties']['cid']
                v_area = feature['properties']['area']
                #v_perimetar = feature['properties']['perimeter']
                #v_poly_geom = feature['geometry']
                if v_cid == c:
                    #print(v_cid, v_area)
                    vpoly_clusters_area += v_area
    avg_vpc_area = vpoly_clusters_area/len(cid_array)
    return vpoly_clusters_area, avg_vpc_area



def comm_coverage(i):
    # for each vornoi polygon we want to put all of it's (unique)cid's in one array
    cid_array = []

    vpoly = "vpoly_" + str(i)
    folder_path = "/home/olivera/Documents/data/vpoly_single_clusters/"

    date = ["nov01", "nov02", "nov03", "nov04", "nov05", "nov06", "nov07", "nov08",
            "nov09", "nov10", "nov11", "nov12", "nov13", "nov14", "nov15",
            "nov16", "nov17", "nov18", "nov19", "nov20", "nov21", "nov22",
            "nov23", "nov24", "nov25", "nov26", "nov27", "nov28", "nov29",
            "nov30", "dec01", "dec02", "dec03", "dec04", "dec05", "dec06",
            "dec07", "dec08", "dec09", "dec10", "dec11", "dec12", "dec13",
            "dec14", "dec15", "dec16", "dec17", "dec18", "dec19", "dec20",
            "dec21", "dec22", "dec23", "dec24", "dec25", "dec26", "dec27",
            "dec28", "dec29", "dec30", "dec31", "jan01"]

    for d in date:
        vpoly_cluster = folder_path + vpoly + "_" + d + ".geojson"
        geojson_file = gpd.read_file(vpoly_cluster)
        cid = geojson_file['cid']

        for c in cid:
            if c not in cid_array:
                cid_array.append(c)

    vpc_area = vpoly_area(cid_array)[0]
    avg_vpc_area = vpoly_area(cid_array)[1]
    res = (vpc_area/1000000, avg_vpc_area/1000000)
    return res


