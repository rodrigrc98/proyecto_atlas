from numpy import append
from importar_excel import init_long_list, init_latit_list, vor_name_ini

jscode = []

lista_vor_unico = []
lat_unica = []
lon_unica = []
n=0

#codigo para escribir la representacion de la lista de puntos vor en js y exportarla a un txt


# bucle que retira los duplicados

for i in vor_name_ini:
    if i not in lista_vor_unico:
        lista_vor_unico.append(i)
        lat_unica.append(init_latit_list[n])
        lon_unica.append(init_long_list[n])

    n += 1
    

# concatenacion de string y adicion a una lista para posteriormente escribirla en un txt
i = 0
for vor in lista_vor_unico:

    jscode.append('L.marker(['+ str(lat_unica[i]) + ',' + str(lon_unica[i]) + '], {icon: voricon, nombre:"'+ str(lista_vor_unico[i]) +'", coordenadas:[' + str(lat_unica[i]) + ',' + str(lon_unica[i]) + '], latitud:' + str(lat_unica[i]) + ', longitud:' + str(lon_unica[i]) + '}).bindPopup("VOR:' + str(lista_vor_unico[i]) + '"),')
    
    i += 1



textfile = open("vor_js.txt", "w")

for element in jscode:

    textfile.write(element + "\n")

textfile.close()
