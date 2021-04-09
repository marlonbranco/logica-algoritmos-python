# # Aula prática 2
# # Exercício 1
# precoProduto = float(input('Digite o preço do produto: '))
# percentualDesconto = float(input('Digite o percentual de desconto (0-100)%: '))
#
# desconto = precoProduto * (percentualDesconto / 100)
# precoFinal = precoProduto - desconto
# print('O preço do produto é {}. Desconto de {}%'.format(precoProduto, percentualDesconto))
# print('Valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto,precoFinal))
#
# # Exercício 2
# diaria = 60.0
# precoKm = 0.15
#
# diasAlugados = float(input('Digite quantos dias o carro foi alugado: '))
# kmPercorrido = float(input('Digite quantos kilômetros foram percorridos: '))
#
# precoFinal = (diaria * diasAlugados) + (precoKm * kmPercorrido);
#
# print('Você alugou o carro por {} dias a R${} a diária'.format(diasAlugados, diaria))
# print('E percorreu {}km custando R${}/km'.format(kmPercorrido, precoKm))
# print('O preco final do aluguel do carro ficou em R${}'.format(precoFinal))
#
# # Exercício 3
#
# frase = input('Digite uma frase: ')
# tamanho = len(frase)
#
# frase2 = frase[:int(tamanho/2)]
#
# print(frase2[-2:])
#
# # Aula 3 Condicionais
# # Exercício 1
# x = int(input("Digite um número:"))
# y = int(input("Digite outro número:"))
# if(x > y) :
#    print("O número {} é maior que {}.".format(x,y))
#
# # Exercício 2
# x = int(input("Digite um número inteiro:"))
# if (x % 2 == 0):
#     print("O número {} é par.".format(x))
# else:
#    print("O número {} é impar".format(x))
#
# # Exercício de expressões lógicas
# x = 10
# y = 1
# z = 5.5
# res = x > y and z == y
# print(res)
#
# # Exercício de notas
#
# m1 = float(input("Digite sua primeira nota:"))
# m2 = float(input("Digite sua segunda nota:"))
# m3 = float(input("Digite sua terceira nota:"))
# if m1 >= 7 and m2 >= 7 and m3 >= 7:
#    print("O aluno está aprovado!")
# else:
#    print("O aluno foi reprovado")
#
# # Exercício de condicionais aninhadas
# maca = 2.30
# laranja = 3.60
# banana = 1.85
#
# print("Qual fruta você deseja comprar?")
# print("Digite 1 para maça.")
# print("Digite 2 para laranja.")
# print("Digite 3 para banana.")
# fruta = int(input("Digite o número da fruta escolhida:"))
# quantidade = int(input("Agora digite a quantidade desejada:"))
# if fruta == 1:
#    total = maca * quantidade
#    print("O preço total ficou em R${}".format(total))
# else:
# #    if fruta == 2:
#        total = laranja * quantidade
#        print("O preço total ficou em R${}".format(total))
#    else:
#        if fruta == 3:
#            total = banana * quantidade
#            print("O preço total ficou em R${}".format(total))
#        else:
#            print("Produto inexistente!")
#
# # Mesmo exercício porém resolvido com condicionais de múltipla escolha
# maca = 2.30
# laranja = 3.60
# banana = 1.85
#
# print("Qual fruta você deseja comprar?")
# print("Digite 1 para maça.")
# print("Digite 2 para laranja.")
# print("Digite 3 para banana.")
# fruta = int(input("Digite o número da fruta escolhida:"))
# quantidade = int(input("Agora digite a quantidade desejada:"))
# if fruta == 1:
#    total = maca * quantidade
#    print("O preço total ficou em R${}".format(total))
# elif fruta == 2:
#    total = laranja * quantidade
#    print("O preço total ficou em R${}".format(total))
# elif fruta == 3:
#    total = banana * quantidade
#    print("O preço total ficou em R${}".format(total))
# else:
#    print("Produto inexistente.")
#
# # Exercício de input de nome e idade
# nome = input("Digite um nome:")
# idade = int(input("Digite a sua idade:"))
# if nome == "Marlon":
#    print("Olá Marlon")
# elif idade < 18:
#        print("Você é menor de idade.")
# elif idade > 100:
#        print("Esta pessoa provavelmente não existe.")
# # Aula prática 3
# # Exercício 1
# soma1 = (2 + 2) < 4
# print(soma1)
# divisao = (7 // 3) == 1+1
# print(divisao)
# potencia = (3 ** 2) + (4 ** 2) == 25
# print(potencia)
# soma2 = (2 + 4 + 6) > 12
# print(soma2)
#
# # Exercício 2
# if (idade > 60):
#     print("Você pode receber o benefício!")
# if (dano > 10 and escudo == 0):
#     print("Você está morto!")
# if (norte  or sul  or lest or oeste):
#     print("Você escapou!")
#
# # Exercício 3 - Condicional Composta
# if(ano % 4 == 0):
#     print("Pode ser um ano bissexto!")
# else:
#     print("Definitivamente não é um ano bissexto")
#
# if(x and y):
#     print("Decida-se!")
# else:
#     print("Você escolheu um caminho!")
#
# # Exercício 1 material
# lado1 = float(input("Informe o primeiro lado do triângulo:"))
# lado2 = float(input("Informe o segundo lado do triângulo:"))
# lado3 = float(input("Informe o terceiro lado do triângulo:"))
#
# if (lado1 > 0 and lado2 > 0 and lado3 > 0):
#     if(lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1):
#         if(lado1 == lado2 and lado2 == lado3):
#             print("É um triângulo equilátero.")
#         elif(lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
#             print("É um triângulo isósceles.")
#         else:
#             print("É um triângulo escaleno.")
#     else:
#         print("Este não é um triângulo!")
# else:
#     print("Este não é um triângulo!")
#
# # Exercício 2 material
# adicao = "+"
# subtracao = "-"
# multiplicacao = "*"
# divisao = "/"
# print("CALCULADORA")
# print("+ Adição.")
# print("- Subtração.")
# print("* Multiplicação.")
# print("/ Divisão.")
# print("Pressione outra tecla para sair.")
# operacao = input("Digite a operação desejada:")
# if operacao == adicao or operacao == subtracao or operacao == multiplicacao or operacao == divisao:
#     valor1 = int(input("Digite o primeiro valor:"))
#     valor2 = int(input("Digite o segundo valor:"))
#     if operacao == adicao:
#         resultado = valor1 + valor2
#         print("Resultado: {} + {} = {}".format(valor1, valor2, resultado))
#     elif operacao == subtracao:
#         resultado = valor1 - valor2
#         print("Resultado: {} - {} = {}".format(valor1, valor2, resultado))
#     elif operacao == multiplicacao:
#         resultado = valor1 * valor2
#         print("Resultado: {} * {} = {}".format(valor1, valor2, resultado))
#     elif operacao == divisao:
#         resultado = valor1 / valor2
#         print("Resultado: {} / {} = {}".format(valor1, valor2, resultado))
#     else:
#         print("Operação invalida.")
# print("Encerrando o programa.")
#
# # Exercício 3 material
# consumo = float(input("Digite a quantidade consumida em kWh:"))
# print("Tipos de instalações:")
# print("R para residências.")
# print("I para indústrias.")
# print("C para comércios.")
# instalacao = input("Digite o tipo da sua instalação:")
# if instalacao == "R" or instalacao == "I" or instalacao == "C":
#     if instalacao == "R":
#         if consumo <= 500:
#             fatura = consumo * 0.4
#             print("Valor da fatura de energia: R$ {}".format(fatura))
#         elif consumo > 500:
#             fatura = consumo * 0.65
#             print("Valor da fatura de energia: R$ {}".format(fatura))
#     elif instalacao == "I":
#         if consumo <= 1000:
#             fatura = consumo * 0.55
#             print("Valor da fatura de energia: R$ {}".format(fatura))
#         elif consumo > 1000:
#             fatura = consumo * 0.60
#             print("Valor da fatura de energia: R$ {}".format(fatura))
#     elif instalacao == "c":
#         if consumo <= 5000:
#             fatura = consumo * 0.55
#             print("Valor da fatura de energia: R$ {}".format(fatura))
#         elif consumo > 5000:
#             fatura = consumo * 0.60
#             print("Valor da fatura de energia: R$ {}".format(fatura))
# else:
#     print("Opção inválida.")
# print("Encerrando o programa.")
# # Estruturas de repetição
# x = 1
# while (x <= 5):
#     print(x)
#    x += 1
# # Exercício 1 - acumuladores - aula 4
# soma = 0;
# cont = 1;
# while (cont <= 5):
#     x = float(input("Digite a {}ª nota: ".format(cont)));
#     soma += x;
#     cont += 1;
# media = soma / cont;
# print("Média final: {}".format(media));
#
# # Exercício 2 - condicionais - aula 4
# x = int(input("Digite um valor inteiro e positivo: "));
#
# while ( x <= 0 ):
#     x = int(input("Digite um valor inteiro e positivo: "));
# print("Você digitou {}. Encerrando o programa...".format(x));
#
# # Exercício 3 - break - aula 4
# print("Digite uma mensagem que irei repetir para você:");
# print("Para encerrar escreva 'sair'");
# while True:
#     texto = input('');
#     print(texto);
#     if(texto == 'sair'):
#         break
# print("Encerrando o programa...")
#
# # Exercício 4 - continue - aula 4
# while True:
#     nome = input("Qual é o seu nome?");
#     if(nome != "Marlon"):
#         continue
#     senha = input("Qual é a sua senha?");
#     if(senha == "senhadificil"):
#         break
# print("Acesso concedido.")
#
# # Exercício 5 - Truthy e Falsy - aula 4
# nome = ''
# while not nome:
#     nome = input("Digite seu nome:")
# valor = int(input("Digite um número qualquer:"));
# if valor:
#     print("Você digitou um valor diferente de zero.")
# else:
#     print("Você digitou zero.")
#
# # Estrutura de repetição - for
# for i in range(6):
#     print(i)
#
# # for com 3 parâmetros
# for i in range(1, 6, 1):
#     print(i)
#
# for i in range(10, 0, -2):
#     print(i)
#
# # Exercicio 6 - for - aula 4
# soma = 0
# qtd = 0
# for i in range(1, 101):
#     if( i % 2 == 0):
#         soma += i
#         qtd += 1
# media = soma / qtd
# print("A média dos números pares de 1 até 100 é: {}".format(media))
#
# # Exercício 7 - estruturas de repetições aninhadas - aula 4
# # 2 while
# tabuada = 1
# while tabuada <= 10:
#     print('TABUADA DO {}:'.format(tabuada))
#     i = 1
#     while i <= 10:
#         print('{} x {} = {}'.format(tabuada, i, tabuada * i))
#         i += 1
#     tabuada += 1
#
# # 2 for
# for tabuada in range(1, 11, 1):
#     print('TABUADA DO {}:'.format(tabuada))
#     for i in range(1, 11, 1):
#         print('{} x {} = {}'.format(tabuada, i, tabuada * i))
#
# # 1 while e 1 for
# tabuada = 1
# while tabuada <= 10:
#     print('TABUADA DO {}:'.format(tabuada))
#     for i in range(1, 11, 1):
#         print('{} x {} = {}'.format(tabuada, i, tabuada * i))
#     tabuada += 1

## Aula pática 4
## Exercício 1 - estruturas de repetições
## letra A
# x = 3
# while x < 13:
#     print(x)
#     x += 1
# for i in range(3, 13, 1):
#     print(i)

## letra B
# x = 0
# while x < 9:
#     print(x)
#     x += 2
# for i in range(0, 9, 2):
#     print(i)
# adicao = "+"
# subtracao = "-"
# multiplicacao = "*"
# divisao = "/"

## Exercício 2 Aula Prática 4
# adicao = "+"
# subtracao = "-"
# multiplicacao = "*"
# divisao = "/"
# print("CALCULADORA")
# print("+ Adição.")
# print("- Subtração.")
# print("* Multiplicação.")
# print("/ Divisão.")
# print("Digite 'sair' para encerrar o programa.")

# operacao = input("Digite a operação desejada:")

# if operacao == adicao or operacao == subtracao or operacao == multiplicacao or operacao == divisao:
#     valor1 = int(input("Digite o primeiro valor:"))
#     valor2 = int(input("Digite o segundo valor:"))

# while (operacao != 'sair'):
#     if operacao == adicao:
#         resultado = valor1 + valor2
#         print("Resultado: {} + {} = {}".format(valor1, valor2, resultado))
#     elif operacao == subtracao:
#         resultado = valor1 - valor2
#         print("Resultado: {} - {} = {}".format(valor1, valor2, resultado))
#     elif operacao == multiplicacao:
#         resultado = valor1 * valor2
#         print("Resultado: {} * {} = {}".format(valor1, valor2, resultado))
#     elif operacao == divisao:
#         resultado = valor1 / valor2
#         print("Resultado: {} / {} = {}".format(valor1, valor2, resultado))
#     else:
#         print("Operação invalida.")
#
#     operacao = input("Digite a operação desejada:")
#     if (operacao == adicao) or (operacao == subtracao) or (operacao == multiplicacao) or (operacao == divisao):
#         valor1 = int(input("Digite o primeiro valor:"))
#         valor2 = int(input("Digite o segundo valor:"))
#
# print("Encerrando o programa.")

## Segunda maneira
# adicao = "+"
# subtracao = "-"
# multiplicacao = "*"
# divisao = "/"
# print("CALCULADORA")
# print("+ Adição.")
# print("- Subtração.")
# print("* Multiplicação.")
# print("/ Divisão.")
# print("Digite 'sair' para encerrar o programa.")
#
# while True:
#     operacao = input("Digite a operação desejada:")
#     if operacao == adicao or operacao == subtracao or operacao == multiplicacao or operacao == divisao:
#         valor1 = int(input("Digite o primeiro valor:"))
#         valor2 = int(input("Digite o segundo valor:"))
#
#     if operacao == adicao:
#         resultado = valor1 + valor2
#         print("Resultado: {} + {} = {}".format(valor1, valor2, resultado))
#         continue
#     elif operacao == subtracao:
#         resultado = valor1 - valor2
#         print("Resultado: {} - {} = {}".format(valor1, valor2, resultado))
#         continue
#     elif operacao == multiplicacao:
#         resultado = valor1 * valor2
#         print("Resultado: {} * {} = {}".format(valor1, valor2, resultado))
#         continue
#     elif operacao == divisao:
#         resultado = valor1 / valor2
#         print("Resultado: {} / {} = {}".format(valor1, valor2, resultado))
#         continue
#     elif operacao == "sair":
#         break
#     else:
#         print("Operação invalida.")
#
# print("Encerrando o programa.")

## Exercício 3 - Aula prática 4
# valor = int(input("Digite o valor em R$: "));
# while True:
#     if valor >= 100:
#         cedulas100 = valor // 100
#         valor -= cedulas100 * 100
#         print("Cédulas de 100: {}".format(cedulas100))
#         if not valor:
#             break
#     if valor >= 50:
#         cedulas50 = valor // 50
#         valor -= cedulas50 * 50
#         print("Cédulas de 50: {}".format(cedulas50))
#         if not valor:
#             break
#     if valor >= 20:
#         cedulas20 = valor // 20
#         valor -= cedulas20 * 20
#         print("Cédulas de 20: {}".format(cedulas20))
#         if not valor:
#             break
#     if valor >= 5:
#         cedulas5 = valor // 5
#         valor -= cedulas5 * 5
#         print("Cédulas de 5: {}".format(cedulas5))
#         if not valor:
#             break
#     if valor:
#         cedulas1 = valor
#         print("Cédulas de 1: {}".format(cedulas1))
#         break

## Exercício 4 - Aula prática 4
# totalPessoas = 0
# totalIngressos = 0
# totalIdades = 0
#
# print("Venda de ingressos para o Cinema.")
# print("Digite 'sair' para finalizar o programa.")
#
# while True:
#     idade = input('Insira a idade: ')
#     if idade == 'sair':
#         break
#     idade = int(idade)
#     if idade < 3:
#         ingresso = 0
#         print("Ingresso gratuíto!")
#     else:
#         if idade > 12:
#             ingresso = 30
#             print("Valor do ingresso: R$ {}".format(float(ingresso)))
#         else:
#             ingresso = 15
#             print("Valor do ingresso: R$ {}".format(float(ingresso)))
#
#     totalPessoas += 1
#     totalIngressos += ingresso
#     totalIdades += idade
#
# mediaIdades = totalIdades / totalPessoas
#
# print("Total de pessoas: {}".format(totalPessoas))
# print("Valor total dos ingressos: R${}".format(float(totalIngressos)))
# print("A média das idades é: {}".format(totalPessoas))

## Aula 5 - funções
# def borda(palavra):
#     tamanho = len(palavra)
#
#     if tamanho:
#         print("+" + "-" * tamanho + "+")
#         print("|" + palavra + "|")
#         print("+" + "-" * tamanho + "+")
#
# borda("Python é muito legal!")

## Exercício 2 - Aula 5
# def validaString(palavra, min, max):
#     s1 = input(palavra)
#     tam = len(s1)
#     while ((tam < min) or (tam > max)):
#         s1 = input(palavra)
#         tam = len(s1)
#     print("Palavra validada")
#
#     return s1
#
# x = validaString("Digite uma palavra:", 10, 30)
# print("Você digitou a string {}. \n Dado válido. Encerrando o programa...".format(x))

## Exemplos de tratamento de excessões
# while True:
#     try:
#         numero = int(input("Digite um número:"))
#     except ValueError:
#         print("Oops! Número inválido. Tente novamente.")

# def divisao():
#     try:
#         valor1 = int(input('Digite o primeiro valor: '))
#         valor2 = int(input('Digite o segundo valor: '))
#         resultado = valor1 / valor2
#     except ZeroDivisionError:
#         print('Oops! Erro de divisão por 0...')
#     except:
#         print('Algo deu errado.')
#     else:
#         return resultado
#     finally:
#         print("Sempre executará!")
#
# print(divisao())

## Funções dentro de funções
# def imprimeComCondicao(num, fcond):
#     if fcond(num):
#         print(num)
#
# def par(x):
#     return x % 2 == 0;
# def impar(x):
#     return not par(x);
#
# imprimeComCondicao(6, par)

## Função lambda
# res = lambda x: x * x;
# print(res(5))

# soma = lambda x, y: x + y
# print(soma(10,15))

## Aula prática 5 - Docstrings
# def soma(x = 0,y = 0,z = 0):
#     """
#     Função que soma até 3 valores inteiros.
#     :param x: Parâmetro opcional.
#     :param y: Parâmetro opcional.
#     :param z: Parâmetro opcional.
#     :return: Retorna o resultado da soma dos 3 valores.
#     """
#     return x + y + z
#
# print(soma(1,2,3))
# help(soma)

## Exercício 1 - Aula prática 5
# def validaInt(pergunta, min, max):
#     x = int(input(pergunta))
#     while ((x < min) or (x > max)):
#         x = int(input(pergunta))
#     return x
#
# def fatorial(num):
#     """
#     Função que calcula a fatorial de um número.
#     :param num: Número a ser calculado.
#     :return: Retorna a fatorial.
#     """
#     fat = 1
#     if num == 0:
#         return fat
#     for i in range(1, num + 1, 1):
#         fat *= i;
#     return fat
#
# x = validaInt("Digite o número que deseja calcular a fatorial: ", 0, 50)
# print("{}! = {}".format(x,fatorial(x)))
