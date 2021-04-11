from operator import itemgetter

def validaIdade(pergunta, min, max):
    idade = int(input(pergunta)) # Recebe a idade do contato e converte para inteiro
    # Porque a validação do intervalo só pode ser feita com um valor int ou float
    while (idade < min) or (idade > max):
        # Continuará rodando até que o usuário digite uma idade válida
        idade = idade(input(pergunta))
    return idade # Retorna a idade verificada que está dentro do valor mínimo e máximo

# Programa principal
contatos = [] # Lista vazia que receberá os contatos

while True: # Estrutura de repetição que repete a cada inserção de contato
    nome = input("Digite o nome do contato: ") # Obtém o nome do contato
    if not nome:
        # Verifica se o usuário inseriu alguma informação em na variável nome
        # Em seguida finaliza o programa se o usuário
        # não digitar nada e pressionar 'Enter'
        break
    idade = validaIdade("Digite a idade do contato: ", 0, 130)
    # Recebe a idade pela função validaIdade que valida a idade do contato
    telefone = input("Digite o número de telefone: ")
    # Recebe o número de telefone do contato

    contato = {"nome": nome, "idade": idade, "telefone": telefone}
    # Cria o dicionário do contato com seus respectivos dados
    contatos.append(contato)
    # Adiciona o dicionário do contato ao dicionário de contatos

contatos.sort(key=itemgetter('nome'));
# Ordena a lista de contatos, utilizando o método .sort()
# Junto com o método itemgetter da biblioteca operator
# Ela é utilizada para acessar o item específico, neste caso a key 'nome'

print("Todos os contatos por ordem alfabética")
print("-" * 40) # Cria uma linha com 40 hífens
for contato in contatos:
    # Estrutura de repetição que itera a lista de contatos imprimindo cada um
    print("{} - {} - {}".format(contato["nome"], contato["idade"], contato["telefone"]))

contatosMenores = {"menoresDe18": []}
# Dicionário que receberá os contatos menores de idade
contatosMaiores = {"maioresDe18": []}
# Dicionário que receberá os contatos maiores de idade

for contato in contatos:
    # Estrutura de repetição que itera a lista de contatos
    # Verificando a idade e adicionando ao seu respectivo dicionário
    if contato["idade"] < 18: # Verifica se o contato é menor de idade
        contatosMenores["menoresDe18"].append(contato)
        # Adiciona o contato ao dicionário contatosMenores
    if contato["idade"] >= 18: # Verifica se o contato é maior de idade
        contatosMaiores["maioresDe18"].append(contato)
        # Adiciona o contato ao dicionário contatosMaiores

print("-" * 40)
print("Todos menores de 18 anos")
print("-" * 40)
for contato in contatosMenores["menoresDe18"]:
    # Estrutura de repetição que itera a lista de contatos menores imprimindo cada um
    print("{} - {} - {}".format(contato["nome"], contato["idade"], contato["telefone"]))

print("-" * 40)
print("Todos maiores de 18 anos")
print("-" * 40)
for contato in contatosMaiores["maioresDe18"]:
    # Estrutura de repetição que itera a lista de contatos maiores imprimindo cada um
    print("{} - {} - {}".format(contato["nome"], contato["idade"], contato["telefone"]))