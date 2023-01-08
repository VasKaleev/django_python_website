from django.shortcuts import render


def index(request):
    data = {
        'title':'Главная страница',
        'values':['Some','Hello','123'],
        'obj': {
            'car': 'BMV',
            'age': '14',
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def magazin(request):
    return HttpResponse("<h4>Страница магазин</h4>")
