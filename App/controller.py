﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo

def initCatalogo():
    return model.initCatalogo()

# Funciones para la carga de datos

def cargarDatos(catalogo, infoAeropuertos, infoRutas, infoCiudades):
    
    cargarRutas(catalogo, infoRutas)
    cargarAeropuertos(catalogo, infoAeropuertos)
    agregarRutas(catalogo)
    cargarCiudades(catalogo, infoCiudades)
    cargarVuelosIdaVuelta(catalogo)
    
def cargarDatos1(catalogo, infoAeropuertos, infoRutas, infoCiudades):
    cargarAeropuertos1(catalogo, infoAeropuertos)
    cargarRutas1(catalogo, infoRutas)
    agregarRutas1(catalogo)
    cargarCiudades(catalogo, infoCiudades)
    cargarVuelosIdaVuelta1(catalogo)
    
    
    
    
    
    
    
def agregarRutas(catalogo):
    model.agregarRutas(catalogo)
    
def agregarRutas1(catalogo):
    model.agregarRutas1(catalogo)
    
    
    
    
    
    
def cargarAeropuertos(catalogo, infoAeropuertos):
    
    archivoAeropuertos = cf.data_dir + infoAeropuertos
    archivo = csv.DictReader(open(archivoAeropuertos, encoding="utf-8"), delimiter=",")
    
    for dato in archivo:
        model.cargarAeropuerto(catalogo, dato)
        
        
def cargarAeropuertos1(catalogo, infoAeropuertos):
    
    archivoAeropuertos = cf.data_dir + infoAeropuertos
    archivo = csv.DictReader(open(archivoAeropuertos, encoding="utf-8"), delimiter=",")
    
    for dato in archivo:
        model.cargarAeropuerto1(catalogo, dato)
        
        
        
        
        
        
        
        
        
        
        
def cargarRutas(catalogo, infoRutas):
    
    archivoRutas = cf.data_dir + infoRutas
    archivo = csv.DictReader(open(archivoRutas, encoding="utf-8"), delimiter=",")
    
    for dato in archivo:
        model.cargarRuta(catalogo, dato)
        
        
def cargarRutas1(catalogo, infoRutas):
    
    archivoRutas = cf.data_dir + infoRutas
    archivo = csv.DictReader(open(archivoRutas, encoding="utf-8"), delimiter=",")
    
    for dato in archivo:
        model.cargarRuta1(catalogo, dato)
        
        
        
        
        
        
        
        
        
        
        
        
def cargarVuelosIdaVuelta(catalogo):
    model.cargarVuelosIdaVuelta(catalogo)
    
    
def cargarVuelosIdaVuelta1(catalogo):
    model.cargarVuelosIdaVuelta1(catalogo)
    
    
    
    
    
    
    
def cargarCiudades(catalogo, infoCiudades):
    
    archivoCiudades = cf.data_dir + infoCiudades
    archivo = csv.DictReader(open(archivoCiudades, encoding="utf-8"), delimiter=",")
    
    for dato in archivo:
        model.cargarCiudad(catalogo, dato)
    
    

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def numVertices(grafo):
    return model.numVertices(grafo)


def numArcos(grafo):
    return model.numArcos(grafo)


def sizeMap(mapa):
    return model.sizeMap(mapa)