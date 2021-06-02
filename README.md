# PROYECTO ATLAS
Para correr la app seguir los siguientes pasos (descrito para Windows).

# Creacion del venv en python
Se recomienda la creacion de un venv de python en la carpeta donde se vaya a guardar el codigo. Pegar alli todos los archivos y carpetas **tal y como estan** subidos. Para crear el env, realizar los siguientes pasos en la terminal:
1. Escogemos la carpeta -->  *$ cd micarpeta*
2. Ahora creamos el env --> *$ py -m venv env*
3. Para activarlo introducimos --> *$ env\Scripts\activate*

# Instalacion de los paquetes
Con el env activado, instalaremos los paquetes con los siguiente comandos:

*$ pip install python-math*

*$ pip install xlrd*

*$ pip install numpy*

*$ pip install pandas*

*$ pip install bokeh*

*$ pip install requests*

*$ pip install Flask*

*$ pip install jupyter*


# Iniciar el servidor en Jupyter y el trackeador
Para iniciar el servidor debemos tener activado el env, despues introduciremos el siguiente comando:

*$ jupyter notebook*

Una vez hecho esto deberemos poner en funcionamiento el archivo *flight_radar.ipynb*, para ello una vez inciado
el servidor en Jupyter:
1. Copiamos el enlace en la barra de navegador web del servidor.
2. Vamos a la carpeta *app*
3. Abrimos el archivo y lo ejecutamos con el boton *run*. 

Con esto ya esta activado para su uso en el *localhost:8000*. Para apagar el servidor basta con pulsar *ctrl + c*.

# Iniciar el servidor en FLASK y uso de la app
Para iniciar el servidor debemos tener activado el env, despues introduciremos los siguientes comandos (debemos correr 
esto en otra terminal ya que en la otra tendremos el servidor de Jupyter activo):

*$ set FLASK_APP=app.py*

*$ set FLASK_ENV=development (esto es por si queremos usar el modo debug)*

*$ flask run*

Una vez hecho esto nos aparecera el puerto donde esta la app, y bastara con copiarlo en la barra del navegador
web que tengamos predeterminado. Con esto ya se puede utilizar la app de forma completa. Para apagar el servidor basta con pulsar 
*ctrl + c*, al igual que se hacia con el servidor Jupyter.

