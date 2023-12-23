soma = cont = 0
while True:
    num = int(input('Digtite um núemro qualquer (Para Sair do programa digite 999): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos valores foi {soma}!')



