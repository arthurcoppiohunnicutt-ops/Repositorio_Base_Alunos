# Crie um programa que some todos os numeros impares 
# que sao multiplos de 3 e 1 a 30 e apresente o resultado.

# Etapas para resolucao
# 1) criar um for de para captar os numeros impares 
# 2) criar uma condicional para checar se o numero é multiplo de 3 
# 3) somar os numeros que atende a condicional
# 4) apresentar os resultados

multiplo_tres = 0 # variavel que ira receber os numeros impares e multiplos de 3

for i in range(1,31,2): # contagem dos numeros impares
    if i % 3 == 0: # checagem se os numeros dao multiplos
        print(i,  end=",") # apresentacao dos numeros que atendem os requisitos (na mesma linha, separados por virgula)
        multiplo_tres += i
print() # pular uma linha
print(f"A soma dos numeros impares multiplos de 3 neste intervalo é {multiplo_tres}.")