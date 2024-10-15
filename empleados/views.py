from django.shortcuts import render


def lista_empleados(request):
    # Lista de nombres de empleados
    empleados = ['Juan Pérez', 'María García', 'Ana López', 'Carlos Méndez']
    
    # Pasar la lista al template mediante contexto
    return render(request, 'empleados.html', {'empleados': empleados})