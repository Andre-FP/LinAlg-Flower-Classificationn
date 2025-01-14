import numpy as np
from Questao_1 import Questao_1


def Questao_4():
    matrizes_W = Questao_1()

    #Letra a):
    X_A = np.array([[5.0], [2.3], [3.3]], dtype=np.double)
    Y_A = 1.0

    #Letra b):
    X_B = np.array([[4.6], [3.2], [1.4]], dtype=np.double)
    Y_B = 0.2

    #Letra c):
    X_C = np.array([[5.0], [3.3], [1.4]], dtype=np.double)
    Y_C = 0.2

    #Letra d):
    X_D = np.array([[6.1], [3.0], [4.6]], dtype=np.double)
    Y_D = 1.4

    #Letra e):
    X_E = np.array([[5.9], [3.0], [5.1]], dtype=np.double)
    Y_E = 1.8

    X = [X_A, X_B, X_C, X_D, X_E]
    Y = [Y_A, Y_B, Y_C, Y_D, Y_E]
    
    classe  =  ["SETOSA SEM TERMO INDEPENDENTE", "VERSICOLOR SEM TERMO INDEPENDENTE", "VIRGINICA SEM TERMO INDEPENDENTE",\
                "SETOSA COM TERMO INDEPENDENTE", "VERSICOLOR COM TERMO INDEPENDENTE", "VIRGINICA COM TERMO INDEPENDENTE"]
    
    for amostra in range(5):
        erros = []
        # Calculando os erros da amostra, sem termo independente
        for W in range(3):
            erros.append(abs(Y[amostra] - np.dot(matrizes_W[W].T, X[amostra])))

        # Calculando os erros, com o termo independente
        X[amostra] = np.append(X[amostra], [[1.0]], axis=0)
        for W in range(3, 6):
            erros.append(abs(Y[amostra] - np.dot(matrizes_W[W].T, X[amostra])))

        # Transformando a matriz "erros", que contém objetos, em uma matriz numérica.
        for element in range(6):
            erros[element] = erros[element][0][0]

        menorErro = min(erros)
        print ("---------------------------------------------------------------------------------------")
        print("\nAmostra ", amostra + 1,": ","IRIS ", classe[erros.index(menorErro)], sep="")
        print("\nErros:", erros)

    return 0

Questao_4()