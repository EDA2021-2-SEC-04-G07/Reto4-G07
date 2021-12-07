﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf

sys.setrecursionlimit(1000000000)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar puntos de interconexión aérea")
    print("3- Encontrar clústeres de tráfico aéreo")
    print("4- Encontrar la ruta más corta entre ciudades")
    print("5- Utilizar las millas de viajero")
    print("6- Cuantificar el efecto de un aeropuerto cerrado")
    print("7- Comparar con servicio WEB externo")

catalogo = None
infoAeropuertos = 'airports-utf8-small.csv'
infoRutas = 'routes-utf8-small.csv'
infoCiudades = 'worldcities-utf8.csv'

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        
        catalogo = controller.initCatalogo()
        #controller.cargarDatos(catalogo, infoAeropuertos, infoRutas, infoCiudades)
        cont = controller.cargarDatos1(catalogo, infoAeropuertos, infoRutas, infoCiudades)
        
        print('======== Grafo Dirigido ========')
        print('Total aeropuertos: ', controller.numVertices(catalogo['vuelos']))
        print('Total rutas: ', cont[1])
        print('Total arcos: ', controller.numArcos(catalogo['vuelos']))
        print('')
        print('======== Grafo NO Dirigido ========')
        print('Total aeropuertos: ', controller.numVertices(catalogo['vuelosIdaVuelta']))
        print('Total rutas: ', cont[2])
        print('Total arcos: ', controller.numArcos(catalogo['vuelosIdaVuelta']))
        print('')
        print('Total de ciudades: ', cont[0])


    elif int(inputs[0]) == 2:
        
        listaInterconectadosDirigido = controller.aeropuertosInterconectados(catalogo['vuelos'], catalogo)
        listaInterconectadosNODirigido = controller.aeropuertosInterconectados(catalogo['vuelosIdaVuelta'], catalogo)
        listaInterconectadosDirigidoOrdenada = controller.merge(listaInterconectadosDirigido, 1)
        listaInterconectadosNODirigidoOrdenada = controller.merge(listaInterconectadosNODirigido, 1)
        
        if controller.sizeList(listaInterconectadosDirigidoOrdenada) < 5:
            top5Dirigido = controller.sublista(listaInterconectadosDirigidoOrdenada, 1, controller.sizeList(listaInterconectadosDirigidoOrdenada))
        else:
            top5Dirigido = controller.sublista(listaInterconectadosDirigidoOrdenada, 1, 5)
            
        if controller.sizeList(listaInterconectadosNODirigidoOrdenada) < 5:
            top5NODirigido = controller.sublista(listaInterconectadosNODirigidoOrdenada, 1, controller.sizeList(listaInterconectadosNODirigidoOrdenada))
        else:
            top5NODirigido = controller.sublista(listaInterconectadosNODirigidoOrdenada, 1, 5)
        
        print('======== Grafo Dirigido ========')
        print('')
        
        if controller.sizeList(top5Dirigido) != 0:
            
            print('Los 5 aeropuertos más interconectados son: ')
            print('')
            print('    IATA    |    Nombre    |    Ciudad    |    País    |    Número de Interconexiones')
            print('')
            
            for aeropuerto in lt.iterator(top5Dirigido):
            
                infoAeropuerto = controller.infoMap(catalogo['aeropuertos'], aeropuerto['aeropuerto'])
                print('    {}    {}    {}    {}     {}'.format(infoAeropuerto['IATA'], infoAeropuerto['nombre'], infoAeropuerto['ciudad'], infoAeropuerto['pais'], aeropuerto['puntInterconexión']))
        
            print('')
            print('El número de aeropuertos interconectados es: ', controller.sizeList(listaInterconectadosDirigidoOrdenada))
        
        elif controller.sizeList(top5Dirigido) == 0:
            print('No existen aeropuertos interconectados')
            
        print('')
        print('')
        
        print('======== Grafo No Dirigido ========')
        print('')
        
        if controller.sizeList(top5NODirigido) != 0:
            
            print('Los 5 aeropuertos más interconectados son: ')
            print('')
            print('    IATA    |    Nombre    |    Ciudad    |    País    |    Número de Interconexiones')
            print('')
        
            for aeropuerto in lt.iterator(top5NODirigido):
            
                infoAeropuerto = controller.infoMap(catalogo['aeropuertos'], aeropuerto['aeropuerto'])
                print('  {}  {}  {}  {}  {}'.format(infoAeropuerto['IATA'], infoAeropuerto['nombre'], infoAeropuerto['ciudad'], infoAeropuerto['pais'], aeropuerto['puntInterconexión']))
            
            print('')
            print('El número de aeropuertos interconectados es: ', controller.sizeList(listaInterconectadosNODirigidoOrdenada))
            
        elif controller.sizeList(top5NODirigido) == 0:
            print('No existen aeropuertos interconectados')
            
        print('')
        print('')

        
    elif int(inputs[0]) == 3:
        numComponentes = controller.llamarNumeroComponentesFuertementeConectados(catalogo['vuelos'])
        print(f'El numero de componentes fuertemente conectados es de: {numComponentes}')
        IATA1 = input('Digite el codigo IATA del aeropuerto 1: ')
        IATA2 = input('Digite el codigo IATA del aeropuerto 2: ')
        
        aeropuerto1 = controller.infoMap(catalogo['aeropuertos'], IATA1)
        aeropuerto2 = controller.infoMap(catalogo['aeropuertos'], IATA2)
        
        estanConectados = controller.llamarEstanFuertementeConectados(catalogo['vuelos'],IATA1,IATA2)
        
        print('El Aeropuerto 1 es: ')
        print('')
        print('    IATA    |    Nombre    |    Ciudad    |    País')
        print('')
        print('  {}  {}  {}  {}  '.format(aeropuerto1['IATA'], aeropuerto1['nombre'], aeropuerto1['ciudad'], aeropuerto1['pais']))
        print('')
        print('El Aeropuerto 2 es: ')
        print('')
        print('    IATA    |    Nombre    |    Ciudad    |    País')
        print('')
        print('  {}  {}  {}  {}  '.format(aeropuerto2['IATA'], aeropuerto2['nombre'], aeropuerto2['ciudad'], aeropuerto2['pais']))
        print('')
        if estanConectados:
            print(f'El aeropuerto de IATA: {IATA1} esta fuertemente conectado con el aeropuerto de IATA: {IATA2}')
        else:
            print(f'El aeropuerto de IATA: {IATA1} no esta fuertemente conectado con el aeropuerto de IATA: {IATA2}')

    elif int(inputs[0]) == 4:
        
        ciudadSalida = input('Digite la ciudad de salida: ')
        ciudadLlegada = input('Digite la ciudad de llegada: ')
        
        listaCiudadesSalida = controller.infoMap(catalogo['ciudades'], ciudadSalida)
        listaCiudadesLlegada = controller.infoMap(catalogo['ciudades'], ciudadLlegada)
        
        print('A continuación se muestran las ciudades homónimas de salida')
        print('')
        print('    Ciudad    |    País    |    Latitud    |    Longitud')
        print('')
        
        elementosSublistaSalida = controller.sizeList(listaCiudadesSalida)
        listaCiudadesSalidaFinal = controller.subList(listaCiudadesSalida, 2, elementosSublistaSalida-1)
        
        for ciudad in lt.iterator(listaCiudadesSalidaFinal):
            print('{}    {}    {}    {}'.format(ciudad['nombre'], ciudad['pais'], ciudad['latitud'], ciudad['longitud']))
            
        print('')
        posSalida = int(input('Digite la posición de la ciudad de salida que desea: '))
        print('')
        print('')
        
        print('A continuación se muestran las ciudades homónimas de llegada')
        print('')
        print('    Ciudad    |    País    |    Latitud    |    Longitud')
        print('')
        
        elementosSublistaLlegada = controller.sizeList(listaCiudadesLlegada)
        listaCiudadesLlegadaFinal = controller.subList(listaCiudadesLlegada, 2, elementosSublistaLlegada-1)
        
        for ciudad in lt.iterator(listaCiudadesLlegadaFinal):
            print('{}    {}    {}    {}'.format(ciudad['nombre'], ciudad['pais'], ciudad['latitud'], ciudad['longitud']))
            
        print('')
        posLlegada = int(input('Digite la posición de la ciudad de llegada que desea: '))
        
        ciudadSalidaFinal = controller.elementoLista(listaCiudadesSalidaFinal, posSalida)
        ciudadLlegadaFinal = controller.elementoLista(listaCiudadesLlegadaFinal, posLlegada)
        coordenadasCiudadSalida = (float(ciudadSalidaFinal['latitud']), float(ciudadSalidaFinal['longitud']))
        coordenadasCiudadLlegada = (float(ciudadLlegadaFinal['latitud']), float(ciudadLlegadaFinal['longitud']))
        
        listaAeropuertosSalida = controller.primerElementoLista(listaCiudadesSalida)
        listaAeropuertosLlegada = controller.primerElementoLista(listaCiudadesLlegada)
        
        menorSalida = 10000000000
        aeropuertoMenorSalida = None
        menorLlegada = 10000000000
        aeropuertoMenorLlegada = None
        
        for aeropuerto in lt.iterator(listaAeropuertosSalida):
            
            infoAeropuerto = controller.infoMap(catalogo['aeropuertos'], aeropuerto)
            coordenadasAeropuerto = (float(infoAeropuerto['latitud']), float(infoAeropuerto['longitud']))
            
            haversine = controller.calcularHaversine(coordenadasAeropuerto, coordenadasCiudadSalida)
            
            if haversine < menorSalida:
                menorSalida = haversine
                aeropuertoMenorSalida = aeropuerto
                
        for aeropuerto in lt.iterator(listaAeropuertosLlegada):
            
            infoAeropuerto = controller.infoMap(catalogo['aeropuertos'], aeropuerto)
            coordenadasAeropuerto = (float(infoAeropuerto['latitud']), float(infoAeropuerto['longitud']))
            
            haversine = controller.calcularHaversine(coordenadasAeropuerto, coordenadasCiudadLlegada)
            
            if haversine < menorLlegada:
                menorLlegada = haversine
                aeropuertoMenorLlegada = aeropuerto
                
        grafoRutasMínimas = controller.dijsktra(catalogo['vuelos'], aeropuertoMenorSalida)
        camino = controller.camino(grafoRutasMínimas, aeropuertoMenorLlegada)
        
        print('')
        print('Aeropuerto origen: ', aeropuertoMenorSalida)
        print('Aeropuerto destino: ', aeropuertoMenorLlegada)
        print('')
        print('Ruta: ')
        print('')
        
        i = controller.sizePila(camino)
        sumaDistanciaRuta = 0
        
        while i > 0:
            
            elemento = controller.elementoPila(camino)
            sumaDistanciaRuta += elemento['weight']
            print('{} --> {}  //Distancia: {} km'.format(elemento['vertexA'], elemento['vertexB'], elemento['weight']))
            i -= 1
         
        #distanciaTotal = menorSalida + menorLlegada +  sumaDistanciaRuta  Esta incluye la distancia de la ciudad al aeropuerto
        distanciaTotal = menorSalida + menorLlegada
        print('')
        print('Distancia total de la ruta: ', distanciaTotal)
        print('')
        print('')
        

    elif int(inputs[0]) == 5:
        aeropuerto = input('Escriba el codigo del aeropuerto de salida: ')
        millas = input('Escriba el numero de millas disponibles: ')



    else:
        sys.exit(0)
sys.exit(0)
