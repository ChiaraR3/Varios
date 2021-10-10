"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Client, Plan, Machine, Booking, Award, Exercise, Stay
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend"
    }

    return jsonify(response_body), 200

@api.route('/create/machine', methods=['GET'])
def list_of_machines():

    machine1 = Machine(
     name = "cinta de correr",
    )
    db.session.add(machine1)
    
    machine2=  Machine(
     name = "kettlebell",
    )
    db.session.add(machine2)

    machine3=  Machine(
     name = "Pesas",
    )
    db.session.add(machine3)

    machine4=  Machine(
     name = "eliptica",
    )
    db.session.add(machine4)

    machine5=  Machine(
     name = "bicicleta",
    )
    db.session.add(machine5)

    machine6=  Machine(
     name = "maquina de abdominales",
    )
    db.session.add(machine6)
    
    
    db.session.commit()

    return jsonify("machine ok"), 200


@api.route('/machines', methods=['GET'])
def get_machines():
    machines = Machine.query.all()
    machines = list(map(lambda machine : machine.serialize(), machines))
    return jsonify(machines), 200

@api.route('/create/exercise', methods=['GET'])
def list_of_exercises():

    exercise1 = Exercise(
     name = "cardio",
     time = "10",
     detail = "velocidad 6.5",
     machine_id = 2,
    )

    db.session.add(exercise1)
    
    exercise2= Exercise(
     name = "fuerza",
     time = "20",
     detail = "5 repeticiones de 10",
     machine_id = 2,
    )

    db.session.add(exercise2)
    db.session.commit()

    return jsonify("exercise ok"), 200

@api.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    exercises = list(map(lambda exercise : exercise.serialize(), exercises))
    return jsonify(exercises), 200



@api.route('/create/stay', methods=['GET'])
def list_of_stays():

    stay1 = Stay(
     name = "corta estancia",
     from_day = "1",
     to_day = "4",
    )
    db.session.add(stay1)
    
    stay2 = Stay(
     name = "media estancia",
     from_day = "5",
     to_day = "10",
    )
    db.session.add(stay2)

    stay3 = Stay(
     name = "larga estancia",
     from_day = "11",
     to_day = "1000",
    )
    db.session.add(stay3)
    
    db.session.commit()

    return jsonify("stay ok"), 200

@api.route('/stays', methods=['GET'])
def get_stays():
    stays = Stay.query.all()
    stays = list(map(lambda stay : stay.serialize(), stays))
    return jsonify(stays), 200
