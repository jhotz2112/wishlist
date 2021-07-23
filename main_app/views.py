from django.shortcuts import render
from .models import Wish
from django.views.generic.edit import CreateView, DeleteView


# Create your views here.


def wishes_index(request):
    wishes = Wish.objects.all()
    return render(request, 'wishes/index.html', { 'wishes': wishes })

class WishesCreate(CreateView):
    model = Wish
    fields = '__all__'
    success_url = ''

class WishesDelete(DeleteView):
    model = Wish
    success_url = ''