import random
from django.shortcuts import render,redirect


# Create your views here.
def start_game(request):
    request.session['number']=random.randint(1,100)
    request.session['attempts']=0
    return render(request,'game/start.html')

def guess(request):
    message = ''
    if request.method== 'POST':
        guess = int(request.POST['guess'])
        request.session['attempts']+=1
        number=request.session['number']

        if guess < number:
            message = 'Too low!'
        elif guess > number:
            message = 'Too high!'
        else:
            message = f'🎉 Correct! You guessed it in {request.session["attempts"]} attempts.'
    return render(request, 'game/guess.html', {'message': message})