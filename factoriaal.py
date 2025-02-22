import time

def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)

def medir_tiempo(func, n):
    inicio = time.time()
    resultado = func(n)
    fin = time.time()
    return resultado, fin - inicio

def main():
    numero = int(input("Ingrese un número para calcular su factorial: "))
    
    res_iter, tiempo_iter = medir_tiempo(factorial_iterativo, numero)
    res_rec, tiempo_rec = medir_tiempo(factorial_recursivo, numero)
    
    print(f"Factorial calculado iterativamente: {res_iter}, Tiempo: {tiempo_iter:.6f} segundos")
    print(f"Factorial calculado recursivamente: {res_rec}, Tiempo: {tiempo_rec:.6f} segundos")
    
    print("\nVentajas de cada método:")
    print("- Iterativo: Más eficiente en términos de memoria, evita desbordamiento de pila.")
    print("- Recursivo: Código más conciso y fácil de entender para problemas con estructura recursiva.")
    
    print("\nComplejidad Big-O:")
    print("- Método iterativo: O(n) en tiempo y O(1) en espacio.")
    print("- Método recursivo: O(n) en tiempo y O(n) en espacio por las llamadas recursivas.")

if __name__ == "__main__":
    main()
