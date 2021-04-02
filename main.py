# Aula prática 3
# Exercício 1
# soma1 = (2 + 2) < 4
# print(soma1)
# divisao = (7 // 3) == 1+1
# print(divisao)
# potencia = (3 ** 2) + (4 ** 2) == 25
# print(potencia)
# soma2 = (2 + 4 + 6) > 12
# print(soma2)

# Exercício 2
# if (idade > 60):
#     print("Você pode receber o benefício!")
# if (dano > 10 and escudo == 0):
#     print("Você está morto!")
# if (norte  or sul  or lest or oeste):
#     print("Você escapou!")

# Exercício 3 - Condicional Composta
# if(ano % 4 == 0):
#     print("Pode ser um ano bissexto!")
# else:
#     print("Definitivamente não é um ano bissexto")
#
# if(x and y):
#     print("Decida-se!")
# else:
#     print("Você escolheu um caminho!")

# Exercício 1 material
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

# Exercício 2 material
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

# Exercício 3 material
consumo = float(input("Digite a quantidade consumida em kWh:"))
print("Tipos de instalações:")
print("R para residências.")
print("I para indústrias.")
print("C para comércios.")
instalacao = input("Digite o tipo da sua instalação:")
if instalacao == "R" or instalacao == "I" or instalacao == "C":
    if instalacao == "R":
        if consumo <= 500:
            fatura = consumo * 0.4
            print("Valor da fatura de energia: R$ {}".format(fatura))
        elif consumo > 500:
            fatura = consumo * 0.65
            print("Valor da fatura de energia: R$ {}".format(fatura))
    elif instalacao == "I":
        if consumo <= 1000:
            fatura = consumo * 0.55
            print("Valor da fatura de energia: R$ {}".format(fatura))
        elif consumo > 1000:
            fatura = consumo * 0.60
            print("Valor da fatura de energia: R$ {}".format(fatura))
    elif instalacao == "c":
        if consumo <= 5000:
            fatura = consumo * 0.55
            print("Valor da fatura de energia: R$ {}".format(fatura))
        elif consumo > 5000:
            fatura = consumo * 0.60
            print("Valor da fatura de energia: R$ {}".format(fatura))
else:
    print("Opção inválida.")
print("Encerrando o programa.")