'''Exercício 1 
Considere que o arquivo “notas.CSV” apresenta uma listagem com os dados dos alunos de uma turma. 
Cada linha do arquivo apresenta os dados de um aluno, no formato: 
RM,NOME,NOTA1,NOTA2,NOTA3,NOTA4
Implemente um programa que leia o arquivo indicado e, a partir desse arquivo, gere dois novos 
arquivos:
• Arquivo “aprovados.CSV” contendo uma listagem dos alunos aprovados na disciplina, contendo 
RM,NOME,MEDIA do aluno 
• Arquivo “reprovados.CSV” contendo uma listagem dos nomes dos alunos reprovados na 
disciplina, contendo RM,NOME,MEDIA do aluno. 
Para o aluno ser aprovado ele deve ter média igual ou superior a 6.0'''

with open('notas.csv', 'r') as arquivo:
    aprovados = open('aprovados.csv', 'w')
    aprovados.write('RM;NOME;MEDIA\n')
    reprovados = open('reprovado.csv', 'w')
    reprovados.write('RM;NOME;MEDIA\n')

    cont = 1
    for linha in arquivo:
        if cont > 1:
            lista = linha.split(';')
            notas = lista[-4:]
            print(notas)
            soma = 0
            for n in notas:
                soma += float(n)
            media = soma / 4
            print(f'{media:.2f}')
            if media >= 6:
                aprovados.write(f'{lista[0]};{lista[1]};{media:.2f}\n')
            else:
                reprovados.write(f'{lista[0]};{lista[1]};{media:.2f}\n')
        cont += 1
