import requests
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import HoverTool,LabelSet,ColumnDataSource
from bokeh.tile_providers import get_provider, STAMEN_TONER
import numpy as np
from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler

#Función para transformar coordenadas WGS84 en coordenadas Web Mercator
#DataFrame
def wgs84_to_web_mercator(df, lon="long", lat="lat"):
    k = 6378137
    df["x"] = df[lon] * (k * np.pi/180.0)
    df["y"] = np.log(np.tan((90 + df[lat]) * np.pi/360.0)) * k
    return df

#Punto
def wgs84_web_mercator_point(lon,lat):
    k = 6378137
    x= lon * (k * np.pi/180.0)
    y= np.log(np.tan((90 + lat) * np.pi/360.0)) * k
    return x,y

#Area geográfica de estudio
lon_min,lat_min=-11,35.88
lon_max,lat_max=5,44

#Conversión de coordenadas
xy_min=wgs84_web_mercator_point(lon_min,lat_min)
xy_max=wgs84_web_mercator_point(lon_max,lat_max)

x_range,y_range=([xy_min[0],xy_max[0]], [xy_min[1],xy_max[1]])

#Realizamos la solicitud a la API a través de una cuenta registrada
user_name='Atlas'
password='yprE7x7WUgkK3v!'
url_data='https://'+user_name+':'+password+'@opensky-network.org/api/states/all?'+'lamin='+str(lat_min)+'&lomin='+str(lon_min)+'&lamax='+str(lat_max)+'&lomax='+str(lon_max)

    
#Definimos la función flight_tracking
def flight_tracking(doc):
    #Inicializamos la tabla de datos
    flight_source = ColumnDataSource({
        'icao24':[],'callsign':[],'origin_country':[],
        'time_position':[],'last_contact':[],'long':[],'lat':[],
        'baro_altitude':[],'on_ground':[],'velocity':[],'true_track':[],
        'vertical_rate':[],'sensors':[],'geo_altitude':[],'squawk':[],'spi':[],'position_source':[],'x':[],'y':[],
        'rot_angle':[],'url':[]
    })
    
    #Definimos función que nos permita actualizar los datos
    def update():
        response=requests.get(url_data).json()
        
        #Lo convertimos en pandas dataframe
        col_name=['icao24','callsign','origin_country','time_position','last_contact','long','lat','baro_altitude','on_ground','velocity',       
'true_track','vertical_rate','sensors','geo_altitude','squawk','spi','position_source']
        flight_data=response['states']
        flight_df=pd.DataFrame(flight_data,columns=col_name)
        wgs84_to_web_mercator(flight_df)
        flight_df=flight_df.fillna('No Data')
        flight_df['rot_angle']=flight_df['true_track']*-1
        icon_url='https:...' #icon url
        flight_df['url']=icon_url
        
        #Convertimos los datos a Bokeh
        n_roll=len(flight_df.index)
        flight_source.stream(flight_df.to_dict(orient='list'),n_roll)
        
    #Establecemos tiempo de actualización
    doc.add_periodic_callback(update, 5000) #5000 ms/10000 ms for registered user . 
    
    #Dibujamos posición de la aeronave
    p=figure(x_range=x_range,y_range=y_range,x_axis_type='mercator',y_axis_type='mercator',sizing_mode='scale_width',plot_height=300)
    tile_prov=get_provider(STAMEN_TONER)
    p.add_tile(tile_prov,level='image')
    p.image_url(url='url', x='x', y='y',source=flight_source,anchor='center',angle_units='deg',angle='rot_angle',h_units='screen',w_units='screen',w=40,h=40)
    p.circle('x','y',source=flight_source,fill_color='red',hover_color='yellow',size=10,fill_alpha=0.8,line_width=0)

    #Añadimos las etiquetas
    my_hover=HoverTool()
    my_hover.tooltips=[('Matrícula','@callsign'),('País de origen','@origin_country'),('Velocidad(m/s)','@velocity'),('Altitud(m)','@baro_altitude')]
    labels = LabelSet(x='x', y='y', text='callsign', level='glyph',
            x_offset=5, y_offset=5, source=flight_source, render_mode='canvas',background_fill_color='white',text_font_size="8pt")
    p.add_tools(my_hover)
    p.add_layout(labels)
    
    doc.title='Flight Tracking'
    doc.add_root(p)


#Iniciamos el server en un puerto local
apps = {'/': Application(FunctionHandler(flight_tracking))}
server = Server(apps, port=8000) 
server.start()




