from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import DiamondsForm


alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_lower = alphabet_upper.lower()


# Create your views here.
def diamonds_home(request):
    if request.method != 'POST':
        form = DiamondsForm()
        return render(request, 'diamonds/diamonds_form.html', {'form': form})

    form = DiamondsForm(request.POST)
    if form.is_valid():
        result = _diamantize(form.cleaned_data['letter'])
        return render(request, 'diamonds/diamonds_result.html', {'result': result})
    else:
        #messages.error(request, 'Informe um valor válido(a-zA-Z).')
        messages.error(request, form.errors['letter'])
        return redirect('/diamonds')



#################################


# &nbsp
def _diamantize(letter):
    space = '_'
    alphabet = ''
    if letter not in alphabet_upper and letter not in alphabet_lower:
        return None
    elif letter in alphabet_upper:
        alphabet = alphabet_upper
    elif alphabet in alphabet_lower:
        alphabet = alphabet_lower

    print(alphabet)
    position = alphabet.index(letter)

    result = []

    len_alphabet_slice = len(alphabet[:position+1])

    indexes = list(range(len_alphabet_slice))
    indexes += reversed(indexes[:-1])
    for i in indexes:
        if i == 0:
            side_spaces = (len_alphabet_slice-i) * space

            line = ''.join([side_spaces, alphabet[i], side_spaces])

            result.append(line)
        else:
            side_spaces = (len_alphabet_slice-(i+1)) * space
            central_spaces = (i*2 + 1) * space

            line = ''.join([side_spaces, alphabet[i], central_spaces, alphabet[i], side_spaces])

            result.append(line)

    return result
