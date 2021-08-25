from django.shortcuts import render
from django.http import HttpResponse

items = [
    { "id": 1, "name": "Cheesecake", "quantity": 4 },
    { "id": 2, "name": "Coriander", "quantity": 25 },
    { "id": 3, "name": "Pancakes", "quantity": 15 }
]

# Create your views here.
def home(request):
    context = { "items": items }
    return render(request, 'inventory/index.html', context)


def about(request):
    return render(request, 'inventory/about.html')

def show(request, id):
    item = [item for item in items if id == item['id']][0]
    return HttpResponse(
        f"<p>We have {item['quantity']} portions of {item['name']} available</p>"
    )

