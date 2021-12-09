"""
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
    
def cargarDatos1(catalogo, infoAeropuertos, infoRutas, infoCiudades):
    cont = cargarCiudades(catalogo, infoCiudades)
    cargarAeropuertos1(catalogo, infoAeropuertos)
    cargarRutas1(catalogo, infoRutas)
    numRutas = agregarRutas1(catalogo)
    numRutasIdaVuelta = cargarVuelosIdaVuelta1(catalogo)
    
    return cont, numRutas, numRutasIdaVuelta
    
   
def agregarRutas1(catalogo):
    return model.agregarRutas1(catalogo)    
 
               
def cargarAeropuertos1(catalogo, infoAeropuertos):
    
    archivoAeropuertos = cf.data_dir + infoAeropuertos
    archivo = csv.DictReader(open(archivoAeropuertos, encoding="utf-8"), delimiter=",")
    
    for dato in archivo:
        model.cargarAeropuerto1(catalogo, dato)
        
        
def cargarRutas1(catalogo, infoRutas):
    
    archivoRutas = cf.data_dir + infoRutas
    archivo = csv.DictReader(open(archivoRutas, encoding="utf-8"), delimiter=",")
    
    for dato in archivo:
        model.cargarRuta1(catalogo, dato)
    
    
def cargarVuelosIdaVuelta1(catalogo):
    return model.cargarVuelosIdaVuelta1(catalogo)
      
    
def cargarCiudades(catalogo, infoCiudades):
    
    archivoCiudades = cf.data_dir + infoCiudades
    archivo = csv.DictReader(open(archivoCiudades, encoding="utf-8"), delimiter=",")
    cont = 0
    
    for dato in archivo:
        model.cargarCiudad(catalogo, dato)
        cont += 1
        
    return cont
    

# Funciones de ordenamiento

def merge(lista, identificador):
    return model.merge(lista, identificador)

# Funciones de consulta sobre el catálogo

def numVertices(grafo):
    return model.numVertices(grafo)


def numArcos(grafo):
    return model.numArcos(grafo)


def obtenerArco(grafo, verticeA, verticeB):
    return model.obtenerArco(grafo, verticeA, verticeB)


def sizeMap(mapa):
    return model.sizeMap(mapa)


def infoMap(catalogo, aeropuerto):
    return model.infoMap(catalogo, aeropuerto)


def elementoLista(lista, pos):
    return model.elementoLista(lista, pos)


def primerElementoLista(lista):
    return model.primerElementoLista(lista)


def sizeList(lista):
    return model.sizeList(lista)


def subList(lista, pos, num):
    return model.subList(lista, pos, num)


def calcularHaversine(coordenadasAeropuerto, coordenadasCiudadSalida):
    return model.calcularHaversine(coordenadasAeropuerto, coordenadasCiudadSalida)


def dijsktra(grafo, origen):
    return model.dijsktra(grafo, origen)


def camino(grafo, vertice):
    return model.camino(grafo, vertice)


def sizePila(pila):
    return model.sizePila(pila)


def elementoPila(pila):
    return model.elementoPila(pila)


def aeropuertosInterconectados(grafo, catalogo):
    return model.aeropuertosInterconectados(grafo, catalogo)

def llamarNumeroComponentesFuertementeConectados(grafo):
    return model.numeroComponentesFuertementeConectados(grafo)

def llamarEstanFuertementeConectados(grafo,elemento1,elemento2):
    return model.estanFuertementeConectados(grafo,elemento1,elemento2)

def sublista(lista, pos, num):
    return model.sublista(lista, pos, num)

def llamarDarRutasAfectadas(listaRutas,IATA):
    return model.darRutasAfectadas(listaRutas,IATA)

def llamarDarListaAeropuertosIATA(catalogo, listaIATA):
    return model.darListaAeropuertosIATA(catalogo, listaIATA)

def PrimMST(grafo):
    return model.PrimMST(grafo)


def prueba(grafo, aeropuerto, lista):
    return model.prueba(grafo, aeropuerto, lista)  