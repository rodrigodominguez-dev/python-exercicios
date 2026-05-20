medida = float(input('Qual é a medida em metros? '))

cm = medida * 100
mm = medida * 1000

print('A medida de {} metros corresponde a {:.0f} cm ou {:.0f} mm'.format(medida, cm, mm))
