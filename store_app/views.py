from django.shortcuts import render, redirect
from store_app.models import Store, Menu
from django.http import HttpResponse


def store(request):
    if request.method == 'GET':
        data = Store.objects.all()
        context = {
            'data': data
        }
    elif request.method == 'POST':
        data = Store.objects.filter(address__contains=request.POST.get('search'))
        context = {
            'data':data
        }
    return render(request, 'store_app/list.html', context)


def store_detail(request, store_id):
    store_set = Store.objects.get(id=store_id)
    context = {
        'data': store_set.menu_set.all,
        'store': store_set
    }
    return render(request, 'store_app/detail.html', context)


def store_menu(request, store_id, menu):
    if request.method == 'GET':
        store_set = Store.objects.get(id=store_id)
        data = Menu.objects.filter(name=menu, store=store_set)
        context = {
            'data': data,
            'store':store_set
        }
    return render(request, 'store_app/menu.html', context)

