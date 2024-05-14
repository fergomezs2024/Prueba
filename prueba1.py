#Precio tratamiento
CARILLAS_PORCELANA = 250000
IMPLANTES_DENTALES = 475000
ORTODONCIA_BRACKETS = 800000 
#Descuentos 
DSCTO_AUXILIAR = 0.15
DSCTO_ADMINISTRATIVO = 0.1
DSCTO_DOCENTE= 0.05
#************************************************
# booleanos
valida = True
valida_coti = True

#Descuentos
tipo_dscto = ""
opcion = ""
tratamientos= ""


#Calculos

# MENU

while valida != False :
    canti_carilla = 0
    canti_implante=0
    canti_orto =0
    total = 0
    subtotal = 0
    descuento = 0
    monto_descuento =0
    dscto_subtotal = 0

    opcion = input("Seleccione una opcion \n 1)Cotizacion \n 2)Renunciar \n 3)Salir ")
    if opcion == "3":
        valida =False
    elif opcion=="2":
        canti_carilla = 0
        canti_implante=0
        canti_orto =0
        total = 0
        subtotal = 0
        descuento = 0
        monto_descuento =0
        dscto_subtotal = 0
        print("Cotizacion anterior eliminada!!")
 
        next
    if opcion =="1":
        if opcion == "1":
            while valida_coti !=False:
                tratamientos = input(f" Seleccione un tratamiento \n 1)Carillas Porcerlana = {CARILLAS_PORCELANA} \n 2)Implantes dentales = {IMPLANTES_DENTALES} \n 3)Ortodoncias dentales = {ORTODONCIA_BRACKETS} \n 4) Terminar ")
                if tratamientos == "1":
                    canti_carilla +=1
                elif tratamientos =="2":
                    canti_implante +=1
                elif tratamientos =="3":
                    canti_orto +=1
                else :
                    valida_coti = False
            
            tipo_dscto = input("Seleccione su cargo para obtener un descuento  \n 1) Auxiliar \n 2) Administrativo \n 3) Docente")
            if tipo_dscto =="1":
                descuento = DSCTO_AUXILIAR
            elif tipo_dscto =="2":
                descuento = DSCTO_AUXILIAR
            else :
                descuento = DSCTO_DOCENTE


            print("-"*22)
            print("-"," "*3,"Cotizacion"," "*3, "-")
            print("-"*22)   
            if canti_carilla > 0 :
                print("-->",f"Tratamiento(s) Carillas Porcelana  {CARILLAS_PORCELANA * canti_carilla}")
                subtotal += CARILLAS_PORCELANA * canti_carilla
            if canti_implante > 0 :
                print("-->",f"Tratamiento(s) Implantes dentales  {IMPLANTES_DENTALES * canti_implante}")
                subtotal += IMPLANTES_DENTALES * canti_implante
            if canti_orto > 0 :
                print("-->",f"Tratamiento(s) Ortodoncia brackets  {ORTODONCIA_BRACKETS * canti_orto}")
                subtotal += ORTODONCIA_BRACKETS * canti_orto
            print("-"*22)
            print(f"Subtotal  {subtotal}")
            dscto_subtotal =  subtotal * descuento
            print(f"Descuento {dscto_subtotal}")
            total = subtotal - dscto_subtotal
            print(f"Total {total}")
            print("-"*22)
            print(f"Son  12 cuotas de : {total /12}")
            print("")
            print("Sonria Bonito!!!")
            print("\n\n")
    #Resultados
    
    
