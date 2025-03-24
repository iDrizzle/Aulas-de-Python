print("Olá, mundo") #print exibe na tela, texto string

nome = input("Digite seu nome: ")
print("Olá, " +  nome + "!")

idade = int(input("Digite sua idade: "))
print("Ano que vem você terá", idade + 1)



numero = int(input("Digite um número: "))

if numero > 0: #se
    print("O número é positivo.")
elif numero < 0: #se não/se
    print("O número é negativo.")
else: #se não
    print("O número é zero.")



for i in range(5):
    print("Número:", i)

#📌 O que faz?
#Repete um bloco de código várias vezes.
#📝 Explicação:
#range(5) → Cria uma sequência de 0 a 4.
#for i in range(5) → Faz i percorrer esses valores e executa o bloco para cada um.

contador = 1
while contador <= 3:
    print("Contagem:", contador)
    contador += 1  # Soma 1 ao contador

#📌 O que faz?
#Repete um bloco de código enquanto uma condição for verdadeira.
#📝 Explicação:
#while contador <= 3 → Enquanto contador for menor ou igual a 3, o código será repetido.
#contador += 1 → A cada repetição, soma 1 ao contador para evitar um loop infinito.

frase = "Python é incrível"
tamanho = len(frase)
print("A frase tem", tamanho, "caracteres.")

#📌 O que faz?
#Conta a quantidade de caracteres em um texto ou itens em uma lista.
#📝 Explicação:
#len(frase) retorna o número de caracteres no texto.

def saudacao(nome):
    print("Olá,", nome)

saudacao("Maria")

#📌 O que faz?
#Cria uma função personalizada para reutilizar código.
#📝 Explicação:
#def saudacao(nome): → Define uma função chamada saudacao, que recebe um nome.
#saudacao("Maria") → Chama a função e exibe a saudação.

frutas = ["Maçã", "Banana", "Uva"]
print(frutas[0,2])  # Mostra a segunda fruta

#📌 O que faz?
#Armazena vários valores dentro de uma única variável.
#📝 Explicação:
#frutas[1] → Pega o item da posição 1 (lembrando que começa do 0).


dict

pessoa = {"nome": "Carlos", "idade": 30}
print(pessoa["nome"])  # Acessa o nome

#📌 O que faz?
#Armazena pares de chave e valor, como um "banco de dados pequeno".
#📝 Explicação:
#pessoa["nome"] retorna "Carlos" porque "nome" é uma chave.


# print()	Exibe mensagens na tela
# input()	Pede informações do usuário
# int(), float()	Converte texto para número
# if, elif, else	Estruturas condicionais
# for	Laço de repetição com contador
# while	Laço de repetição com condição
# len()	Conta caracteres ou itens de uma lista
# def	Cria funções reutilizáveis
# list[]	Armazena vários valores (listas)
# dict{}	Armazena pares de chave e valor (dicionários)