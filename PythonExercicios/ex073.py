tabela = ('Botafogo', 'Flamengo', 'Grêmio', 'São Paulo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Athletico - PR',
           'Fortaleza', 'Cruzeiro', 'Internacional', 'Atlético - MG', 'Cuiabá', 'Chapecoense', 'Corinthians',
           'Bahia', 'Goiás', 'Coritiba', 'Vasco', 'América - MG')
print('-='*15)
print(f'Os cinco primeiros colocados são: {tabela[:5]}')
print('-='*15)
print(f'Os quatros últimos da tabela são: {tabela[-4:]}')
print('-='*15)
print(f'Lista do time em ordem alfabética: {sorted(tabela)}')
print('-='*15)
print(f'A Chapecoense está na posição {tabela.index("Chapecoense")+1}ª posição')
print('-='*15)

