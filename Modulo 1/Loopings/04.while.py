# Crie um codigo que faça a conversao de moeda do real para dólar e vice-versa

# Etapas da resolução:
# 1) Criar uma variável chamada cotacao
# 2) Solicitar ao usuário a opção de conversão desejada
# 3) Apresentar o resultado da conversão da moeda
# 4) Perguntar se ele deseja continuar a conversão


letra = 's'
while letra == 's':
    cotacao = float(input('Digite a cotação do dólar: '))
    print('-'*50)
    print(f'-'*15, 'Escolha a Opção','-'*18)
    print('-'*50)

    opcao = int(input('1 - Converter dolar para real | 2 - Conversor real para dolar: '))

    if opcao == 1:
        valor = float(input('Digite o valor em dolar a ser convertido para real U$: '))
        resultado = valor * cotacao
        print(f'O valor em reais é : {resultado:.2f}')
    elif opcao == 2:
        valor1= float(input('Digite o valor em real a ser convertido para dolar R$: '))
        resultado1 = valor1/ cotacao
        print(f'O valor em dolar é : {resultado1:.2f}')
    else:
        print('Digite uma opção válida.')
    letra = input('Deseja continuar? (s/n): ').lower()