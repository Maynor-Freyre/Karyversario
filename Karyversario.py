enero       = 0
febrero     = enero + 31
marzo       = febrero + 28
abril       = marzo + 31
mayo        = abril + 30
junio       = mayo + 31
julio       = junio + 30
agosto      = julio + 31
septiembre  = agosto + 31
octubre     = septiembre + 30
noviembre   = octubre + 31
diciembre   = noviembre + 30
i=1000
bisciesto = 0
print(enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre)
inicio = agosto + 12 #Día inicial de mi aniversario#
inicio_ano = 2018 #Para lidiar con años bisciestos#
siguiente = inicio
pending=0
while i!=0:
    if siguiente >= 365:
        siguiente = siguiente - 365
        inicio_ano = inicio_ano + 1
    if inicio_ano%4 == 0 and inicio_ano%100 != 0 and bisciesto !=0:
##        print("Detectado año bisciesto nuevamente, Procede a verificar si se resta un día")
        marzo = febrero + 29        
        if pending == 1:
            siguiente-=1
##            print("Detección confirmada, restando un día")
            pending = 0
        elif pending != 1:
##            print("Detección ignorada, el día ya fue restado")
            pending+=0
        bisciesto=0
    elif inicio_ano%4 == 0 and inicio_ano%100 != 0 and bisciesto == 0:  #año multiplo de 4 PERO no es multiplo de 100 (año bisciesto)
##        print("detectado año bisciesto por primera vez, procede a verificar si se resta un día")
        marzo=febrero + 29
        if siguiente > 59:
##            print("Resta del día confirmada")
            siguiente-=1
            bisciesto = 1
        elif siguiente < 59:
##            print("Resta del día queda pendiente para la detección subsecuente")
            pending=1
            bisciesto = 1
       

    elif inicio_ano%4 == 0 and inicio_ano%100 == 0: #año multiplo de 4 Y ADEMAS es multiplo de 100 (se ignora el año bisciesto)
        marzo=febrero + 28
##        print(".\ndetectado año bisciento, pero fue ignorado por se rmultiplo de 100\n.")
    else:                                   #año normal (no se agrega nada)
        marzo = febrero + 28
##        print(".\nno se detecto año bisciesto\n.")    
    if siguiente >= diciembre:                              
            print(siguiente-diciembre,"de diciembre del año",inicio_ano)           
    elif siguiente > noviembre:
            print(siguiente-noviembre,"de noviembre del año",inicio_ano)       
    elif siguiente > octubre:
            print(siguiente-octubre,"de octubre del año",inicio_ano)
    elif siguiente > septiembre:
            print(siguiente-septiembre,"de septiembre del año",inicio_ano)
    elif siguiente > agosto:
            print(siguiente-agosto,"de agosto del año",inicio_ano)
    elif siguiente > julio:
            print(siguiente-julio,"de julio del año",inicio_ano)
    elif siguiente > junio:
            print(siguiente-junio,"de junio del año",inicio_ano)
    elif siguiente > mayo:
            print(siguiente-mayo,"de mayo del año",inicio_ano)
    elif siguiente > abril:
            print(siguiente-abril,"de abril del año",inicio_ano)
    elif siguiente > marzo:
            print(siguiente-marzo,"de marzo del año",inicio_ano)
    elif siguiente > febrero:
            print(siguiente-febrero,"de febrero del año",inicio_ano)
    elif siguiente > enero:
            print(siguiente-enero,"de enero del año",inicio_ano)   
    siguiente+=200
    i-=1
    
