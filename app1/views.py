from django.shortcuts import render


def index(request):
    context = {'dams':1}
    return render(request, 'index.html', context)
