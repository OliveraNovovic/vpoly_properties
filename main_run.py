import osm_poi
from osm_poi import poi_density_read
from avgpwdist_diameter_gyration_chull import adgc
from avg_pw_dist_diameter_gyration_update import adg2
from intersection import intersect
from community_coverage_overall import comm_coverage
import pandas as pd
import sys


def main():
    sys.setrecursionlimit(1500)
    print(sys.getrecursionlimit())
    pd.set_option('display.max_columns', 999)
    cols = ["poly_name", "poi_density", "avg_pw_dist", "diameter", "gyration",
            "chull_area_km2", "chull_perim_km", "mean_intersec_area",
            "st_dev_intersec_area", "mean_jaccard_sim", "st_dev_jaccard_sim"]
    vpoly_properties_df = pd.DataFrame(columns=cols)
    #data folder: /home/olivera/Documents/data
    for i in range(1, 314):
        print("working on poly ", str(i))
        name = "poly_" + str(i)
        poi_density = poi_density_read(i)
        #calculated when central point is mean coord
        avg_pw_dist = adgc(i)
        avg_dist = avg_pw_dist[0]
        diameter = avg_pw_dist[1]
        gyration = avg_pw_dist[2]

        chull_area_km2 = avg_pw_dist[3]
        chull_perim_km = avg_pw_dist[4]
        intersec_res = intersect(i)
        intersec_st_dev = intersec_res[0]
        intersec_mean = intersec_res[1]
        jaccard_st_dev = intersec_res[2]
        jaccard_mean = intersec_res[3]
        #calculated when central point is vpoly centroid
        avg_pw_dist_2 = adg2(i)
        avg_dist2 = avg_pw_dist_2[0]
        diameter2 = avg_pw_dist_2[1]
        gyration2 = avg_pw_dist_2[2]

        comm_coverage_overall = comm_coverage(i)
        coverage_area_km2 = comm_coverage_overall[0]
        coverage_avg_area_km2 = comm_coverage_overall[1]

        new_row = {'poly_name': name, 'poi_density': poi_density, 'avg_pw_dist': avg_dist,
                   'diameter': diameter, 'gyration': gyration, 'chull_area_km2': chull_area_km2,
                   'chull_perim_km': chull_perim_km, 'mean_intersec_area': intersec_mean,
                   'st_dev_intersec_area': intersec_st_dev, 'mean_jaccard_sim': jaccard_mean,
                   'st_dev_jaccard_sim': jaccard_st_dev,
                   'avg_pw_dist2': avg_dist2, 'diameter2': diameter2, 'gyration2': gyration2,
                   'coverage_area_km2': coverage_area_km2, 'coverage_avg_area_km2': coverage_avg_area_km2}
        vpoly_properties_df = vpoly_properties_df.append(new_row, ignore_index=True)

    #print(vpoly_properties_df)
    nonull = vpoly_properties_df.fillna(0)
    nonull.to_pickle("/home/olivera/Documents/data/vpoly_properties_update.pkl")




if __name__=='__main__':
    main()