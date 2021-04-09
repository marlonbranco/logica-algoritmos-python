def validaInt(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, "wt+")
        a.close()
    except:
        print("Erro na criação do arquivo.")
    else:
        print("Arquivo {} foi criado com sucesso!\n".format(nomeArquivo));

def arquivoExiste(nomeArquivo):
    try:
        a = open(nomeArquivo, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def cadastraJogo(nomeArquivo, nomeJogo, plataforma):
    try:
        a = open(nomeArquivo, "at")
    except:
        print("Erro ao abrir o arquivo")
    else:
        a.write("{} - {}\n".format(nomeJogo, plataforma))
        print("Jogo cadastrado com sucesso!\n")
    finally:
        a.close()

def listaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, "rt")
    except:
        print("Erro ao ler o arquivo.")
    else:
        print(a.read())
    finally:
        a.close()

# Programa principal.
arquivo = "games.txt"

if arquivoExiste(arquivo):
    print("Arquivo localizado no computador!\n")
else:
    print("Arquivo não encontrado!\n")
    criaArquivo(arquivo)

while True:
    print("MENU")
    print("1 - Cadastrar jogo.")
    print("2 - Listar jogos.")
    print("3 - Sair do programa.")

    operacao = validaInt("Escolha a opção desejada: ", 1, 3)
    if operacao == 1:
        print("Opção de cadastrar jogo selecionada... \n")
        nomeJogo = input("Nome do jogo: ")
        plataforma = input("Plataforma: ")
        cadastraJogo(arquivo, nomeJogo, plataforma)
    elif operacao == 2:
        print("Opção de listar jogos selecionada... \n")
        listaArquivo(arquivo)
    elif operacao == 3:
        print("Encerrando o programa...")
        break