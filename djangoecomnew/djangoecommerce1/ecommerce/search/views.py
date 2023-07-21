from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def searchresult(request):
    query=""
    r=None
    if(request.method=="POST"):
        query=request.POST.get('q')
        if(query):
            r=Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'search.html',{'query':query,'r':r})
