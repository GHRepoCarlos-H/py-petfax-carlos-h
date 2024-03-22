# folder petfax file pet.py
from flask import (Blueprint, render_template, json)


bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index():
    pets = json.load(open('pets.json'))
    return render_template('index.html', pets=pets)

@bp.route('/<int:pet_id>')
def show(pet_id):
    pets = json.load(open('pets.json'))
    pet = next((pet for pet in pets if pet['pet_id'] == pet_id), None)
    if pet:
        return render_template('show.html', pet=pet)
    else:
        return "This pet does not exist", 404
    
@bp.route('/facts/new')
def new_fact():
    return render_template('new.html')
