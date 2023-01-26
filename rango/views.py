from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):

    context_dict = {'boldmessage': 'this tutorial was put put together byDavid Naray'}
    return render(request, 'rango/about.html', context=context_dict)
