v = float(input('Digite quantos KM/H seu veículo está: '))
if v>=81:
    print('Seu veículo esta acima do limte de velocidade de 80KM/H e será multado em R${:.2f}!'.format((v-80)*7))
else:
    print('Parabéns você esta dentro do limite de velocidade da via!')