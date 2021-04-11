# Função que valida se o número está entre os intervalos definidos
def validaInt(pergunta, min, max):
    codigo = int(input(pergunta)) # Recebe o código do produto e converte para inteiro
    # Porque a validação do intervalo só pode ser feita com valor inteiro
    while (codigo < min) or (codigo > max):
        # Continuará rodando até que o usuário digite um número válido
        codigo = int(input(pergunta))
    return codigo # Retorna o código verificado que está dentro do intervalo

def criaLista(codigo, peso):
    # Cria uma lista com os números do código do produto e do peso
    strCodigo = str(codigo) # Converte o código para String para que ele possa ser iterado
    lista = [[], []]
    # Cria uma lista com 2 posições vazias
    # A posição [0] conterá a lista com os números do código do produto
    # A posição [1] conterá a lista com os números do peso
    for codigo in strCodigo: # Itera o código do produto, extraindo cada número
        intCodigo = int(codigo) # Converte o código para inteiro novamente
        lista[0].append(intCodigo) # Anexa cada número do código a lista do
    lista.insert(1, peso) # Insere na variável lista, a variável peso com os números do peso
    return lista # Retorna a lista com os números do código do produto e do peso

def calculaCodigoVerificador(tabela):
    # Função que recebe a tabela com o código do produto em uma lista na posição [0]
    # os peso em uma lista também na posição [1], e calcula o código verificador
    j = 0 # Iterador para a tabela na posição [1] onde está o peso do produto
    acumulador = 0 # Acumulador do resultado de cada multiplicação na tabela
    for i in tabela[0]:
        # Laço de repetição que itera na posição [0] que é onde está o código do produto
        acumulador += i * tabela[1][j] # Acumula o resultado da multiplicação pelo peso
        j += 1 # Incrementa o iterador do peso
    codigoVerificador = acumulador % 7 # Calcula o resto da divisão entre o acumulador e 7
    return codigoVerificador # Retorna o resultado da multiplicação acima

# Programa principal
peso = [2,3,4,5,6] # Lista com os pesos definidos no escopo

# Variável que obtem o código do produto e valida se está entre [10000, 30000]
codigoProduto = validaInt("Digite o código do produto entre 10000 e 30000: ", 10000, 30000)

# Chama a função criaLista e obtém a lista
# passando como parâmetro o 'codigoProduto' e o 'peso'
lista = criaLista(codigoProduto, peso)
# Chama a função calculaCodigoVerificador e obtém o código verificador
# passando como parâmetro a variável 'lista'
codigoVerificador = calculaCodigoVerificador(lista)
# Escreve o códigoFinal do produto com o codigoProduto e seu codigoVerificador
print("{}-{}".format(codigoProduto, codigoVerificador))

