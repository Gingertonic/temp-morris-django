from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import NewItemForm, UpdateQuantityForm

# Create your views here.
def index(request):
    items = Item.objects.all()
    context = { "items": items }
    return render(request, 'inventory/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        item = NewItemForm(request.POST)
        if item.is_valid():
            new_item = item.save()
            return redirect('show-item', id=new_item.id)
    else:
        form = NewItemForm()
        context = { "form": form }
        return render(request, 'inventory/new.html', context)


def about(request):
    return render(request, 'inventory/about.html')

@login_required
def show(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        form = UpdateQuantityForm(request.POST)
        if form.is_valid():
            item.quantity += 1
            item.save()
            return redirect('show-item', id=id)
    else:
        form = UpdateQuantityForm(initial={ 'quantity': item.quantity + 1 }) if request.user == item.cat.cat_manager else None
        context = { 
            "item": item,
            "form": form
        }
    return render(request, 'inventory/show.html', context)

def not_found_404(request, exception):
    return render(request, '404.html')

