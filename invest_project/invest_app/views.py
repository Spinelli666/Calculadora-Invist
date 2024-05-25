from django.shortcuts import render
from .utils import investimento_dinamico
import numpy as np

def investimento_view(request):
    if request.method == "POST":
        ativos = int(request.POST.get('ativos'))
        T = int(request.POST.get('T'))
        B_inicial = float(request.POST.get('B_inicial'))
        lambda_valor = float(request.POST.get('lambda_valor'))
        
        # Transformar as entradas de string para array
        retorno = np.array(eval(request.POST.get('retorno')))
        risco = np.array(eval(request.POST.get('risco')))

        # Chamada da função investimento_dinamico
        x, B = investimento_dinamico(ativos, retorno, risco, B_inicial, T, lambda_valor)

        # Preparação do contexto para renderizar o template com os resultados
        context = {
            'x': x,
            'B': B
        }
        return render(request, 'result.html', context)

    return render(request, 'investment_form.html')
