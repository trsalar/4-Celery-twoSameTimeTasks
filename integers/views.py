from django.shortcuts import render


def index(request):
    return render(request, 'integers/index.html', context={'text': 'Hello World'})
