def saque(saldo, valor):
    saldo -= valor
    print(f"Saque de R${valor:.2f} efetuado com sucesso!\nSaldo atual R${saldo:.2f}")
    return saldo

def deposito(saldo, valor):
    saldo += valor
    print(f"Depósito de R${valor:.2f} efetuado com sucesso!\nSaldo atual R${saldo:.2f}")
    return saldo

def extrato(historico, saldo):
    print("\n================EXTRATO================")
    print("Não foram realizadas movimentações." if historico == "" else historico)
    print("======================================")
    print(f"SALDO R${saldo:.2f}\n")

saldo = 1500.00
limite = 500.00
numero_saques = 0
LIMITE_SAQUES = 3
historico = ""

menu = """\n
================MENU================
[1] SAQUE
[2] DEPÓSITO
[3] EXTRATO
[4] SAIR
====================================
=> """

while True:
    opcao = input(menu)

    if opcao == '1':
        valor = float(input("Informe o valor do saque: "))
        if valor > saldo:
            print("Saldo insuficiente para saque.")
        elif valor > limite:
            print(f"Valor do saque excede o limite permitido.\nSeu limite é R${limite:.2f}.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques diários atingido.")
        elif valor <= 0:
            print("Valor inválido para saque.")
        else:
            saldo = saque(saldo, valor)
            numero_saques += 1
            historico += f"DÉBITO R${valor:.2f}\n"

    elif opcao == '2':
        valor = float(input("Informe o valor do depósito: "))
        if valor <= 0:
            print("Valor inválido para depósito.")
        else:
            saldo = deposito(saldo, valor)
            historico += f"CRÉDITO R${valor:.2f}\n"

    elif opcao == '3':
        extrato(historico, saldo)

    elif opcao == '4':
        print("Obrigado por usar nosso sistema bancário. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
