from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse

from todolist.models import Item

def home_page(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def view_list(request):
    items = Item.objects.all()
    return render_to_response('list.html', locals(), context_instance=RequestContext(request))

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')
