from django.shortcuts import render
from .form import materiaform

import django.shortcuts as tk
from tkinter import messagebox
# Create your views here.


def submit_data():
    name = name_entry.get()
    contraseña = age_entry.get()
    # Puedes realizar aquí alguna acción con los datos ingresados, como guardarlos en un archivo o una base de datos
    messagebox.showinfo("Mensaje", f"Datos ingresados:\nNombre: {name}\nEdad: {contraseña}")

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario de Carga de Datos")

# Etiquetas y campos de entrada
name_label = tk.Label(root, text="Nombre:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Contraseña:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Botón de envío
submit_button = tk.Button(root, text="Enviar", command=submit_data)
submit_button.pack()

# Iniciar el bucle de la interfaz gráfica
root.mainloop()

def create_materia(request):

    if request.method == 'GET':
        return render(request, 'materia.html', {
            'form' : materiaform
        })
    else: 
        form = materiaform(request.POST)
        print(form)
        return render(request, 'materia.html', {
            'form' : materiaform
        })



    