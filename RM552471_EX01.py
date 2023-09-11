planoAssinatura = input ("Informe seu plano de assinatura: BASIC, SILVER, GOLD ou PLATINUM.")

faturaAnual = float(input("Informe o faturamento anual do seu canal:"))

if planoAssinatura.upper() == "BASIC":

    porcent = ( 30.0 / 100.0) 
    anuidade = porcent * faturaAnual
    print("Sua anuidade é: {}." .format(anuidade))
   

elif planoAssinatura.upper() == "SILVER":

    porcent = ( 20.0 / 100.0) 
    anuidade = porcent * faturaAnual
    print("Sua anuidade é: {}." .format(anuidade))

elif planoAssinatura.upper() == "GOLD":

    porcent = ( 10.0 / 100.0) 
    anuidade = porcent * faturaAnual
    print("Sua anuidade é: {}." .format(anuidade))

elif planoAssinatura.upper() == "PLATINUM":

    porcent = ( 5.0 / 100.0) 
    anuidade = porcent * faturaAnual
    print("Sua anuidade é: {}." .format(anuidade))

else:
    print("Plano não reconhecido")


