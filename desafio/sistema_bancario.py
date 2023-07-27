menu = """

[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 450
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
           saldo += valor
           extrato += f"Depósito: R$ {valor:.2f}\n"

        else :
          print("Operaçaõ falhou! O valor informado é invalido")  

    elif opcao == "s":
        valor = float(input("informe o valro do saque :"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >=LIMITE_SAQUES

        if excedeu_saldo:
           print("Operação falhou! Voce não tem saldo suficiente.")

        elif excedeu_limite:
           print("Operação falhou! O valro do saque excede o limite.")

        elif excedeu_saques:
           print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0 :
           saldo -= valor
           extrato += f"Saque: R$ {valor:.2f}\n"
           numero_saques +=1       
        
        else :
           print("Operação falhou! O valor informado é invalido.")

    elif opcao == "e":

     print("EXTRATO".center(60,"="))
     print("Não foram realizadas movimentações." if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("".center(60,"="))
      
    elif opcao == "q":
       print(" Obrigado por utilizar nosso sistema!")
       break

    else:
       print("Operação inválida, por favor selecione novamente a operação desejada.")    