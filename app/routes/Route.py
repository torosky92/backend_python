#!/usr/bin/env python
#_*_ coding: utf8 _*_

# Llamo librerias de tiempo y flask
from flask import request
from flask_cors import cross_origin
from app import app
from app.controllers.Routes_Controller import Routes_Controller

route = Routes_Controller()

class Route():
    # BUSCAR PATENTE
    @app.route('/buscar', methods=['GET'])
    @cross_origin()
    def buscar_patente():
        patente = request.args.get('patente', None)
        return route.get_patente(patente)

    # INGRESAR PATENTE
    @app.route('/insertar', methods=['POST'])
    @cross_origin()
    def add_patente():
        value = request.get_json()
        return route.add_patente(value)