import tkinter as tk

def sumar():
    try:
        resultado.set(float(entry_num1.get()) + float(entry_num2.get()))
    except ValueError:
        resultado.set("Error: Ingresa números válidos")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Variables para almacenar los números y el resultado
entry_num1 = tk.Entry(ventana)
entry_num1.pack()

entry_num2 = tk.Entry(ventana)
entry_num2.pack()

resultado = tk.StringVar()

# Botón para sumar
tk.Button(ventana, text="Sumar", command=sumar).pack()

# Etiqueta para mostrar el resultado
tk.Label(ventana, textvariable=resultado).pack()

# Ejecutar la ventana
ventana.mainloop()
