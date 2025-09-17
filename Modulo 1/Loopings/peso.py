# Crie um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lido.

# Etapas para resolucao:
# 1) crie uma lista vazia para receber os pesos
# 2) crie um for para receber os pesos das 5 pessoas.
# 3) adicione os pesoso recebidos a lista
# 4) utilize a funcao max() e min() ou ordene a lista e busque o primeiro e o ultimo elemento
# 5) apresente os resultados

pesos = []

for i in range(5):
    peso = float(input("Informe seu peso em Kg:"))
    if peso > 0: 
        pesos.append(peso)
    else: 
        print('Valor inválido.')
print(f'A lista dos pesos em Kg:{pesos}')  

maior_peso = max(pesos)
menor_peso = min(pesos)
print(f"O maior peso é {maior_peso} Kg e o menor peso é {menor_peso} Kg.")


# outra maneira de resolver o maior e o menor
#pesos.sort()
#menor =pesos[0]
#maior = pesos [-1]
#print(f"O maior peso é {maior} Kg e o menor peso é {menor} Kg.")