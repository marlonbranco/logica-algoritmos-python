# Aula prática 2
# Exercício 1
precoProduto = float(input('Digite o preço do produto: '))
percentualDesconto = float(input('Digite o percentual de desconto (0-100)%: '))

desconto = precoProduto * (percentualDesconto / 100)
precoFinal = precoProduto - desconto
print('O preço do produto é {}. Desconto de {}%'.format(precoProduto, percentualDesconto))
print('Valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto,precoFinal))

# Exercício 2
diaria = 60.0
precoKm = 0.15

diasAlugados = float(input('Digite quantos dias o carro foi alugado: '))
kmPercorrido = float(input('Digite quantos kilômetros foram percorridos: '))

precoFinal = (diaria * diasAlugados) + (precoKm * kmPercorrido);

print('Você alugou o carro por {} dias a R${} a diária'.format(diasAlugados, diaria))
print('E percorreu {}km custando R${}/km'.format(kmPercorrido, precoKm))
print('O preco final do aluguel do carro ficou em R${}'.format(precoFinal))

# Exercício 3

frase = input('Digite uma frase: ')
tamanho = len(frase)

frase2 = frase[:int(tamanho/2)]

print(frase2[-2:])

# Aula 3 Condicionais
# Exercício 1
x = int(input("Digite um número:"))
y = int(input("Digite outro número:"))
if(x > y) :
   print("O número {} é maior que {}.".format(x,y))

# Exercício 2
x = int(input("Digite um número inteiro:"))
if (x % 2 == 0):
    print("O número {} é par.".format(x))
else:
   print("O número {} é impar".format(x))

# Exercício de expressões lógicas
x = 10
y = 1
z = 5.5
res = x > y and z == y
print(res)

# Exercício de notas

m1 = float(input("Digite sua primeira nota:"))
m2 = float(input("Digite sua segunda nota:"))
m3 = float(input("Digite sua terceira nota:"))
if m1 >= 7 and m2 >= 7 and m3 >= 7:
   print("O aluno está aprovado!")
else:
   print("O aluno foi reprovado")

# Exercício de condicionais aninhadas
maca = 2.30
laranja = 3.60
banana = 1.85

print("Qual fruta você deseja comprar?")
print("Digite 1 para maça.")
print("Digite 2 para laranja.")
print("Digite 3 para banana.")
fruta = int(input("Digite o número da fruta escolhida:"))
quantidade = int(input("Agora digite a quantidade desejada:"))
if fruta == 1:
   total = maca * quantidade
   print("O preço total ficou em R${}".format(total))
else:
#    if fruta == 2:
       total = laranja * quantidade
       print("O preço total ficou em R${}".format(total))
   else:
       if fruta == 3:
           total = banana * quantidade
           print("O preço total ficou em R${}".format(total))
       else:
           print("Produto inexistente!")

# Mesmo exercício porém resolvido com condicionais de múltipla escolha
maca = 2.30
laranja = 3.60
banana = 1.85

print("Qual fruta você deseja comprar?")
print("Digite 1 para maça.")
print("Digite 2 para laranja.")
print("Digite 3 para banana.")
fruta = int(input("Digite o número da fruta escolhida:"))
quantidade = int(input("Agora digite a quantidade desejada:"))
if fruta == 1:
   total = maca * quantidade
   print("O preço total ficou em R${}".format(total))
elif fruta == 2:
   total = laranja * quantidade
   print("O preço total ficou em R${}".format(total))
elif fruta == 3:
   total = banana * quantidade
   print("O preço total ficou em R${}".format(total))
else:
   print("Produto inexistente.")

# Exercício de input de nome e idade
nome = input("Digite um nome:")
idade = int(input("Digite a sua idade:"))
if nome == "Marlon":
   print("Olá Marlon")
elif idade < 18:
       print("Você é menor de idade.")
elif idade > 100:
       print("Esta pessoa provavelmente não existe.")
