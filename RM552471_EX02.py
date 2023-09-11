print("Insira a seguir o total de votos para cada dia da semana:")
segunda = int(input("Total de votos para segunda-feira"))
terca = int(input("Total de votos para terça-feira"))
quarta = int(input("Total de votos para quarta-feira"))
quinta = int(input("Total de votos para quinta-feira"))
sexta = int(input("Total de votos para sexta-feira"))

lista = [segunda, terca, quarta, quinta, sexta]

if (segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta ):
    print("Segunda-feira teve o maior número de votos! Com {} votos. Total de votos de cada dia da semana de segunda á sexta : {}".format(segunda, lista))

elif (segunda < terca and terca > quarta and terca > quinta and terca > sexta ):
    print("Terça-feira teve o maior número de votos! Com {} votos. Total de votos de cada dia da semana de segunda á sexta : {}".format(terca))

elif (quarta > segunda and terca < quarta and quarta > quinta and quarta > sexta ):
    print("Quarta-feira teve o maior número de votos! Com {} votos. Total de votos de cada dia da semana de segunda á sexta : {}".format(quarta, lista))

elif (quinta > segunda and terca < quinta and quarta < quinta and quinta > sexta ):
    print("Quinta-feira teve o maior número de votos! Com {} votos. Total de votos de cada dia da semana de segunda á sexta : {}".format(quinta, lista))

elif (sexta > segunda and terca < sexta and sexta > quinta and sexta > quarta ):
    print("Sexta-feira teve o maior número de votos! Com {} votos. Total de votos de cada dia da semana de segunda á sexta : {}".format(sexta, lista))

else:
    print("Empate! Por favor refaça a votação. Total de votos de cada dia da semana de segunda á sexta : {}".format(lista))

