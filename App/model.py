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
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
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

def cargarAeropuerto(catalogo, dato):
    
    if not mp.contains(catalogo['aeropuertos'], dato['IATA']):
        aeropuerto = nuevoAeropuerto(catalogo, dato)
        mp.put(catalogo['aeropuertos'], dato['IATA'], aeropuerto)
    
    if not gr.containsVertex(catalogo['vuelos'], dato['IATA']):
        gr.insertVertex(catalogo['vuelos'], dato['IATA'])
        
        
def cargarAeropuerto1(catalogo, dato):
    
    aeropuerto = nuevoAeropuerto1(dato)
    mp.put(catalogo['aeropuertos'], aeropuerto['IATA'], aeropuerto)
    gr.insertVertex(catalogo['vuelos'], aeropuerto['IATA'])
    
    
    
    
    
    
    
    
    
    
    
    
        

def cargarRuta(catalogo, dato):
    
    ruta = nuevaRuta(dato)
    salidaDestino = (ruta['salida'], '-', ruta['destino'])
    
    if mp.contains(catalogo['rutas'], salidaDestino):
        entry = mp.get(catalogo['rutas'], salidaDestino)
        listaAerolineas = me.getValue(entry)['aerolineas']
        lt.addLast(listaAerolineas, dato['Airline'])
        
    else:
        mp.put(catalogo['rutas'], salidaDestino, ruta)
        
        
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
        
        
    
    
    
    
    
    
        
        
        
def agregarRutas(catalogo):
    
    listaAeropuertos = mp.keySet(catalogo['aeropuertos'])
    
    for aeropuerto in lt.iterator(listaAeropuertos):
        entry = mp.get(catalogo['aeropuertos'], aeropuerto)
        infoAeropuerto = me.getValue(entry)
        destinos = infoAeropuerto['destinos']
        
        for destino in lt.iterator(destinos):
            salDes = aeropuerto + '-' + destino
            entryVuelo = mp.get(catalogo['rutas'], salDes)
            infoVuelo = me.getValue(entryVuelo)
            distancia = infoVuelo['distancia']
            gr.addEdge(catalogo['vuelos'], aeropuerto, destino, distancia)
            
            
def agregarRutas1(catalogo):
    
    listaAeropuertos = gr.vertices(catalogo['vuelos'])
    
    for aeropuerto in lt.iterator(listaAeropuertos):
        entryDestinos = mp.get(catalogo['rutas'], aeropuerto)
        if entryDestinos is not None:
            listaDestinos = me.getValue(entryDestinos)
        
            for destino in lt.iterator(listaDestinos):
                gr.addEdge(catalogo['vuelos'], aeropuerto, destino['destino'], destino['distancia'])
            
            
            
            
            
            
            
            
            
            
            
            
            
            
def cargarVuelosIdaVuelta(catalogo):
    
    listaAeropuertos = gr.vertices(catalogo['vuelos'])
    
    for aeropuerto in lt.iterator(listaAeropuertos):
        
        if not gr.containsVertex(catalogo['vuelosIdaVuelta'], aeropuerto):
            
            listaDestinos = gr.adjacents(catalogo['vuelos'], aeropuerto)
            
            for destino in lt.iterator(listaDestinos):
                listaSalidas = gr.adjacents(catalogo['vuelos'], destino)
                if lt.isPresent(listaSalidas, aeropuerto):
                    agregarVueloIdaVuelta(catalogo, aeropuerto, destino)
                    
                    
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
                    
                    
                    
def agregarVueloIdaVuelta(catalogo, aeropuerto, destino):
    
    salDes = aeropuerto + '-' + destino
    entryDistancia = mp.get(catalogo['rutas'], salDes)
    infoDistancia = me.getValue(entryDistancia)
    distancia = infoDistancia['distancia']
    
    gr.insertVertex(catalogo['vuelosIdaVuelta'], aeropuerto)
    gr.insertVertex(catalogo['vuelosIdaVuelta'], destino)
    gr.addEdge(catalogo['vuelosIdaVuelta'], aeropuerto, destino, distancia)
    
    
    
def cargarCiudad(catalogo, dato):
    
    ciudad = nuevaCiudad(dato)
    mp.put(catalogo['ciudades'], ciudad['nombre'], ciudad)
    
        
# Funciones para creacion de datos

def nuevaRuta(dato):
    
    ruta = {
        'salida': dato['Departure'],
        'destino': dato['Destination'],
        'distancia': dato['distance_km'], 
        'aerolineas': None
    }
    
    ruta['aerolineas'] = lt.newList(datastructure='ARRAY_LIST')
    lt.addLast(ruta['aerolineas'], dato['Airline'])
    
    return ruta


def nuevaRuta1(dato):
    
    ruta = {
        'salida': dato['Departure'],
        'destino': dato['Destination'],
        'distancia': dato['distance_km'], 
        'aerolinea': dato['Airline']
    }
    
    return ruta


















def nuevoAeropuerto(catalogo, dato):
    
    aeropuerto = {
        'nombre': dato['Name'],
        'ciudad': dato['City'],
        'pais': dato['Country'],
        'IATA': dato['IATA'],
        'latitud': dato['Latitude'],
        'longitud': dato['Longitude'],
        'destinos': None
    }
    
    aeropuerto['destinos'] = encontrarDestinos(catalogo, aeropuerto['IATA'])
    
    return aeropuerto


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

def encontrarDestinos(catalogo, IATA):
    
    listaRutas = mp.keySet(catalogo['rutas'])
    listaDestinos = lt.newList(datastructure='ARRAY_LIST')
    
    for i in listaRutas:
        listaSalDes = i.split('-')
        if IATA == listaSalDes[0]:
            lt.addLast(listaDestinos, listaSalDes[1])
            
    return listaDestinos


def numVertices(grafo):
    return gr.numVertices(grafo)


def numArcos(grafo):
    return gr.numEdges(grafo)


def sizeMap(mapa):
    return mp.size(mapa)
            
        
    
# Funciones utilizadas para comparar elementos dentro de una lista

def cmpCiudades():
    pass

# Funciones de ordenamiento
