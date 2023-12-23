km=float(input('Quantos KM foram rodados com o carro?:KM '))
dias= int(input('Quantos dias você ficou com o carro?: Dias '))
preco= (dias*60) + (km*0.15)
print('O valor a ser pago pela locação do carro é de {:.2f}'.format(preco))
