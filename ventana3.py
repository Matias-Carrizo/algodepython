import tkinter as tk

# Función para procesar el nombre ingresado
def saludar_usuario():
    nombre_ingresado = cuadro_texto.get()
    
    if nombre_ingresado.strip() == "": 
        etiqueta_resultado.config(text="Por favor, escribe un nombre válido.", fg="red")
    else:
        etiqueta_resultado.config(text="Hola pibes"+ nombre_ingresado +" bienvenido", fg="blue")
# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Captura de Datos - Tkinter")
ventana.geometry("450x250")

# Etiqueta de instrucción
instruccion = tk.Label(ventana, text="Escribe tu nombre a continuación:", font=("Arial", 11))
instruccion.pack(pady=10)

# Cuadro de entrada de datos (Entry)
cuadro_texto = tk.Entry(ventana, font=("Arial", 12), width=30)
cuadro_texto.pack(pady=5)

# Botón de acción
boton_saludar = tk.Button(ventana, text="Enviar Saludo", font=("Arial", 10, "bold"), command=saludar_usuario)
boton_saludar.pack(pady=15)

# Etiqueta vacía reservada para mostrar la respuesta del sistema
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12, "italic"))
etiqueta_resultado.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()