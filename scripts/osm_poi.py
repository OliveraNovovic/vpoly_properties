

def poi_density_read(i):
    data = "/home/olivera/Documents/data"
    osm_poi_file = data + "/osm_points_per_vornoi_poly.csv"
    with open(osm_poi_file, 'r') as f:
        lines = f.readlines()[1:] #skip the header
        for line in lines:
            el = line.split(",")
            cid = int(el[0])
            area_poly = float(el[1])
            osm_poi_num = int(el[2])
            poi_density = float(el[3])
            if cid == i:
                return poi_density
            else:
                print("No poly id: " + i + " in data!")
                continue