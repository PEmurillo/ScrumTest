print("Compara numeros")

num1 = int(input("Dame n1: "))
num2 = int(input("Dame n2: "))

if num1>num2:
    print("el {} es mayor que el {}".format(num1,num2))
else:
    print("el {1} es mayor que el {0}".format(num1,num2))

print("--------------------------pedri edad---------------------------")
edad = int(input("Ingresa tu edad"))
if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")