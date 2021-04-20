import numpy as np
# N = 3
n = 3
# Criando um array de n x n+1 e inicializando com zero para guardar a matriz
matriz = np.zeros((n, n + 1))

# Criando um array de tamanho n e inicializando com zero para guardar o vetor da solução
x = np.zeros(n)

# # Leitura de coeficientes de matriz
# print("Digite 1 para digitar os valores")
# print("Digite 2 gerar valores aleatorios")
# print("Digite 3 para usar valores criados pelo próprio programa")
# print("Digite 4 para sair do programa")

# entrada = input()




#

def escreveMatriz(m):
    for i in range(n):
        for j in range(n + 1):
            print('|', matriz[i][j], '|', '\t\t', end='')
        print("\n")

        print()


matriz = [[1, 2, 3, 97], [4, 5, 6, 98], [7, 8, 9, 99]]

SEGUNDAmatriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 4):
        matriz[i][j] = float(input('X[' + str(i) + '][' + str(j) + ']='))

for i in range(0, 3):
    for j in range(0, 3):
        SEGUNDAmatriz[i][j] = matriz[i][j]

print('-> Matriz de coeficientes do sistema:')
escreveMatriz(matriz)

for etapa in range(len(matriz) - 1):

    pivot = matriz[etapa][etapa]
    for i in range(etapa + 1, len(matriz)):
        if abs(matriz[i][etapa]) > abs(pivot):
            linhaPivotamento = i
            pivot = matriz[i][etapa]
            AUX = matriz[etapa]
            matriz[etapa] = matriz[linhaPivotamento]
            matriz[linhaPivotamento] = AUX

    for i in range(etapa + 1, len(matriz)):
        c = matriz[i][etapa] / pivot
        for j in range(len(matriz) + 1):
            matriz[i][j] = (matriz[i][j]) - c * (matriz[etapa][j])

aux = 0
r = [[0, 0, 0]]

r[0][2] = matriz[len(matriz) - 1][len(matriz)] / matriz[len(matriz) - 1][len(matriz) - 1]
r[0][1] = (matriz[1][3] - (matriz[1][2] * r[0][2])) / matriz[1][1]
r[0][0] = matriz[0][3] - (matriz[0][1] * r[0][1]) - (matriz[0][2] * r[0][2])
r[0][0] = r[0][0] / matriz[0][0]

print('Resultado')

print(r)

print('\nMatriz finalizada: ')
for i in range(n):
    for j in range(n + 1):
        print('|', matriz[i][j], '|', '\t\t', end='')
    print("\n")

x = np.linalg.det(SEGUNDAmatriz)
if (x == 0):
    res = 'Possivel indeterminado'
elif (x != 0):
    res = 'Possivel determinado'
else:
    res = 'Impossível determinado'

print("Tipo:", {res})
