from django.shortcuts import render
from order_app.models import Basket
from store_app.models import Menu
#from order_app.forms import BasketForm

# Create your views here.
def basket(request):
    if request.method == 'POST':
        menu = Menu.objects.get(store=request.POST.get('store'), name=request.POST.get('menu'))
        data = Basket()
        data.menu = menu
        data.name = request.POST.get('name')
        data.price = request.POST.get('price')
        data.count = request.POST.get('count')
        data.total = int(data.count) * int(data.price)
        data.save()

        context = {
            'data':data,
            'store':menu.store
        }
    else:
        data = Basket.objects.last()
        context = {
            'data':data,
        }
    return render(request, 'order_app/basket.html', context)

def order(request):
    pass




