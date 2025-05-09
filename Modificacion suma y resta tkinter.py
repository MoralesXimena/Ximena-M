import tkinter as tk

def sumar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 + num2
    label_resultado.config(text=f"Resultado: {resultado}")

def restar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 - num2
    label_resultado.config(text=f"Resultado: {resultado}")
ventana = tk.Tk()
ventana.title("Bienevenido a la programacion en python")
ventana.geometry("1000x600")
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack()
entry_num1 = tk.Entry(ventana,bg="Black", fg="White")
entry_num1.pack()
label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack()
entry_num2 = tk.Entry(ventana,bg="Black", fg="White")
entry_num2.pack()
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar, width=10, height=3,font=("Arial", 20))
boton_sumar.pack()
boton_restar = tk.Button(ventana, text="Restar", command=restar, width=10, height=3,font=("Arial", 20))
boton_restar.pack()
label_resultado = tk.Label(ventana, text="")
label_resultado.pack()
ventana.mainloop()