import django.shortcuts as tk
from django.shortcuts import redirect, render
from .form import materiaform
from tkinter import messagebox
# Create your views here.

def submit_data(request):
    if request.method == 'POST':
        form = materiaform(request.POST)
        if form.is_valid():
            # Process the form data
            return redirect('success')
    else:
        form = materiaform()
    return render(request, 'materia.html', {'form': form})



    