from math import dist
import numpy as np
from importar_excel import init_long_list, init_latit_list, end_long_list, end_latit_list, distance_list, route_name, vor_name_end, vor_name_ini
from distance_coordinates import Dist_Coord


i = 0
dist = 9999999999999
coord_vor = [0,0]
vor = 0

apt_lat = 39.862625
apt_lon = 4.220085

for n in init_latit_list:
    if Dist_Coord(init_latit_list[i], apt_lat, init_long_list[i], apt_lon) <= dist:
        
        dist = Dist_Coord(init_latit_list[i], apt_lat, init_long_list[i], apt_lon)
        coord_vor = [init_latit_list[i],init_long_list[i]]

        vor = i

        i += 1
    else: i +=1 

print(vor_name_ini[vor])