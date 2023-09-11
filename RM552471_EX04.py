minuto = int(input("Qual minuto está marcando na máquina? "))
resultado=1
i=1

while i <= minuto:
    resultado *= i
    i += 1

print(" A senha é LIBERDADE{}".format(resultado))




