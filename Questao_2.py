import numpy as np
from Questao_1 import ObterDadosIris

def PowerMethod_SymetricMatrix(A):
    '''
    Calcula os autovalores e autovetores de "A", se "A" for simétrica.
    
    Retorno: (matriz_autovalores, matriz_autovetores)
    '''

    # Verificando se A é simétrica
    if not np.array_equal(A, A.T):
        print ("Erro na função PowerMethod. Matriz \"A\" não é simétrica.")
        return -1

    # Pegando a dimensão de "A"
    n = len(A)

    # Inicializando a matriz de autovetores
    matrizAutovetores_A = np.zeros((n, n))
    
    # Inicializando a matriz de autovetores
    matrizAutovalores_A = np.zeros((n, n))
    ##### ----------------------------------- ###############


    for i in range (n):
        x = np.ones((n, 1))
        x = np.dot(A, x)
        x = x/np.linalg.norm(x, 2)
        autovetor = np.zeros((n, 1))
        while np.linalg.norm(x-autovetor, 2) > 0.0000000001:
            autovetor = x
            x = np.dot(A, x)
            x = x/np.linalg.norm(x, 2)

        x = np.dot(A, autovetor)
        autovalor = x[0]/autovetor[0]
        matrizAutovalores_A[i, i] = autovalor
        autovetor = x/np.linalg.norm(x, 2)
        for j in range(n):
            matrizAutovetores_A[j, i] = autovetor[j]
        
        A = A - autovalor*(np.dot(autovetor, autovetor.T))

    return (matrizAutovetores_A, matrizAutovalores_A)



def main():
    
    Dados = ObterDadosIris()
    matrizes_R = Dados[1]

    classe  =  ["SETOSA SEM TERMO INDEPENDENTE", "VERSICOLOR SEM TERMO INDEPENDENTE", "VIRGINICA SEM TERMO INDEPENDENTE",\
                "SETOSA COM TERMO INDEPENDENTE", "VERSICOLOR COM TERMO INDEPENDENTE", "VIRGINICA COM TERMO INDEPENDENTE"]
    
    for aux in range(6):
        autovetores, autovalores = PowerMethod_SymetricMatrix(matrizes_R[aux])
        print ("\n--------------------------------")
        print (classe[aux], ":", sep="")
        print ("\nAutovetores:")
        print (autovetores)
        print ("Autovalores:")
        print (autovalores)
    
    return 0    

if __name__ == '__main__':
    main()

