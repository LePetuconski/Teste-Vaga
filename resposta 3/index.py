import json

with open('./dados.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)

aux = 0
maiorFaturamento = 0
menorFaturamento = 0
somaTotal = 0
mediaTotal = 0

for dia in data:

    if (dia['valor']) != 0:

        aux = dia['valor']

        if (aux > maiorFaturamento):
            maiorFaturamento = aux

        if (menorFaturamento == 0):
            menorFaturamento = aux
        elif (aux < menorFaturamento):
            menorFaturamento = aux

        somaTotal += dia['valor']


mediaTotal = somaTotal / len(data)
diasFaturamento = ''

for i in data:
    if (i['valor']) != 0:
        if (i['valor']) > mediaTotal:
           diasFaturamento += (str(i['dia']) + ' ')

print('''
    O maior faturamento do mês foi de: R$ {0}
    O menor faturamento do mês foi de: R$ {1}
    Dias em que o faturamento diário foi superior à média mensal: {2}
'''.format(maiorFaturamento, menorFaturamento, diasFaturamento))
    
file.close()