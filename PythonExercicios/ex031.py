d = float(input('Quntos KM terá sua viagem? KM'))
if d>=200:
    print('O valor da sua passagem custará R${}'.format(d*0.50))
else:
    print('O valor da sua passagem será de R${}'.format(d*0.45))
