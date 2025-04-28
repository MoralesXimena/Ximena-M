num1=float(input("Ingrese el primer numero: "))
print(f"Ingresa el primer número: ")
num2=float(input("Ingrese el segundo numero: "))
print(f"Ingresa el segundo número: ")
operacion=input("Seleccione la operacion (+, -, *, /):" )
print(f"Ingresa la Operación: ")

if operacion=='+':
    resultado=num1+num2
    print(f"Resultado: "{resultado:%f})
    elif operacion=='-':
        resultado=num1-num2
        print(f"Resultado: "{resultado:%f})
        elif operacion=='*':
        resultado=num1*num2
        print(f"Resultado: "{resultado:%f})
        elif operacion=='/':
            if num2 !=0:
                resultado=num1/num2
                print(f"Resultado: "{resultado:%f})
    else:            
                print("Error: No se uede dividir entre cero.")
     else:           
        print("Operación no válida.") 
    