nota1 = float(input('Digite a primira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Tiando {:.1f} e {:.1f} , a média do aluno é {:.1f}'.format(nota1,nota2,media))
if 7 > media >=5:
    print('O aluno está em RECUPERAÇÃO.')
elif media <5:
    print('O aluno está REPROVADO.')
elif media >= 7:
    print('O aluno está AROVADO.')

