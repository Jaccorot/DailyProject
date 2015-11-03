from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse

from todolist.models import Item, List

def home_page(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render_to_response('list.html', locals(), context_instance=RequestContext(request))

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))
