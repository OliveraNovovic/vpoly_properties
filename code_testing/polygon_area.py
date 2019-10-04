
from shapely.geometry import Polygon
from shapely.ops import transform
from functools import partial
import pyproj


def main():
    '''
    POLYGON((9.2771075744521756 45.3999743526693678, 9.2720152069542259 45.4082706791823512,
    9.2736420360315748 45.4600856784859104, 9.2855392215288575 45.4720815063955612,
    9.2927932086663390 45.4482628050353838, 9.2808850142363166 45.4039329550894664,
    9.2771075744521756 45.3999743526693678))
    '''

    polygon = Polygon([[9.2771075744521756, 45.3999743526693678], [9.2720152069542259, 45.4082706791823512],
    [9.2736420360315748, 45.4600856784859104], [9.2855392215288575, 45.4720815063955612],
    [9.2927932086663390, 45.4482628050353838], [9.2808850142363166, 45.4039329550894664],
    [9.2771075744521756, 45.3999743526693678]])

    convex_hull_4326 = polygon.convex_hull

    project = partial(
        pyproj.transform,
        pyproj.Proj(init='EPSG:4326'),
        pyproj.Proj(init='EPSG:32632'))

    poly_tranform = transform(project, polygon)
    convex_hull = poly_tranform.convex_hull
    chull_area = convex_hull.area
    chull_perimeter = convex_hull.length
    chull = [chull_area, chull_perimeter]
    print(chull)








if __name__=='__main__':
    main()