from flask import Blueprint, render_template, request, flash
from flask.helpers import url_for
from .importar_excel import init_long_list, init_latit_list, end_long_list, end_latit_list, distance_list, route_name, vor_name_end, vor_name_ini
from .dijkstra import shortest_path, Graph, dist_path

# Definicion para __init__
main = Blueprint('main', __name__)

# Diccionario para que valide las entradas tanto del buscador como desde el mapa
aeropuertos = { 'MADRID': 'MADRID', 'BARCELONA':'BARCELONA','BILBAO':'BILBAO', 'SEVILLA':'SEVILLA', 'SANTANDER':'SANTANDER',
'ASTURIAS':'ASTURIAS', 'SANTIAGO':'SANTIAGO', 'A CORUNA':'ACORUNA', 'VIGO':'VIGO', 'VALLADOLID':'VALLADOLID', 'SALAMANCA':'SALAMANCA',
'ZARAGOZA':'ZARAGOZA', 'GIRONA':'GIRONA', 'VALENCIA':'VALENCIA', 'ALBACETE':'ALBACETE', 'ALICANTE':'ALICANTE', 'MURCIA':'MURCIA',
'ALMERIA':'ALMERIA', 'GRANADA':'GRANADA', 'MALAGA': 'MALAGA', 'JEREZ':'JEREZ', 'MALLORCA':'MALLORCA', 'MENORCA':'MENORCA', 
'IBIZA':'IBIZA','A CORUÑA':'ACORUNA'}

# Funcion para que graph no este vacio y funcione la funcion de busqueda del camino mas corto
def init_graph():
    graph = Graph()

    i = 0

    for node in vor_name_ini:
        
        graph.add_node(vor_name_ini[i])
        i += 1
    
    i = 0
    for edge in route_name:
        graph.add_edge(vor_name_ini[i], vor_name_end[i], distance_list[i])
        i += 1
    return graph

# Definicion de la pagina principal y del buscador
@main.route("/", methods=["POST", "GET"]) # Dominio que usa la pagina
def home():
    # POST si envia datos y GET si solo recarga
    if request.method == "POST":

        #Inicializacion de graph
        graph = init_graph()

        # Obtencion del destino y origen en el main y el buscador
        aeropuerto1 = request.form["origen"]
        aeropuerto2 = request.form["destino"]

        # Transformacion de la entrada para que funcione en la funcion dijkistra
        origen = aeropuertos.get(aeropuerto1)
        destino = aeropuertos.get(aeropuerto2)

        # Comprobacion si la entrada es erronea
        if origen == None or destino == None:
            flash('La entrada no es valida', category = 'error') # Hace aparecer una notificacion del error
        else:
            # Comprobacion si la entrada es igual
            if origen == destino:
                flash('El destino debe de ser diferente al origen', category = 'error') # Hace aparecer una notificacion del error
            else:

                # Definicion del camino mas corto y la distancia recorrida
                camino = shortest_path(graph, origen, destino)
                distancia = dist_path(graph, origen, destino)

                # Envio de datos al mapa y definicion de la pagina del buscador/mapa
                return render_template("buscador.html", orig = origen, dest = destino, way = camino, dist = distancia)

    return render_template("home.html") #Definicion de la pagina principal

# Definicion de la pagina de objetivos
@main.route("/objetivos")
def objetivo():
    return render_template("objetivos.html")
