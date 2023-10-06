from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    resultado = None

    if request.method == 'POST':
        operacion = request.POST.get('operacion')
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))

        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
        elif operacion == 'division':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = 'División por cero no permitida'

    return render(request, 'index.html', {'resultado': resultado})