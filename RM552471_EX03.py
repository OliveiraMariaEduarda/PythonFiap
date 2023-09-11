print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPAR ")
notaTotal = 0.0
for x in range(1,50,2):
    alunosImpares = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}.".format(x)))
    notaTotal = notaTotal + alunosImpares
    mediaImpar = notaTotal/25
   
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES ")
notaTotal = 0.0
for x in range(2,51,2):
    alunosPares = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}.".format(x)))
    notaTotal = notaTotal + alunosPares
    mediaPar = notaTotal/25
   
if mediaImpar < mediaPar:
    print("A maior média é do grupo Par {}".format(mediaPar))
elif mediaImpar > mediaPar:
    print("A maior média é do grupo ímpar {}".format(mediaImpar))
else:
    print("Média de notas iguais! Média do grupo ímpar {}, média do grupo par {}.".format(mediaImpar, mediaPar))


    
