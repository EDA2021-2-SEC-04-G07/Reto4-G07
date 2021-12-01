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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import haversine as hv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import stack as sk
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT.graph import gr
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def initCatalogo():

    catalogo = {
        "rutas": None,
        "aeropuertos":None,
        "vuelos" : None,
        "vuelosIdaVuelta" : None,
        "ciudades": None
    }
    
    catalogo['rutas'] = mp.newMap(numelements=14000,
                                     maptype='PROBING',
                                     comparefunction=None)
    
    catalogo['aeropuertos'] = mp.newMap(numelements=14000,
                                     maptype='CHAINING',
                                     comparefunction=None)

    catalogo["vuelos"] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000,
                                              comparefunction=None)
    
    catalogo['vuelosIdaVuelta'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=14000,
                                              comparefunction=None)
    
    catalogo['ciudades'] = mp.newMap(numelements=14000,
                                     maptype='CHAINING',
                                     comparefunction=None)
    
    return catalogo

# Funciones para agregar informacion al catalogo
        
def cargarAeropuerto1(catalogo, dato):
    
    aeropuerto = nuevoAeropuerto1(dato)
    
    entryCiudad = mp.get(catalogo['ciudades'], aeropuerto['ciudad'])
    
    if entryCiudad != None:
        listaCiudades = me.getValue(entryCiudad)
        listaAeropuertos = lt.firstElement(listaCiudades)
        lt.addLast(listaAeropuertos, aeropuerto['IATA'])
    
    mp.put(catalogo['aeropuertos'], aeropuerto['IATA'], aeropuerto)
    gr.insertVertex(catalogo['vuelos'], aeropuerto['IATA'])
        
        
def cargarRuta1(catalogo, dato):
    
    ruta = nuevaRuta1(dato)
    
    if mp.contains(catalogo['rutas'], ruta['salida']):
        entryRutas = mp.get(catalogo['rutas'], ruta['salida'])
        listaRutas = me.getValue(entryRutas)
        lt.addLast(listaRutas, ruta)
        
    else:
        listaRutas = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(listaRutas, ruta)
        mp.put(catalogo['rutas'], ruta['salida'], listaRutas)
            
            
def agregarRutas1(catalogo):
    
    listaAeropuertos = gr.vertices(catalogo['vuelos'])
    
    for aeropuerto in lt.iterator(listaAeropuertos):
        entryDestinos = mp.get(catalogo['rutas'], aeropuerto)
        if entryDestinos is not None:
            listaDestinos = me.getValue(entryDestinos)
        
            for destino in lt.iterator(listaDestinos):
                gr.addEdge(catalogo['vuelos'], aeropuerto, destino['destino'], destino['distancia'])
                    
                    
def cargarVuelosIdaVuelta1(catalogo):
    
    listaArcos = gr.edges(catalogo['vuelos'])
    
    for arco in lt.iterator(listaArcos):
        
        arcoTranspuesto = gr.getEdge(catalogo['vuelos'], arco['vertexB'], arco['vertexA'])
        
        if arcoTranspuesto is not None:
            agregarRutaIdaVuelta(catalogo, arco)
    
    
def agregarRutaIdaVuelta(catalogo, arco):
    
    if not gr.containsVertex(catalogo['vuelosIdaVuelta'], arco['vertexA']):
        gr.insertVertex(catalogo['vuelosIdaVuelta'], arco['vertexA'])
        
    if not gr.containsVertex(catalogo['vuelosIdaVuelta'], arco['vertexB']):
        gr.insertVertex(catalogo['vuelosIdaVuelta'], arco['vertexB'])
        
    gr.addEdge(catalogo['vuelosIdaVuelta'], arco['vertexA'], arco['vertexB'], arco['weight'])
    
    
def cargarCiudad(catalogo, dato):
    
    ciudad = nuevaCiudad(dato)
    
    if mp.contains(catalogo['ciudades'], ciudad['nombre']):
        entryCiudad = mp.get(catalogo['ciudades'], ciudad['nombre'])
        infoCiudad = me.getValue(entryCiudad)
        lt.addLast(infoCiudad, ciudad)
    else:
        listaCiudades = lt.newList(datastructure='ARRAY_LIST')
        lista_aeropuertos = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(listaCiudades, lista_aeropuertos)
        lt.addLast(listaCiudades, ciudad)
        mp.put(catalogo['ciudades'], ciudad['nombre'], listaCiudades)
    
        
# Funciones para creacion de datos

def nuevaRuta1(dato):
    
    ruta = {
        'salida': dato['Departure'],
        'destino': dato['Destination'],
        'distancia': float(dato['distance_km']), 
        'aerolinea': dato['Airline']
    }
    
    return ruta


def nuevoAeropuerto1(dato):
    
    aeropuerto = {
        'nombre': dato['Name'],
        'ciudad': dato['City'],
        'pais': dato['Country'],
        'IATA': dato['IATA'],
        'latitud': dato['Latitude'],
        'longitud': dato['Longitude'],
    }
    
    return aeropuerto


def nuevaCiudad(dato):
    
    ciudad = {
        'nombre': dato['city'],
        'nombre_ASCII': dato['city_ascii'],
        'latitud': dato['lat'],
        'longitud': dato['lng'],
        'pais': dato['country'],
        'capital': dato['capital'],
        'poblacion': dato['population'],
        'id': dato['id']
    }
    
    return ciudad


# Funciones de consulta

def numVertices(grafo):
    return gr.numVertices(grafo)


def numArcos(grafo):
    return gr.numEdges(grafo)


def obtenerArco(grafo, verticeA, verticeB):
    return gr.getEdge(grafo, verticeA, verticeB)


def sizeMap(mapa):
    return mp.size(mapa)


def infoMap(mapa, llave):
    
    entry = mp.get(mapa, llave)
    value = me.getValue(entry)
    
    return value


def elementoLista(lista, pos):
    
    lista = lt.getElement(lista, pos)
    return lista


def primerElementoLista(lista):
    
    elemento = lt.firstElement(lista)
    return elemento


def sizeList(lista):
    return lt.size(lista)


def subList(lista, pos, num):
    return lt.subList(lista, pos, num)


def calcularHaversine(coordenadasAeropuerto, coordenadasCiudadSalida):
    
    haversine = hv.haversine(coordenadasAeropuerto, coordenadasCiudadSalida)
    
    return haversine


def dijsktra(grafo, origen):
    
    grafo = djk.Dijkstra(grafo, origen)
    return grafo


def camino(grafo, vertice):
    
    pila = djk.pathTo(grafo, vertice)
    return pila


def sizePila(pila):
    return sk.size(pila)


def elementoPila(pila):
    return sk.pop(pila)
    
    


def infoMapInterconectados(catalogo, listaInterconectados, mayor):
    
    infoAeropuertos = lt.newList(datastructure='ARRAY_LIST')
    
    for aeropuerto in lt.iterator(listaInterconectados):
    
        entry = mp.get(catalogo['aeropuertos'], aeropuerto)
        value = me.getValue(entry)
        lt.addLast(infoAeropuertos, value)
    
    return infoAeropuertos, mayor


def aeropuertosInterconectados(grafo, catalogo):
    
    mayor = 0
    interconectadoMayor = None
    listaAeropuertos = gr.vertices(grafo)
    listaInterconectados = lt.newList(datastructure='ARRAY_LIST')
    
    for aeropuerto in lt.iterator(listaAeropuertos):
        
        puntInterconexion = gr.degree(grafo, aeropuerto)
        
        if puntInterconexion >= mayor:
            mayor = puntInterconexion
            
    for aeropuerto in lt.iterator(listaAeropuertos):
        
        puntInterconexion = gr.degree(grafo, aeropuerto)
        
        if puntInterconexion >= mayor:
            lt.addLast(listaInterconectados, aeropuerto)
            
    return infoMapInterconectados(catalogo, listaInterconectados, mayor)
            
            
    
# Funciones utilizadas para comparar elementos dentro de una lista

def cmpCiudades():
    pass

# Funciones de ordenamiento
