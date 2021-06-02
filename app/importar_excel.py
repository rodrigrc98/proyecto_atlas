import pandas as pd
import numpy as np
from .distance_coordinates import Dist_Coord

# importamos excel en un dataframe
df = pd.read_excel(r'C:\Users\Rodrigo Garcés\Documents\flask_app\app\Data\LE_Amdt_A_2021_03_ENR_3_1_en.xls')

# extraemos las columnas del excel que nos interesan en arrays

#nombres de rutas

route_name = np.array(df['DESIGNATOR_TXT'])

#nombbres de vor correspondiente a cada ruta

vor_name_ini = np.array(df['PUNTO_INICIO'])     
vor_name_end = np.array(df['PUNTO_FINAL'])      

#valores iniciales/finales de coordenadas

init_long = np.array(df['COOR_LON_INICIO'])
init_latit = np.array(df['COOR_LAT_INICIO'])

end_latit = np.array(df['COOR_LAT_FINAL'])
end_long = np.array(df['COOR_LON_FINAL'])


#precarga de listas

init_long_list = []
init_latit_list = []
end_long_list = []
end_latit_list = []
distance_list = []

# contador para bucles
i = 0


#bucles para manipular los datos y obtener las listas finales

for n in init_long:
   
    a = init_long[i]
    signo = -1 if a[-1]=='W' else 1
    horas = int(a[:3])
    minu = str('0.' + str(a[3:-1]))
    init_long_list.append(round((horas + float(minu))*signo,5))

    i += 1

i = 0

for n in init_latit:
   
    a = init_latit[i]
    signo = -1 if a[-1]=='S' else 1
    horas = int(a[:2])
    minu = str('0.' + str(a[2:-1]))
    init_latit_list.append(round((horas + float(minu))*signo,5))
    
        
    i += 1

i = 0

for n in end_long:
   
    a = end_long[i]
    signo = -1 if a[-1]=='W' else 1
    horas = int(a[:3])
    minu = str('0.' + str(a[3:-1]))
    end_long_list.append(round((horas + float(minu))*signo,5))

    i += 1

i = 0

for n in end_latit:
   
    a = end_latit[i]
    signo = -1 if a[-1]=='S' else 1
    horas = int(a[:2])
    minu = str('0.' + str(a[2:-1]))
    end_latit_list.append(round((horas + float(minu))*signo,5))
    
        
    i += 1

i = 0    

for n in init_latit_list:
    
    d_between_vor = Dist_Coord(init_latit_list[i], end_latit_list[i], init_long_list[i], end_long_list[i])      #funcion que calcula distancia entre puntos de distance_coordinates.py

    distance_list.append(round(d_between_vor, 2))
    
    i +=1



# print(len(vor_name_ini))
# print(len(init_long_list))
# print(len(init_latit_list))