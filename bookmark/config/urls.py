"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello, world!</h1>')

def book_list(request):
    book_text = ''

    for i in range(1,11):
        book_text += f'book {i}<br>'

    return HttpResponse(book_text)

def book(request, num):
    book_text = f'book {num}번 페이지입니다.'
    return HttpResponse(book_text)

def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지입니다.</h1>')

def python(request):
    return HttpResponse('This is python page.')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('book_list/',book_list),
    path('book_list/<int:num>/',book),
    path('language/<str:lang>/',language), # case A
    path('language/python/',python), # case B

    # <str:변수명> 변수 사용주의!
    ## case A와 case B를 동시에 작성한 상태에서 language/python/ 을 접속하면?
    ### 위에서부터 읽으므로 <str:lang>에 python이 들어간 내용이 나옴.
]