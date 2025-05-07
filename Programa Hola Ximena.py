import tkinter as tk 

def saludar():
    nombre = entrada.get()
    etiqueta_resultado.confi(text=f"Hola{nombre}")
    
    edad = entrada.get()
    etiqueta_resultado.confi(text=f"Tienes{edad}años")
    
    ventana = tk.Tk()
    ventana.title("Saludo") 
    ventana.title("Edad") 
    ventana.geometry("300x150")
    
    etiqueta = tk.Label(ventana, text="Ingresa tu nombre:")
    etiqueta.pack()
    
    etiqueta = tk.Label(ventana, text="Ingresa tu edad:")
    etiqueta.pack()
    
    entrada = tk.Entry(ventana)
    entrada.pack()
    
    boton = tk.Button(ventana, text="Saludar", command=saludar)
    boton.pack() 

    boton = tk.Button(ventana, text=" Mostrar edad", command=mostrar_edad)
    boton.pack() 
    
    etiqueta_resultado = tk.Label(ventana, text="")
    etiqueta_resultado.pack()
    
    ventana.mainloop()
