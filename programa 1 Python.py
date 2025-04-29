num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
operacion = input("Seleccione la operacion (+, -, *, /):" )

if operacion == '+':
    resultado = num1 + num2
      print(f"Resultado: {resultado:.2f}")
elif operacion == '-':
    resultado = num1 - num2
        print(f"Resultado: {resultado:.2f}")
elif operacion == '*':
    resultado = num1 * num2
        print(f"Resultado: {resultado:.2f}")
elif operacion == '/':
    if num2 != 0:
        resultado = num1 / num2
      print(f"Resultado: {resultado:.2f}")
    else:            
      print("Error: No se uede dividir entre cero.")
else:           
      print("Operación no válida.") 

    
