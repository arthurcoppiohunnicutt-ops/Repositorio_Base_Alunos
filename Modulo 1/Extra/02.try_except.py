num1= input("Digite o primeiro numero: ")
num2= input("Digite o segundo numero: ")

try:
    num1 = int(num1)
    num2 = int(num2)

    print(f"Soma dos numeros é {num1 +num2}")
except:
    print("Digite um número correto.")