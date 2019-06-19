from django.shortcuts import render, redirect
from .forms import DiamondsForm


alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_lower = alphabet_upper.lower()


# Create your views here.
def diamonds_home(request):
    if request.method == 'POST':
        form = DiamondsForm(request.POST)
        if form.is_valid():
            result = diamantize(form.cleaned_data['letter'])
            return render(request, 'diamonds/diamonds_result.html', {'result': result})
        else:
            return redirect('/diamonds')
    else:
        form = DiamondsForm()
        return render(request, 'diamonds/diamonds_form.html', {'form': form})


# &nbsp
def diamantize(letter):
    alphabet = ''
    if letter in alphabet_upper:
        alphabet = alphabet_upper
    elif alphabet in alphabet_lower:
        alphabet = alphabet_lower

    position = alphabet.index(letter)

    result = []

    len_alphabet_slice = len(alphabet[:position+1])
    for i in range(len_alphabet_slice):
        line = ' '*len_alphabet_slice
        line += alphabet[i]
        line += ' ' * len_alphabet_slice
        result.append(line)

    return result