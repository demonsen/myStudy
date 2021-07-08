
from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    return HttpResponse("Hello world ! ")

def runoob(request):
    context = {}
    context['hello'] = 'Hello, xx World!'
    context['num'] = 111233322
    context['name'] = request.GET.get('name')
    return render(request, 'runoob.html', context)


