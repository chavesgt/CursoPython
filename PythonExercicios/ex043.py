peso = float(input('Digite quantos KG você pesa: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso normal')
elif 18.5 <= imc <25:
    print(' PARABÉNS, você está na faixa do PESO NORMAL')
elif 25<= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')