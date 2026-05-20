p = float(input('Qual o valor do produto? R$: '))

desc = p - (p * 5 / 100)

print('O produto que custava R$ {:.2f}, com desconto de 5%, passa a custar R$ {:.2f}'.format(p, desc))