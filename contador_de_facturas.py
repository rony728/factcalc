#! /usr/bin/python3

while True:

    print( "**Bienvenido al contador de facturas**" )

#ingresa la cantidad de facturas en orden ascendiente
    veinte = int(input("Ingrese la cantidad de facturas de lps 20: ")) #ingresa el numero de facturas de lps 20
    v1 = veinte*20
    print(veinte*20)
    veinticinco = int(input( "Ingrese la cantidad de facturas de lps 25: " )) #ingresa el numero de facturas de lps 25
    v2 = veinticinco*25
    print(veinticinco*25)
    treintaicinco = int(input( "Ingrese la cantidad de facturas de lps 35: " )) #ingresa el numero de facturas de lps 35
    v3 = treintaicinco*35
    print(treintaicinco*35)
    taxis = int(input( "Ingrese la cantidad de facturas de taxis : " )) #ingresa la cantidad de facturas por taxis
    v4 = taxis*1050
    print(taxis*1050)
    locales_y_publicidad = int(input( "Ingrese la cantidad de facturas locales  : " ))

#calcula y muetra el total de dinero y numero de facturas
    total_de_facturas = veinte + veinticinco + treintaicinco + taxis + locales_y_publicidad #suma el total de facturas
    print( "El Total de Facturas es de: ")
    print(total_de_facturas)
    print( "El Total de Dinero es de: ")
    print(v1+v2+v3+v4)

#calcula el total de dinero cuando se pagan mas de 41 taxis
    mas_taxis = int(input(" si el pago de taxis es mas de 41 unidades ingrese 1 de lo contrario ingrese 0: "))
    if mas_taxis == 1:
        print(v1+v2+v3+v4+25)
    else:
        print ( "..." )
        
        
