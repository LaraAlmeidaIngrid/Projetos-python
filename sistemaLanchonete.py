print ('''
===LANCHONETE===
''')

valorTotal = 0
pedido = ""

while True:
   opc = int(input('''
─CARDÁPIO─

1. Lanches
2. Bebidas
3. Sobremesas
4. Finalizar o pedido

➜ O que deseja pedir?: '''))
   match opc:
    case 1:
     lanche = int(input('''
⸺ LANCHES ⸺

1. Hambúrguer - R$ 12.00
2. X-Salada   - R$ 15.00
3. Hot Dog    - R$ 10.00

➜ Qual lanche deseja pedir?: '''))
     match lanche:
      case 1:
       quantHamb = int(input('''
➜ Quantos hambúrgueres você deseja?: '''))
       if quantHamb <= 0:
        print(f'''
─── Valor indefinido, tente novamente ───''')
       else:
        valorHamb = quantHamb * 12
        valorTotal += valorHamb
        pedido += f"{quantHamb}x Hambúrger.\n"
        print(f'''
O lanche escolhido foi: {quantHamb}x Hambúrger.
O valor do lanche foi: R$ {valorHamb}.''')
      case 2:
       quantXsal = int(input('''
➜ Quantos x-saladas você deseja?: '''))
       if quantXsal <= 0:
        print(f'''
─── Valor indefinido, tente novamente ───''')
       else:
        valorXsal = quantXsal * 15
        valorTotal += valorXsal
        pedido += f"{quantXsal}x X-Salada.\n"
        print(f'''
O lanche pedido foi: {quantXsal}x X-Salada.
O valor do lanche foi: R$ {valorXsal}.''')
      case 3:
       quantHdog = int(input('''
➜ Quantos hot dogs você deseja?: '''))
       if quantHdog <= 0:
        print(f'''
─── Valor indefinido, tente novamente ───''')
       else:
        valorHdog = quantHdog * 10
        valorTotal += valorHdog
        pedido += f"{quantHdog}x Hot Dog.\n"
        print(f'''
O lanche pedido foi: {quantHdog}x Hot Dog.
O valor do lanche foi: R$ {valorHdog}.''')
      case _:
       print(f'''
── Este valor não foi reconhecido, tente novamente ──''')
    case 2:
     bebida = int(input('''
⸺ BEBIDAS ⸺

1. Refrigerante - R$ 06.00
2. Suco         - R$ 05.00
3. Água         - R$ 03.00

➜ Qual bebida deseja pedir?: '''))
     match bebida:
      case 1:
       quantRef = int(input('''
➜ Quantos refrigerantes você deseja?: '''))
       if quantRef <= 0:
        print(f'''
─── Valor indefinido, tente novamente ───''')
       else:
        valorRef = quantRef * 6
        valorTotal += valorRef
        pedido += f"{quantRef}x Refrigerante.\n"
        print(f'''
A bebida escolhida foi: {quantRef}x Refrigerante.
O valor da bebida foi: R$ {valorRef}.''')
      case 2:
       quantSuco = int(input('''
➜ Quantos sucos você deseja?: '''))
       if quantSuco <= 0:
        print(f'''
─── Valor indefinido, tente novamente ───''')
       else:
        valorSuco = quantSuco * 5
        valorTotal += valorSuco
        pedido += f"{quantSuco}x Suco.\n"
        print(f'''
A bebida escolhida foi: {quantSuco}x Suco.
O valor da bebida foi: R$ {valorSuco}.''')
      case 3:
       quantAgua = int(input('''
➜ Quantas águas você deseja?: '''))
       if quantAgua <= 0:
        print(f'''
─── Valor indefinido, tente novamente ───''')
       else:
        valorAgua = quantAgua * 3
        valorTotal += valorAgua
        pedido += f"{quantAgua}x Água.\n"
        print(f'''
A bebida escolhida foi: {quantAgua}x Água.
O valor da bebida foi: R$ {valorAgua}.''')
      case _:
       print(f'''
── Este valor não foi reconhecido, tente novamente ──''')
    case 3:
     sobr = int(input('''
⸺ SOBREMESAS ⸺

1. Sorvete - R$ 8.00
2. Bolo    - R$ 7.00
3. Pudim   - R$ 6.50

➜ Qual sobremesa deseja pedir?: '''))
     match sobr:
      case 1:
       quantSorv = int(input('''
➜ Quantos sorvetes você deseja?: '''))
       if quantSorv <= 0:
        print(f'''
─── Valor indefinido, tente novamente ───''')
       else:
        valorSorv = quantSorv * 8
        valorTotal += valorSorv
        pedido += f"{quantSorv}x Sorvete.\n"
        print(f'''
A sobremesa pedida foi: {quantSorv}x Sorvete.
O valor da sobremesa foi: R$ {valorSorv}.''')
      case 2:
        quantBolo = int(input('''
➜ Quantos bolos você deseja?: '''))
        if quantBolo <= 0:
         print(f'''
─── Valor indefinido, tente novamente ───''')
        else:
         valorBolo = quantBolo * 7
         valorTotal += valorBolo
         pedido += f"{quantBolo}x Bolo.\n"
         print(f'''
A sobremesa pedida foi: {quantBolo}x Bolo.
O valor da sobremesa foi: R$ {valorBolo}.''')
      case 3:
        quantPudim = int(input('''
➜ Quantos pudins você deseja?: '''))
        if quantPudim <= 0:
         print(f'''
─── Valor indefinido, tente novamente ───''')
        else:
         valorPudim = quantPudim * 6.50
         valorTotal += valorPudim
         pedido += f"{quantPudim}x Pudim.\n"
         print(f'''
A sobremesa pedida foi: {quantPudim}x Pudim.
O valor da sobremesa foi: R$ {valorPudim}.''')
    case 4:
     if valorTotal == 0:
      print(f'''
──Nenhum pedido foi realizado.──''')
     else:
      print(f'''
O pedido foi: {pedido}
Valor do pedido: R$ {valorTotal}.
Obrigada pelo seu pedido, em breve estará pronto! ( ദ്ദി ˙ᗜ˙ )''')
      break
    case _:
     print("Este valor não foi reconhecido, tente novamente. ")
     continue