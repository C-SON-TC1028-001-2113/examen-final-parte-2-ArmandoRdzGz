
def main():
    matriz = crearmatriz()
    l_col = []
    if len(matriz) > 0:
        for i in range(len(matriz[0])):
            a = 0
            for j in range(len(matriz)):
                a += matriz[j][i] 
            l_col.append(a)
        print(l_col)

def crearmatriz():
    lista = []
    filas = int(input())
    columnas = int(input())
    if filas > 0 and columnas > 0: 
        for i in range(filas):
            lista.append([])
            for j in range(columnas):
                n = int(input())
                lista[i].append(n)
    else: 
        print('Error')
    return lista

if __name__=='__main__':
    main()
