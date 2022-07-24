faturamentos = {
    "sp": 67836.43,
    "rj": 36678.66,
    "mg": 29229.88,
    "es": 27165.48,
    "outros": 19849.53
}

total = sum(faturamentos.values())

for key, value in faturamentos.items():
	porcentagem = str(round((100 * value / total), 2)) + '%'
	print('Porcentagem do faturamento de {0}: {1}'.format(key.upper(), porcentagem))
