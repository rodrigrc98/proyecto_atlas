from flask import Flask

#Funcion que crea la app en flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Proyecto Atlas'

    #Importacion de los blueprints
    from .main import main
    app.register_blueprint(main, url_prefix='/') # A partir de donde se va a escribir la ruta

    return app 