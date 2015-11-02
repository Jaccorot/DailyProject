from django.shortcuts import render
from django.shortcuts import render_to_response

def home_page(request):
    return render_to_response('index.html', locals())
