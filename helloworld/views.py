from django.http import HttpResponse
from django.template import loader
from .models import AddWord


def index(request):
    data_list = AddWord.objects.all()
    template = loader.get_template('helloworld/index.html')
    context = {
        'lists': data_list
    }
    return HttpResponse(template.render(context, request))

