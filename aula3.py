import random

letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
caracteres_especiais = "!@#$%^&*()-_=+"

todostodos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais

tamanho = int(input("Digite o tamanho da senha desejada: "))

senha = "".join(random.sample(todos_caracteres, tamanho))

print("Senha gerada:", senha)

# biblioteca de caracteres para a senha
# Junta todos os caracteres possíveis
# Pede ao usuário o tamanho da senha
# Gera a senha aleatória