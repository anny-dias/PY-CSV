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



with open('notas.csv', 'r') as arquivo:         # arquivo para leitura
    
    aprovados = open('aprovados.csv', 'w')      # arquivo para escrita
    aprovados.write('RM,NOME,MEDIA\n')          # escreve primeira linha
    reprovados = open('reprovado.csv', 'w')     # arquivo para escrita
    reprovados.write('RM,NOME,MEDIA\n')         # escreve primeira linha

    cont_linha = 1
    for linha in arquivo:                   # percorre linhas do arquivo
        if cont_linha > 1:                  # exclui primeira linha
            lista = linha.split(',')
            lista_notas = lista[-4:]        # gera lista com as notas

            soma = 0                        # calcular media
            for nota in lista_notas:        
                soma += float(nota)
            media = soma / 4
            print(f'Notas: {lista_notas}\t Média: {media:.2f}')
            
            if media >= 6:
                aprovados.write(f'{lista[0]},{lista[1]},{media:.2f}\n')     # escreve no arquivo
            else:
                reprovados.write(f'{lista[0]},{lista[1]},{media:.2f}\n')    # escreve no arquivo
        cont_linha += 1