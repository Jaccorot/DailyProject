from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.core.exceptions import ValidationError
from django.http import HttpResponse

from todolist.forms import ItemForm
from todolist.models import Item, List

def home_page(request):
    form = ItemForm()
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def view_list(request, list_id):
    form = ItemForm()
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save(for_list=list_)
            return redirect(list_)
    return render_to_response('list.html', locals(), context_instance=RequestContext(request))

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render_to_response('index.html', locals(), context_instance=RequestContext(request))
