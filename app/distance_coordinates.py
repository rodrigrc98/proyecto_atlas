from math import radians, sin, cos, atan2, sqrt

def Dist_Coord (init_lat, end_lat, init_long, end_long):

    #coordenadas y paso a radianes

    lat1 = radians(init_lat)
    lat2 = radians(end_lat)
    lon1 = radians(init_long)
    lon2 = radians(end_long)

    R = 6371e3; # Radio de la tierra en metros

    #diferencia de lats y longs

    lat_dif = (lat2-lat1)
    lon_dif = (lon2-lon1)

    #formulas de la distancia entre dos puntos de una superficie esferica

    a = sin(lat_dif/2) * sin(lat_dif/2) + cos(lat1) * cos(lat2) *sin(lon_dif/2) * sin(lon_dif/2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    d = R * c; # en metros

    return(d)

