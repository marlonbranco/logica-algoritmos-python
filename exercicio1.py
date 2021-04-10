# Função que verifica a Categoria do lutador
def verificaCategoria(pesoLutador):
    if peso < 65: # Verifica se é da categoria Pena
        return "Pena"
    elif 65 <= peso < 72: # Verifica se é da categoria Leve
        return "Leve"
    elif 72 <= peso < 79: # Verifica se é da categoria Ligeiro
        return "Ligeiro"
    elif 79 <= peso < 86: # Verifica se é da categoria Meio-médio
        return "Meio-médio"
    elif 86 <= peso < 93: # Verifica se é da categoria Médio
        return "Médio"
    elif 93 <= peso < 100: # Verifica se é da categoria Meio-pesado
        return "Meio-pesado"
    elif peso >= 100: # Verifica se é da categoria Pesado
        return "Pesado"

# Programa principal
while True:
    # Estrutura de repetição While, continuará executando
    # até que o usuário deseje finalizar o programa
    sair = input("Você deseja verificar a cadegoria um lutador? [S/N]")
    if sair.upper() in "N":
        # Converte o caracter inserido na variável 'sair' para maíúsculo
        # Verifica se o usuário digitou a letra 'N'
        # Em seguida finaliza o programa se o usuário digitar a letra 'N'
        break
    if sair.upper() not in "S":
        # Converte o caracter inserido na variável 'sair' para maíúsculo
        # Verifica se o usuário digitar outro caracter diferente de 'S'
        # Ele será orientado a digitar 'S' ou 'N'
        print("Digite 'S' para 'SIM' e 'N' para 'NÃO'.")

    nome = input("Digite o nome do lutador: ")
    # Recebe o nome do lutador
    peso = float(input("Digite o peso do lutador: "))
    # Recebe o peso do lutador e converte para ponto flutuante
    categoria = verificaCategoria(peso)
    # Chama a função verificaCategoria passando o peso como parâmetro
    print("O lutador {} pesa {} Kg e se enquadra na categoria {}.".format(nome,peso,categoria))
print("Encerrando o programa...")