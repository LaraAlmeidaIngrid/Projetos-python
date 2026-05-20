import random
print(16*'--')
print('Simulador de Viagem Interestelar')
print(16*'--')

nome = input('''
SEJA BEM-VINDO AO NOSSO PROGRAMA DE VIAGEM ESPACIAL 🪐
             
🠆 Digite o seu nome: ''')

print(f'Nome em maiúsculo: {nome.upper()}')
print(f'Nome em minúsculo: {nome.lower()}')
print(f'Total de letras: {len(nome)-nome.count(' ')}')
nomeSep = nome.split()
print(f'''Primeiro nome: {nomeSep[0]}
Total de letras: {len(nomeSep[0])}''')

destino = input('''
DESTINOS DISPONÍVEIS 🪐

1. Marte 
2. Júpiter
3. Espaço Sideral

🠆 Digite o nome do destino: ''').upper().strip()

if destino == 'MARTE' or destino == '1':
 nome_destino = 'Marte'
 distancia = 1.5
 precoUA = 10000
 status = '\033[32mCondições climáticas estáveis\033[m'
elif destino == 'JÚPITER' or destino == '2' or destino == 'JUPITER':
 nome_destino = 'Júpiter'
 distancia = 5.2
 precoUA = 7000
 status = '\033[31mGrandes tempestades mágneticas, trajes pesados são obrigatórios!\033[m'
else:
 nome_destino = 'Espaço profundo'
 distancia = 8
 precoUA = 8500
 status = '\033[33mRota em estágio de mapeamento\033[m'

precoFinal = distancia * precoUA

naves = ['Alpha','Beta','Gamma']
nave = random.choice(naves)

print('-- BILHETE ESPACIAL --')
print(f'''
-------------------------------
PASSAGEIRO: {nomeSep[0]}.
NAVE: {nave}.
-------------------------------
ROTA:

► DESTINO: {nome_destino}.
► DISTÂNCIA: {distancia}.
► PREÇO POR UA: R$ {precoUA}.
-------------------------------
VALOR TOTAL: \033[1;36mR$ {precoFinal:.2f}\033[m
STATUS: {status}.
-------------------------------
Obrigada por utilizar nossos serviços, desejamos uma viagem intergaláctica a todos! 🛸
''')