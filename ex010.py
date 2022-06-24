
validacao = False
while validacao !=True:
    introducao = input('para converter suas moedas iremos fazer algumas perguntas, ok? (Digite (Y) para sim e (N) para não)\n')
    if introducao == 'Y':
        validacao = True
        dinheiro = float(input('Quanto você tem de dinheiro, R$? (ex: 50.30 ou 50.00)\n'))
        tipo_1 = input('Qual o tipo da sua moeda? (ex: R$,US,...)\n')
        tipo_2 = input('Qual o tipo da moeda para qual você quer converter? (ex: R$,US,...)\n')
        moeda = float(input(f'Quanto está valendo o {tipo_2}? (Separe por ponto, ex: 3.24)\n'))
        conversao = (dinheiro/moeda)
        print(f' Com {dinheiro} {tipo_1}, Você poderá comprar{moeda} {tipo_2}')
    elif introducao == 'N':
        validacao = True
        print('Finalizado, Obrigado!')
    else:
        print('Não digitou uma respota válida')