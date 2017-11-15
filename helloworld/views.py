from django.shortcuts import render
from .models import AddWord


def helloworld_index(request):
    data_list = AddWord.objects.all()
    context = {
        'lists': data_list
    }
    return render(request, 'helloworld/index.html', context)

