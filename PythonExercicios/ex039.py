from datetime import date
nascimento = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nascimento
if idade == 18:
    print('Está na hora de se alistar, procure a junta militar mais próxima!')
elif 18 > idade:
    print('Ainda não esta na hora de se alistar! Faltam {} anos para o alistamento.'.format(18-idade))
elif 18 < idade:
    print('Já passou do prazo para o alistamento, você está a {} anos atrasado para o alistamento!'.format(idade-18))
