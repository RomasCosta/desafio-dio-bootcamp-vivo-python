menu = """
=================== Menu =========================
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair
===================================================

 => """

saldo = 0.0
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

  opcao = input(menu)

  if opcao == 'd':
      
    valor = float(input('Informe o valor do depósito: \n'))

    if valor < 0:
      print('Valor inválido para depósito, insira um valor a partir de R$ 0.01')

    else:
      saldo += valor
      extrato += f'Depósito de: R${valor:.2f}\n'

  elif opcao == 's':
      
    valor = float(input('Informe o valor do saque: \n'))
    
    if saldo > 0 and saldo >= valor:
        if numero_saques < LIMITE_SAQUES and valor <= limite:
          saldo -= valor
          extrato += f'Saque de: R${valor:.2f}\n'
          numero_saques += 1

        else:
            print('Verifique o motivo do erro abaixo: \n')
            print(f'Você atingiu o limite de saques diário que são 3.\nSaques feitos hoje: {numero_saques}\nOu ultrapassou o valor do limite por saque que é de R$ 500.00.\nTentativa de saque:{valor: .2f}')

    else:
      print(f'Você não tem saldo suficiente, seu saldo atual e: {saldo: .2f}')

  elif opcao == 'e':
    if extrato == "":
      print('Você não tem movimentações')

    else:
      print(f'\n{extrato}\nSaldo atual: {saldo: .2f}\nNúmero de saques feitos hoje: {numero_saques}')

  elif opcao == 'q':
    print('Obrigado pela sua presenca!')

    break

  else:
    print('Entrada inválida!')
