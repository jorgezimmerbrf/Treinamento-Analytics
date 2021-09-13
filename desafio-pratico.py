ano_atual = 2021

nome = input('Qual o seu nome?\n')
idade = int(input('Qual é a sua idade?\n'))
altura = float(input('Qual é a sua altura?\n'))
peso = float(input('Qual é o seu peso?\n'))

ano_nascimento = ano_atual - idade
imc = peso / (altura**2)
classificacao = ''
if imc < 16:
    classificacao = 'Subpeso Severo'
elif imc >= 16 and imc < 20:
    classificacao = 'Subpeso'
elif imc >= 20 and imc < 25:
    classificacao = 'Peso Normal'
elif imc >= 25 and imc < 30:
    classificacao = 'Sobrepeso'
elif imc >= 30 and imc < 40:
    classificacao = 'Obesidade'
elif imc >= 40:
    classificacao = 'Obesidade Mórbida'


print(f"Olá, {nome}!\nSeu ano de nascimento é {ano_nascimento} e seu IMC é {imc:.2f} ({classificacao}).")
