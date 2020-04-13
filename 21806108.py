n = 5

#Funcion que tiene tres bucles diferentes
def ejercicio_a():
    # A1
    sum = 0
    for I in range(0, n):
        for J in range(0, n * n):
            sum += 1
    print(sum)

    # A2
    for I in range(0, n):
        for J in range(0, I * I):
            for K in range(0, K):
                sum += 1

    # A3
    i = 1
    x = 0
    while i <= n:
        x += 1
        i += 2

#Funcion que determina si el numero es primo
def ejercicio_b():
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "No es un numero primo")
            break
    else:
        print(n, "Es un numero primo")

# las matrices deben de auto generarse.
#Funcion que calcula el producto de dos matrices
def ejercicio_c():
    X = [[1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]]
    Y = [[1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]]

    Result = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                Result[i][j] += X[i][k] * Y[k][j]

    print(Result)

#Funcion recursiva que indica si el numero es capicua
def ejercicio_d(sn):

    sLen = len(sn)
    if sLen <= 1:
        return True
    else:
        if sn[0] != sn[sLen - 1]:
            return False
        else:
            return ejercicio_d(sn[1:sLen - 1])

#Funcion que suma dos matrices cuadradas
def ejercicio_e(X, Y, Result, fila, col):

    if (col >= len(X)):
        return Result
    Result[fila][col] = X[fila][col] + Y[fila][col]
    fila += 1
    if (fila == len(X)):
        fila = 0
        col +=1
    return ejercicio_e(X, Y, Result, fila, col)




#Funcion que ordena con el metodo de la burbuja
def ejercicio_f():
    A = [2, 1, 8, 0, 6, 1, 0, 8]
    print(A)

    for i in range(1, len(A)):
        for j in range(0, len(A) - i):
            if (A[j + 1] < A[j]):
                aux = A[j]
                A[j] = A[j + 1]
                A[j + 1] = aux
    print(A)

#Funcion iterativa que calcula el factorial
def ejercicio_gI(n):
    producto = 1
    for i in range (n):
        producto = producto * (i+1)
    return producto

#Funcion recursiva que calcula el factorial
def ejercicio_gR(n):
    if n <=1:
        return 1
    else:
        return n*ejercicio_gR(n-1)

#Funcion que ordena con el algoritmo de insertion sort
def ejercicio_h(values):
    print(values)
    k = 0
    g = len(values) - 1
    comparisons = 0
    while k + 1 <= g:
        i = k + 1
        curr_val = values[i]
        comparisons += 1
        while i > 0 and values[i - 1] > curr_val:
            values[i] = values[i - 1]
            i = i - 1
            comparisons += 1
        values[i] = curr_val
        k = k + 1
        print(values)

#Funcion principal
def main():
    ejercicio = '0'
    loop = True

    while loop:
        print("\n\n\nElija una de las opciones")
        print("Escriba 1 para el Ejercicio A")
        print("Escriba 2 para el Ejercicio B")
        print("Escriba 3 para el Ejercicio C")
        print("Escriba 4 para el Ejercicio D")
        print("Escriba 5 para el Ejercicio E")
        print("Escriba 6 para el Ejercicio F")
        print("Escriba 7 para el Ejercicio G")
        print("Escriba 8 para el Ejercicio H")
        print("Escriba 0 para finalizar")

        ejercicio = input("Please make a choice: ")

        if ejercicio == '1':
            ejercicio_a()
        elif ejercicio == '2':
            ejercicio_b()
        elif ejercicio == '3':
            ejercicio_c()
        elif ejercicio == '4':
            sn = str(n)
            if ejercicio_d(sn)==True:
                print("Es capicua")
            else:
                print("No es capicua")
        elif ejercicio == '5':
            X = [[1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5]]
            Y = [[1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5]]
            Result = [[0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0]]
            print(ejercicio_e(X, Y, Result, 0, 0))
        elif ejercicio == '6':
            ejercicio_f()
        elif ejercicio == '7':
            print("El factorial en iterativo es ",ejercicio_gI(n))
            print("El factorial en recursivo es ",ejercicio_gR(n))
        elif ejercicio == '8':
            ejercicio_h([2, 1, 8, 0, 6, 1, 0, 8])
        elif ejercicio == '0':
            loop = False
            print("Que pase un buen dia.")
        else:
            print("Elija una opcion valida.")


def login():
    log = True

    while log:
        email = input("Ingrese su email: ")
        contra = input("Ingrese su password: ")
        if (email == '21806108@live.uem.es'):
            if (contra == '1234'):
                print("Acceso concedido")
                log = False
        else:
            print("Email y password invalidos")



login()
main()
