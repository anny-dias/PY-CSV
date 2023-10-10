alunos = {}

with open('arquivo.csv', 'r') as arquivo:
    cont = 1 
    for linha in arquivo:
        if cont > 1:
            lista = linha.split(',')
            print(lista)
            alunos[int(lista[0])] = lista[1].replace('\n','')
        cont += 1
print(alunos)