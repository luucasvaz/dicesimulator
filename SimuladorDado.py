# definindo a função dado_6 (um dado de seis lados)
def dado_6():
    res_user = input('Você deseja jogar o dado? (S/N)').upper()
    if res_user == 'S':
        import numpy as np
        res_dado_6 = str(np.random.randint(1, 7))
        print('O resultado do dado foi ' + res_dado_6 + '.')
    elif res_user == 'N':
        print('Foi um prazer.')
    else:
        print('Resposta não reconhecida. Por favor, responda com "S" ou "N".')


dado_6()
