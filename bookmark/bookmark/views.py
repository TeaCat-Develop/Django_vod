from django.http import HttpResponse
from django.shortcuts import render

def bookmark_list(request):
    # return HttpResponse('<h1>Bookmark List</h1>')
    return render(request, 'bookmark_list.html',context={'index':index})

def bookmark_detail(request, num):
    return render(request, 'bookmark_detail.html',context={'num': num})