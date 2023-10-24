'''Exercício 2 
Considere o arquivo “foods.CSV”, com três colunas: "name" (nome), "id" (identificação) e "favorite food" 
(comida favorita).
Cada linha representa um indivíduo com suas respectivas informações. 
Escreve um programa que leia esse arquivo e informe a comida preferida pela maioria das pessoas.'''


with open('foods.csv', 'r') as arquivo:
    dicionario = {}
    conta_linha = 1
    for linha in arquivo:
        if conta_linha > 1:             # ignora a primeira linha do arquivo
            lista = linha.split(';')
            prato = lista[2].replace('\n', '')
            if prato in dicionario:
                dicionario[prato] += 1
            else:
                dicionario[prato] = 1
        conta_linha += 1

maior = 0
prato = ''
for chave, valor in dicionario.items():
    if valor > maior:
        maior = valor
        prato = chave
print(f'{prato}: {maior}')