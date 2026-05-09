print('''
==PREFEITURA MUNICIPAL DE IGUATU==

 1. Secretaria de Obras
 2. Secretaria de Frotas
 3. Secretaria de Educação ''')

opc = int(input("Digite a secretaria que deseja consultar: "))

match opc:
  case 1:
    print('''
---SECRETARIA DE OBRAS---

 1. Pavimentação
 2. Reforma
 3. Construção  ''')

    opc1 = int(input("Qual recurso deseja consultar?: "))

    match opc1:
      case 1:
        areaP = float(input("Digite o valor da área que será pavimentada em m²: "))
        if areaP > 1000:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ {120 * areaP}.
Status: Será necessária a licitação estadual. ''')
        elif areaP <= 1000 and areaP >= 1:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ {120 * areaP}.
Status: Será necessária a licitação municipal.''')
        else:
          print("Valor inválido, tente novamente.")
      case 2:
        areaR = float(input("Digite o valor da área que será reformada em m²: "))
        if areaR > 500:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ {80 * areaR}.
Status: O engenheiro será obrigatório.''')
        elif areaR <= 500 and areaR >= 1:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ {80 * areaR}.
Status: O engenheiro é opcional.''')
        else:
          print("Valor inválido, tente novamente.")
      case 3:
        areaC = float(input("Digite o valor da área que será construída em m²: "))
        if areaC > 300:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ {200 * areaC}.
Status: O projeto estrutural será obrigatório.''')
        elif areaC <= 300 and areaC >=1:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ {200 * areaC}.
Status: O projeto estrutural é opcional.''')
        else:
          print("Valor inválido, tente novamente.")
      case _:
          print("Valor não reconhecido, tente novamente.")
  case 2:
    print('''
    ---SECRETARIA DE FROTAS---

     1. Carro
     2. Caminhão
     3. Máquina pesada ''')

    opc2 = int(input("Qual recurso deseja consultar?: "))

    match opc2:
      case 1:
        km1 = float(input("Insira a quilometragem do transporte: "))
        if km1 > 100000:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ 300,00.
Status: Será necessária a manutenção completa.''')
        elif km1 <= 100000 and km1 >= 1:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ 150,00.
Status: Será necessária a manutenção simples. ''')
        else:
          print("Valor inválido, tente novamente.")
      case 2:
        km2 = float(input("Insira a quilometragem do transporte: "))
        if km2 > 200000:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ 800,00.
Status: Será necessária a troca estrutural.''')
        elif km2 <=200000 and km2 >= 1:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ 400,00.
Status: Será necessário o reparo superficial.''')
        else:
          print("Valor inválido, tente novamente.")
      case 3:
        km3 = float(input("Insira a quilometragem do transporte: "))
        if km3 > 150000:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ 1.500,00.
Status: Será necessário parar a operação e realizar um reparo completo.''')
        elif km3 <= 150000 and km3 >= 1:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: 750,00.
Status: A máquina pode continuar em operação, mas necessita de uma revisão.''')
        else:
          print("Valor inválido, tente novamente.")
      case _:
          print("Valor não reconhecido, tente novamente.")
  case 3:
    print(f'''
    ---SECRETARIA DE EDUCAÇÃO---

     1. Merenda
     2. Transporte
     3. Reforma Escolar ''')

    opc3 = int(input("Qual recurso deseja consultar?: "))

    match opc3:
      case 1:
        alunos = int(input("Qual a quantidade de alunos?: "))
        if alunos > 500:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ {alunos * 5}.
Status: O contrato será anual. ''')
        elif alunos <= 500 and alunos >= 1:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ {alunos * 5}.
Status: O contrato será semestral. ''')
        else:
          print("Valor inválido, tente novamente.")
      case 2:
        distancia = float(input("Qual a distância em km?: "))
        if distancia > 50:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ {distancia * 12}.
Status: Será necessário um novo veículo. ''')
        elif distancia <= 50 and distancia >=1:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ {distancia * 12}.
Status: Será necessário um reparo no veículo. ''')
        else:
          print("Valor inválido, tente novamente.")
      case 3:
        sala = int(input("Digite a quantidade de salas: "))
        if sala > 10:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ {2000 * sala}.
Status: Será necessário uma licitação. ''')
        elif sala <= 10 and sala >=1:
          print(f'''
             ═══════ RESPOSTA ═══════

Valor estimado: R$ {2000 * sala}.
Status: A licitação é opcional, aguarde as instruções municipais. ''')
        else:
          print("Valor inválido, tente novamente.")
      case _:
          print("Valor não reconhecido, tente novamente.")
  case _:
     print("Valor não reconhecido, tente novamente.")