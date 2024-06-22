def suma():
    return 3+4

def resta(a,b):
    return a -b

print("1.-Suma\n2.-Resta\n")
op=int(input("Opcion: "))

if op==1:
    print("La suma es {}".format(suma()))
if op==2:
    num1 = int(input("Dame n1: "))
    num2 = int(input("Dame n2: "))
    print("La resta es {}".format(resta(num1,num2)))

