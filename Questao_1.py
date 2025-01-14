# BIBLIOTECAS IMPORTADAS #

import numpy as np
import pandas as pd

################################# FUNCOES #################################

def LU(A):
    n_linhas = A.shape[0]
    U = np.zeros((n_linhas, n_linhas), dtype = np.double)
    L = np.eye(n_linhas, dtype = np.double)
    for indice_1 in range(n_linhas):
        U[indice_1, indice_1:] = A[indice_1, indice_1:] - L[indice_1, :indice_1] @ U[:indice_1, indice_1:]
        L[(indice_1 + 1):, indice_1] = (A[(indice_1 + 1): , indice_1] - L[(indice_1 + 1):, :] @ U[:, indice_1]) / U[indice_1, indice_1]    
    return L, U


def forward_subs(L, P):
    y = []
    for indice_2 in range(len(P)):
        y.append(P[indice_2])
        for indice_3 in range(indice_2):
            y[indice_2] = y[indice_2] - (L[indice_2, indice_3] * y[indice_3])
        y[indice_2] = y[indice_2] / L[indice_2, indice_2]
    return y


def back_subs(U, y):
    x = np.zeros_like(y)
    for indice_4 in range(len(x), 0, -1):
      x[indice_4 - 1] = (y[indice_4 - 1] - np.dot(U[indice_4 - 1, indice_4:], x[indice_4:])) / U[indice_4 - 1, indice_4 - 1]
    return x


def resultado(L, U, P):
    y = forward_subs(L, P)
    x = back_subs(U, y)
    return x

def ObterDadosIris():
    
    #################### LEITURA DA PLANILHA (SEM O TERMO IDEPENDENTE) ########################
    lista_colunas = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm"]
    Data = pd.read_excel("dados.xlsx", usecols = lista_colunas)
    ###########################################################################################
    
    matrizes_X = []
    matrizes_R = []
    
    # COLETANDO AS MATRIZES "X" E CALCULANDO "R", SEM TERMO INDEPENDENTE
    aux = 0
    for count in range (3):
        matrizes_X.append(Data.iloc[aux:aux + 15])
        matrizes_R.append(np.dot(matrizes_X[count].T, matrizes_X[count]))
        aux += 15

    ####################    LEITURA DA PLANILHA (COM O TERMO IDEPENDENTE) #####################
    lista_colunas = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm","PetalWidthCm"]
    Data_ti = pd.read_excel("dados.xlsx", usecols = lista_colunas)
    Data_ti.PetalWidthCm = 1
    ###########################################################################################
    
    # COLETANDO AS MATRIZES "X" E CALCULANDO "R", COM TERMO INDEPENDENTE
    aux = 0
    for count in range (3):
        matrizes_X.append(Data_ti.iloc[aux:aux + 15])
        matrizes_R.append(np.dot(matrizes_X[count + 3].T, matrizes_X[count + 3]))
        aux += 15
    
    '''
    matrizes_R = [R_SetosaSemTermo, R_VersicolorSemTermo, R_VirginicaSemTermo, 
                   R_SetosaComTermo, R_VersicolorComTermo, R_VirginicaComTermo]
    
    matrizes_X = [X_SetosaSemTermo, X_VersicolorSemTermo, X_VirginicaSemTermo, 
                   X_SetosaComTermo, X_VersicolorComTermo, X_VirginicaComTermo]
    '''
    
    return (matrizes_X, matrizes_R)

########################################### MAIN ##########################################

def Questao_1():

    # Rw = P

    # Obtendo as matrizes "X" e "R"
    matrizes_X, matrizes_R = ObterDadosIris()
    
    # COLETANDO AS MATRIZES "Y"
    lista_colunas_2 = ["PetalWidthCm"]
    Data_Y = pd.read_excel("dados.xlsx", usecols = lista_colunas_2)
    
    # GERANDO AS MATRIZES "P"
    # P = Xt*Y
    P = []
    aux = 0
    for X in matrizes_X:
        Y = (Data_Y.iloc[aux:aux + 15]) 
        P.append(np.dot(X.T, Y))
        aux += 15
        if aux == 45:
            aux = 0

    #### APLICANDO O MÉTODO "LU" EM "R" E RESOLVENDO O SISTEMA ####
    
    classe  =  ["SETOSA SEM TERMO INDEPENDENTE", "VERSICOLOR SEM TERMO INDEPENDENTE", "VIRGINICA SEM TERMO INDEPENDENTE",\
                "SETOSA COM TERMO INDEPENDENTE", "VERSICOLOR COM TERMO INDEPENDENTE", "VIRGINICA COM TERMO INDEPENDENTE"]

    aux = 0
    matrizes_W = []
    for R in matrizes_R:
        L, U = LU(R)
        
        # APLICANDO FOWARDSUBSTITUTION E BACKSUBSTITUTION        
        matrizes_W.append(resultado(L, U, P[aux]))
        
        if __name__ == '__main__':
            print ("\n--------------------------------")
            print (classe[aux], ":", sep="")    
            print("\n w = \n", matrizes_W[aux], sep ="")   
        
        aux += 1

    return matrizes_W  

if __name__ == '__main__':
    Questao_1()

