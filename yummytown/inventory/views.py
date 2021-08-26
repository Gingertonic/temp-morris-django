from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Item

# items = [
#     { "id": 1, "name": "Cheesecake", "quantity": 4 },
#     { "id": 2, "name": "Coriander", "quantity": 25 },
#     { "id": 3, "name": "Pancakes", "quantity": 15 }
# ]

# Create your views here.
def home(request):
    items = Item.objects.all()
    context = { "items": items }
    return render(request, 'inventory/index.html', context)


def about(request):
    return render(request, 'inventory/about.html')

@login_required
def show(request, id):
    item = get_object_or_404(Item, pk=id)
    context = { "item": item }
    return render(request, 'inventory/show.html', context)

def not_found_404(request, exception):
    return render(request, '404.html')

