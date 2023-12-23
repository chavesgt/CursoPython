def aumentar(preço = 0, taxa= 0, formato=False ):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def dimuinuir(preço= 0 , taxa= 0, formato=False ):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço = 0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço = 0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')
