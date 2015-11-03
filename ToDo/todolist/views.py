from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST.get('item_text', '')
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))
