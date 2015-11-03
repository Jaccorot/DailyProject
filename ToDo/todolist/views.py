from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse

from todolist.models import Item

def home_page(request):
    if request.method == 'POST':
        # new_item_text = request.POST.get('item_text', '')
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))
