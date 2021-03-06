from django.http import HttpResponse
from django.views import generic
from elementaryCellularAutomata.forms import WolframForm
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
import matplotlib.pyplot as plt
import numpy as np


def Wolf(x):
    buffer = []
    rule = int(x)
    rules = list(f"{rule:08b}")
    rules = [ int(x) for x in rules ]
    A = np.zeros((40, 79), dtype = int)

    A[0, 39] = 1

    def executeRules(a, b, c):
        if a == 1 and b == 1 and c == 1:
            return rules[0]
        if a == 1 and b == 1 and c == 0:
            return rules[1]
        if a == 1 and b == 0 and c == 1:
            return rules[2]
        if a == 1 and b == 0 and c == 0:
            return rules[3]
        if a == 0 and b == 1 and c == 1:
            return rules[4]
        if a == 0 and b == 1 and c == 0:
            return rules[5]
        if a == 0 and b == 0 and c == 1:
            return rules[6]
        if a == 0 and b == 0 and c == 0:
            return rules[7]
        return 0

    for i, row in enumerate(A):
        if(i != 0):
            for j in range(len(A[i])):
                if j is 0:
                    a = 0
                else:
                    a = A[i-1, j-1]

                b = A[i-1, j]

                if j is len(row) - 1:
                    c = 0
                else:
                    c = A[i-1, j+1]
                A[i, j] = executeRules(a, b, c)
        line = ""
        for _, letter in enumerate(A[i]):
            if int(letter) is 0:
                line = line + "."
            else:
                line = line + "#"
        buffer.append(line)
    return '\n'.join(buffer)

def show(request):
    nmb = int(request.POST['nmb'])
    if not 0 <= nmb <= 256:
        raise ValidationError("parameter rule number should have a value between 0 and 256")
    
    value = Wolf(nmb)
    return render(request, 'elementaryCellularAutomata/show.html', {
        'string': value,
        'nmb': nmb,
    })


class WolfForm(FormView):
    template_name = 'elementaryCellularAutomata/form.html'
    form_class = WolframForm
    success_url = reverse_lazy('show')
