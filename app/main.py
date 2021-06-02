from flask import Blueprint, render_template, request, redirect, flash
from flask.helpers import url_for
from .importar_excel import init_long_list, init_latit_list, end_long_list, end_latit_list, distance_list, route_name, vor_name_end, vor_name_ini
from .dijkstra import shortest_path, Graph, dist_path

main = Blueprint('main', __name__)

aeropuertos = { 'MADRID': 'MADRID', 'BARCELONA':'BARCELONA','BILBAO':'BILBAO', 'SEVILLA':'SEVILLA', 'SANTANDER':'SANTANDER',
'ASTURIAS':'ASTURIAS', 'SANTIAGO':'SANTIAGO', 'A CORUNA':'ACORUNA', 'VIGO':'VIGO', 'VALLADOLID':'VALLADOLID', 'SALAMANCA':'SALAMANCA',
'ZARAGOZA':'ZARAGOZA', 'GIRONA':'GIRONA', 'VALENCIA':'VALENCIA', 'ALBACETE':'ALBACETE', 'ALICANTE':'ALICANTE', 'MURCIA':'MURCIA',
'ALMERIA':'ALMERIA', 'GRANADA':'GRANADA', 'MALAGA': 'MALAGA', 'JEREZ':'JEREZ', 'MALLORCA':'MALLORCA', 'MENORCA':'MENORCA', 
'IBIZA':'IBIZA','A CORUÑA':'ACORUNA'}

# graph = Graph()

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


@main.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        graph = init_graph()

        aeropuerto1 = request.form["origen"]
        aeropuerto2 = request.form["destino"]

        origen = aeropuertos.get(aeropuerto1)
        destino = aeropuertos.get(aeropuerto2)

        if origen == None or destino == None:
            flash('La entrada no es valida', category = 'error')
        else:
            # camino = shortest_path(graph, origen, destino)
            print(origen)
            print(destino)
            # print(camino)

            if origen == destino:
                flash('El destino debe de ser diferente al origen', category = 'error')
            else:
                camino = shortest_path(graph, origen, destino)
                distancia = dist_path(graph, origen, destino)
                return render_template("buscador.html", orig = origen, dest = destino, way = camino, dist = distancia)
    return render_template("home.html")

@main.route("/objetivos")
def objetivo():
    return render_template("objetivos.html")
