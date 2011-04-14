from django.shortcuts import render

from .models import Thingie

def tag_test(request):
    return render(request, 'tag_test.html')

def thingies(request):
    context = {
        'thingies': Thingie.objects.all(),
        }
    return render(request, 'thingies.html', context)