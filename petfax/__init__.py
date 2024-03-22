# folder petfax file __init__.py
from flask import Flask, render_template

def create_app():
    app = Flask(__name__, template_folder='templates')

    @app.route('/')
    def hello():
        return "Hello, PetFax"
    
    from . import pet
    app.register_blueprint(pet.bp)

    @app.route('/pets/facts/new')
    def new_fact():
        return render_template('new.html')
    

    return app