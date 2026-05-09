saldo = 1000

while True:
 opc = int(input('''
- CAIXA ELETRÔNICO -

1. Ver Saldo.
2. Depositar.
3. Sacar.
4. Sair.

Digite o que deseja consultar: '''))
 match opc:
  case 1:
   print(f'''
Seu saldo atual é de: R$ {saldo}.''')
  case 2:
   depositar = float(input(f'''
Digite o valor que deseja depositar: '''))
   if depositar == 0:
    print('''
-Não houve nenhum valor depositado.''')
   elif depositar < 0:
    print('''
-Valor inválido, tente novamente.''')
    continue
   else:
    saldo += depositar
    print(f'''
O valor depositado foi: R$ {depositar}.
O saldo atual é: R$ {saldo}.''')
  case 3:
   sacar = float(input('''
Digite o valor que deseja sacar: '''))
   if sacar > saldo:
    print('''
-Saldo insuficiente.''')
   elif sacar == 0:
    print('''
-Nenhum valor foi sacado.''')
   elif sacar < 0:
    print('''
-Valor inválido, tente novamente.''')
    continue
   else:
    saldo -= sacar
    print(f'''
O valor sacado foi: R$ {sacar}.
Seu saldo atual é: R$ {saldo}.''')
  case 4:
   print('''
-Sistema fechado, obrigada por utilizar nossos serviços!''')
   break