import numpy as np
from Questao_1 import ObterDadosIris
from Questao_2 import PowerMethod_SymetricMatrix

def SVD_SymetricMatrix(R):
    '''
    Decompõe qualquer matriz simétrica em "V*M*V^T", Então:
            R = V*M*VT 
    onde:
        M = Matriz diagonal
        V = eigenvector matrix of R*R

    Retorno: (V, M, VT) 
    '''

    ########## CALCULANDO A MATRIZ "V" ###############
    RR = np.dot(R, R)

    V, Lambda = PowerMethod_SymetricMatrix(RR)

    ########## CALCULANDO A MATRIZ "M" ###############
    M = np.sqrt(Lambda)

    return (V, M, V.T)

def main():
    
    Dados = ObterDadosIris()
    matrizes_R = Dados[1]
    
    classe  =  ["SETOSA SEM TERMO INDEPENDENTE", "VERSICOLOR SEM TERMO INDEPENDENTE", "VIRGINICA SEM TERMO INDEPENDENTE",\
                "SETOSA COM TERMO INDEPENDENTE", "VERSICOLOR COM TERMO INDEPENDENTE", "VIRGINICA COM TERMO INDEPENDENTE"]
    
    # Como R é simétrica, SVD de R é igual a V*M*V^T

    for aux in range(6):
        V_R, M_R, VT_R = SVD_SymetricMatrix(matrizes_R[aux])
        print ("\n--------------------------------")
        print (classe[aux], ":", sep="")
        print ("\nMatriz \"V\":")
        print (V_R)
        print ("Matriz \"M\":")
        print (M_R)

    return 0

main()