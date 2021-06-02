# PROYECTO ATLAS
Para correr la app seguir los siguientes pasos (descrito para Windows).

# Creacion del env en python
Se recomienda la creacion de un env de python en la carpeta donde se vaya a guardar el codigo. Para ello
realizar los siguientes pasos en la terminal:
* 1º Escogemos la carpeta -->  $ cd micarpeta
* 2º Ahora creamos el env --> $ py -3 -m venv venv
* 3ºPara activarlo introducimos --> $ venv\Scripts\activate

# Instalacion de los paquetes
Con el env activado, instalaremos los paquetes con los siguiente comandos:
* $ pip install Flask

# Iniciar el servidor en FLASK
Para iniciar el servidor debemos tener activado el env, despues introduciremos los siguientes comandos:
* $ set FLASK_APP=app.py
* $ set FLASK_ENV=development (esto es por si queremos usar el modo debug)
* $ flask run
Una vez hecho esto nos aparecera el puerto donde esta la app, y bastara con copiarlo en la barra del navegador
web que tengamos predeterminado.

