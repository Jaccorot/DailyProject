from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.core.exceptions import ValidationError
from django.http import HttpResponse

from todolist.models import Item, List

def home_page(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect('/lists/%d/' % (list_.id,))
        except ValidationError:
            error = "You can't have an empty list item"
    #items = Item.objects.filter(list=list_)
    return render_to_response('list.html', locals(), context_instance=RequestContext(request))

def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render_to_response('index.html', {"error": error},  context_instance=RequestContext(request))
    return redirect('/lists/%d/' % (list_.id,))
