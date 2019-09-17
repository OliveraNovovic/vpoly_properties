import osm_poi
from osm_poi import poi_density_read


def main():
    #data folder: /home/olivera/Documents/data
    for i in range(1, 314):
        poi_density = poi_density_read(i)
        #avg_pw_dist =

if __name__=='__main__':
    main()