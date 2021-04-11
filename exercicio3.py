def validaNota(pergunta, min, max):
    nota = float(input(pergunta)) # Recebe a nota do aluno e converte para inteiro
    # Porque a validação do intervalo só pode ser feita com um valor int ou float
    while (nota < min) or (nota > max):
        # Continuará rodando até que o usuário digite uma nota válida
        nota = float(input(pergunta))
    return nota # Retorna a nota verificada que está dentro do valor mínimo e máximo

def calculaMedia(notas): # Função que recebe as notas e calcula a média
    acumulador = 0 # Acumula a soma das notas
    for nota in notas: # Itera a lista de notas obtendo cada nota
        acumulador += nota; # Soma ao acumulador cada nota iterada
    media = acumulador / 4 # Calula a média das notas dividindo o acumulador por 4
    return media # Retorna a variável com o valor da média

def verificaSituacaoAluno(media): # Função que verifica a situação do aluno
    if media < 7: # Se a média do aluno for menor do que 7
        return "Reprovado" # A função retorna 'Reprovado'
    elif media >= 7: # Se a média do aluno for maior ou igual a 7
        return "Aprovado" # A função retorna 'Aprovado'

def formataNotas(alunoNotas): # Formata as notas do aluno em formato String
    notasString =  [str(nota) for nota in alunoNotas]
    # Itera cada nota do aluno e a converte para string
    stringDeNotas = " ".join(notasString) # Formata as notas em uma linha de strings
    return stringDeNotas; # Retorna as notas formatadas para impressão na tela

# Programa principal
alunoNotas = [] # Lista vazia de alunos para a inserção

while True: # Estrutura de repetição que repete a cada inserção de aluno
    notaMin = 0 # Variável de nota mínima
    notaMax = 10 # Variável de nota máxima
    nome = input("Digite o nome do aluno: ") # Obtém o nome do aluno
    n1 = validaNota("Digite a primeira nota: ", notaMin, notaMax)
    n2 = validaNota("Digite a segunda nota: ", notaMin, notaMax)
    n3 = validaNota("Digite a terceira nota: ", notaMin, notaMax)
    n4 = validaNota("Digite a quarta nota: ", notaMin, notaMax)
    # As variáveis n1, n2, n3 e n4 chamam a função validaNota que verifica
    # se o usuário inseriu uma nota dentro dos valores de notaMin e notaMax
    notas = [n1, n2, n3, n4] # Lista com as notas do aluno
    media = calculaMedia(notas)
    # Chama a função calculaMedia passando como parâmetro as notas
    situacaoAluno = verificaSituacaoAluno(media)
    # Chama a função verificaSituacaoAluno passando como parâmetro a media
    dicionarioAluno = {"nome": nome, "notas": notas, "situação": situacaoAluno}
    # Cria um dicionário com os dados do aluno
    alunoNotas.append(dicionarioAluno)
    # Adiciona o dicionarioAluno a variável alunoNotas

    sair = input("Você deseja adicionar mais um aluno e suas notas? [S/N]")
    if sair.upper() in "N":
        # Converte o caracter inserido na variável 'sair' para maíúsculo
        # Verifica se o usuário digitou a letra 'N'
        # Em seguida finaliza o programa se o usuário digitar a letra 'N'
        break
    if sair.upper() not in "S":
        # Converte o caracter inserido na variável 'sair' para maíúsculo
        # Verifica se o usuário digitar outro caracter diferente de 'S'
        # Ele será orientado a digitar 'S' ou 'N'
        print("Digite 'S' para SIM ou 'N' para NÃO.")

print("Notas dos Alunos") # Titulo da impressão das notas
print("-" * 40) # Cria uma linha com 40 hífens
for aluno in alunoNotas: # Estrutura de repetição que itera a lista alunoNotas
    notas = formataNotas(aluno["notas"])
    # Chama a função formataNotas que converte a lista de notas para uma string
    print("{}   {}   {}".format(aluno["nome"], notas, aluno["situação"]))
    # Finalmente imprime cada aluno em uma listagem com nome, notas e situação.


