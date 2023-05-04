import random


repetir="s"
SaldoDisponible=4500
for i in range(3,-1,-1):
    numero=input("Escriba su numero de celular \n")
    claveDigitada=input("Digite la clave de 4 digitos \n")
    if numero=="1023" and claveDigitada=="1234":
        while repetir=="s" or repetir=="S":
            print("Bienvenido A Nequi, Su saldo actual es de ",SaldoDisponible)
            ChoiseUser=input("Escoga entre estas opciones cual desea ejecutar: \n1. Para Sacar\n2. Para Envíar\n3. Para Recargar\n4. Para Sucribirse a una Plataforma de Streaming\n5. Para Pagar Recibos \n6. Para Salir Del Aplicativo\n")
            if ChoiseUser=="1":
                ChoiseSacar=input("Ahora escriba que opción desea digitar \nCajero: para sacar el dinero desde un punto Cajero y generar un codigo \nPunto Fisico: para generar un codigo de acceso en un punto fijo \n").lower()
                codigo=" "
                for i in range(6):
                    codigo +=str(random.randint (0,9))
                if ChoiseSacar=="cajero" and SaldoDisponible>=2000 or ChoiseSacar=="punto fisico" and SaldoDisponible>=2000:
                    SaldoSacado=int(input(f"Usted Selecciono la opción {ChoiseSacar} y el codigo q le genero es {codigo} \nAhora,escoga cuanto dinero va a retirar\nRecuerde que su saldo actual es {SaldoDisponible}\n")) 
                    if SaldoDisponible>SaldoSacado:
                        SaldoDisponible=SaldoDisponible-SaldoSacado
                        print("Usted retiró ",SaldoSacado," De su cuenta Nequi, Su Saldo Actual Ahora es de ",SaldoDisponible,"\n") 
                    else:
                        print("Respete, no puede sacar mas dinero del que usted tiene, RECUERDE, su saldo actual es de ",SaldoDisponible,"\n")
                elif ChoiseSacar=="cajero" or ChoiseSacar=="punto fisico":
                    print("No te alcanza, solo se puede retirar dinero si tu saldo es mayor a 2000 mil pesos\n")
                else:
                    print("La opción digitada no es valida\n")
            elif ChoiseUser=="2":
                numeroEnviar=input("Digite el numero a el que enviara la transacción\n")
                valorNumero=int(input(f"Digite la cantidad de dinero que va a enviar al numero {numeroEnviar} \nSu saldo actual es de {SaldoDisponible} \n"))
                if SaldoDisponible>valorNumero:
                    SaldoDisponible=SaldoDisponible-valorNumero
                    print(f"Transacción Completada!, Usted Envió {valorNumero} a el numero {numeroEnviar}, su saldo actual ahora es {SaldoDisponible}\n")
                else:
                    print("La cantidad ingresada es mayor a el saldo que dispone,por lo tanto la transacción no pudo ser completada, su saldo es de ",SaldoDisponible,"\n")
            elif ChoiseUser=="3":
                Recargar=input("Usted seleccionó la opción de Recargar,Digite \n1. Si desea hacer la recarga\n2. Para cancelar la Recarga y volver al modo de selección\n")
                if Recargar=="1":
                    ValorRecarga=int(input(f"Su saldo actual es de {SaldoDisponible}, digite el valor a recargar\n"))
                    SaldoDisponible=SaldoDisponible+ValorRecarga
                    print("Recarga realizada con exito!... Su saldo actual ahora es de ",SaldoDisponible,"\n")
                else:
                    print("Usted seleccionó cancelar la recarga, se transladara al inicio\n")
                    repetir="s"
            elif ChoiseUser=="4":
                Plataforma=input("Escoga a que plataforma de Streaming desea Suscribirse:\n1. Netflix: Costo de 18000 mil pesos\n2. Disney: Costo de 22000 mil pesos\n3. HBO Max: costo de 15000 mil pesos\n4. Star Plus: costo de 20000 mil peso\n5. Amazon Prime Video: costo 16000 mil pesos \n6. Para Mirar Combos Disponibles A Plataformas De Streaming\n")
                if Plataforma=="1" and SaldoDisponible>=18000:
                    SaldoDisponible=SaldoDisponible-18000
                    print("Usted Selecciono Netflix, Se le descontara 18000 mil pesos de su saldo actual...¡ Disfruta de tu suscripcion !,Ahora puedes ver La Casa De Papel\n")
                elif Plataforma=="2" and SaldoDisponible>=22000:
                    SaldoDisponible=SaldoDisponible-22000
                    print("Usted Selecciono Disney, Se le descontara 22000 mil pesos de su saldo actual...¡ Disfruta de tu suscripcion !,Ahora puedes ver Toda la saga de Marvel\n")
                elif Plataforma=="3" and SaldoDisponible>=15000:
                    SaldoDisponible=SaldoDisponible-15000
                    print("Usted Selecciono HBO Max, Se le descontara 15000 mil pesos de su saldo actual...¡ Disfruta de tu suscripcion !,Ahora puedes ver The Last Of Us, Pedro Pascal Es Un Actorazo\n")
                elif Plataforma=="4" and SaldoDisponible>=20000:
                    SaldoDisponible=SaldoDisponible-20000
                    print("Usted Selecciono Star Plus, Se le descontara 20000 mil pesos de su saldo actual...¡ Disfruta de tu suscripcion !,Ahora puedes ver Los partidos de la Champions en Vivo\n")
                elif Plataforma=="5" and SaldoDisponible>=16000:
                    SaldoDisponible=SaldoDisponible-16000
                    print("Usted Selecciono La mejor opción de todas: Amazon Prime Video, Se le descontara 16000 mil pesos de su saldo actual...¡ Disfruta de tu suscripcion !,Ahora puedes ver The Boys\n")
                elif Plataforma=="1" or Plataforma=="2" or Plataforma=="3" or Plataforma=="4":
                        print("Alto Ahí, No tienes suficiente dinero para adquirir este producto, tu saldo actual es de ",SaldoDisponible,"\n") 
                elif Plataforma=="6":
                    Combos=input("Seleccione Que Combo Desea Comprar:\n1. Netflix, Disney y Star Plus: costo de 48000 mil pesos\n2. Disney y Star Plus: costo de 30000 mil pesos\n3. Netflix, Amazon y HBO Max: costo de 32000 mil pesos\n4. HBO Max y Amazon: costo de 20000 mil pesos \n")
                    if Combos=="1" and SaldoDisponible>=48000:
                        SaldoDisponible=SaldoDisponible-48000
                        print("Buena Opción, Ahora puedes disfrutar de Estas Tres Plataformas De Streaming: Netflix, Disney y Star Plus Por tan solo 48000 mil pesos, se le descontara de su saldo actual\n")
                    elif Combos=="2" and SaldoDisponible>=30000:
                        SaldoDisponible=SaldoDisponible-30000
                        print("Buena Opción, Ahora puedes disfrutar de Estas dos Plataformas De Streaming: Disney y Star Plus Por tan solo 30000 mil pesos, se le descontara de su saldo actual\n")
                    elif Combos=="3" and SaldoDisponible>=32000:
                        SaldoDisponible=SaldoDisponible-32000
                        print("Buena Opción, Ahora puedes disfrutar de Estas tres Plataformas De Streaming: Netflix,Amazon y HBO Max Por tan solo 32000 mil pesos, se le descontara de su saldo actual\n")
                    elif Combos=="4" and SaldoDisponible>=20000:
                        SaldoDisponible=SaldoDisponible-20000
                        print("Buena Opción, Ahora puedes disfrutar de Estas dos Plataformas De Streaming: Amazon y HBO Max Por tan solo 20000 mil pesos, se le descontara de su saldo actual\n")
                    elif Combos=="1" or Combos=="2" or Combos=="3" or Combos=="4":
                        print("Alto Ahí, No tienes suficiente dinero para adquirir este producto, su saldo actual es de ",SaldoDisponible,"\n")
                    else:
                        print("La opción digitada no es valida\n")
                else:
                    print("La opción digitada no es valida\n")     
            elif ChoiseUser=="5":
                Facturas=input("Seleccione q Factura desea Pagar:\n1. Telefonia: costo de 50000 mil pesos \n2. Internet:220000 mil pesos \n3. Pagar Ambos: costo de 270000 pesos\n")
                TipoTelefonia=input("Digite Que Operador es: Movistar,Claro o Tigo\n")
                if Facturas=="1" and SaldoDisponible>=50000:
                    SaldoDisponible=SaldoDisponible-50000
                    print(f"Usted es Cliente {TipoTelefonia} y Acaba de pagar La Factura De la telefonia Con Exito!..., Se le descontara de su saldo actual\n")
                elif Facturas=="2" and SaldoDisponible>=220000:
                    SaldoDisponible=SaldoDisponible-220000
                    print(f"Usted es Cliente {TipoTelefonia} y Acaba de pagar La Factura De el Internet Con Exito!..., Se le descontara de su saldo actual\n")
                elif Facturas=="3" and SaldoDisponible>=270000:
                    SaldoDisponible=SaldoDisponible=270000
                    print("Usted Pagó ambos recibos al operador ",TipoTelefonia,"Se le descontara de su saldo actual \n")
                elif Facturas=="1" or Facturas=="2" or Facturas=="3":
                    print("Las Facturas van a seguir en deudas porque no le alcanza con su saldo actual pagarlas,su saldo actual es de ",SaldoDisponible,"\n")
                else:
                    print("La opción digitada no es valida\n")
            elif ChoiseUser=="6":
                repetir=input("Usted Escogió la opción de salir, digite s si desea volver al selector o cualquier otra tecla para salir de la aplicación\n")
            else:
                print("La opción digitada no es valida\n")
        break
    else:
        print(f"¡Upps! Parece que tus datos de acceso no son correctos, Tienes {i} intentos más\n")

    
