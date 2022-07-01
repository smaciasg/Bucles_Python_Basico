# EJERCICIO 1: Básico: imprime todos los números enteros del 0 al 150.
print(f"Resultado ejercicio 1: \n{[i for i in range(151)]}")

# EJERCICIO 2: Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
print("\n------------------------------------------------------------------")
print(f"Resultado ejercicio 2: \n{[i for i in range(5,1001) if i%5==0]}")

# EJERCICIO 3: Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar.
# Si es divisible por 10, imprime "Coding Dojo".
print("\n------------------------------------------------------------------")
e= ['Coding Dojo' if((i%5==0) and (i%10==0)) else 'Coding' if(i%5==0) else i for i in range(1,101)]
print(f"Resultado ejercicio 3: \n{e}")

# EJERCICIO 4:Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
print("\n------------------------------------------------------------------")
e= [i for i in range(1,500001,2)]
print(f"Resultado ejercicio 4: \n{sum(e)}") 

sum=0
for i in range(1,500001,2):
    sum +=i
print(sum)

# EJERCICIO 5: Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
print("\n------------------------------------------------------------------")
print(f"Resultado ejercicio 5: \n{[i for i in range(2018,-1,-4)]}")

# EJERCICIO 6: Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, 
# imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 
# (en líneas sucesivas).
print("\n------------------------------------------------------------------")
n1= int(input("LowNum: "))
n2= int(input("HighNum: "))
n3= int(input("Mult: "))
[print(i) for i in range(n1,n2+1) if i%n3==0]