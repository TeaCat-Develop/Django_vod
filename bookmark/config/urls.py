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
from django.http import Http404
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

music_lists = [
    {'title' : '피차일반', 'artist' : 'UmYull', 'album' : '행복론'},
    {'title' : 'Teeth', 'artist' : '5 Seconds of Summer', 'album' : 'CALM'},
    {'title' : '태양물고기', 'artist' : 'YOUNHA', 'album' : 'GROWTH THEORY'},
] # 더미데이터

# book_lists = [
#     {'title' : '피차일반', 'artist' : 'UmYull', 'album' : '행복론'},
#     {'title' : 'Teeth', 'artist' : '5 Seconds of Summer', 'album' : 'CALM'},
#     {'title' : '태양물고기', 'artist' : 'YOUNHA', 'album' : 'GROWTH THEORY'},
# ] # 더미데이터

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

def musics(request): # HttpResponse 예제 주석처리. render 사용으로 변경
#     music_titles = [
#         f'<a href="/music/{index}/">{music['title']}</a><br>'
#         for index, music in enumerate(music_lists)]
#     ##################################
#     # 상기 list comprehension의 for문 형태
#     # music_titles = []
#     # for music in music_list:
#     #     music_titles.append(music['title'])
#     ##################################
#
#     response_text ='<br>'
#     for index, title in enumerate(music_titles):
#         response_text += f'<a href="/music/{index}/">{title}</a><br>'
#     return HttpResponse(response_text)
    # from django.shortcuts import render 최상단 import란에 추가
    return render(request, 'musics.html', {'music_lists': music_lists})

def music_detail(request, index):
    if index > len(music_lists) -1: # 의도되지 않은 접근(없는 index) 방지
        # from django.http import Http404 ->최상단 import에 추가
        raise Http404

    music = music_lists[index]
    context = {'music_lists': music_lists, 'index': index}
    # response_text = f'<h1>{music["title"]}</h1> <p>아티스트: {music['artist']}</p> <p>앨범: {music['album']}</p>'
    # return HttpResponse(response_text)

    return render(request,'music.html',context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('book_list/',book_list),
    path('book_list/<int:num>/',book),
    path('language/<str:lang>/',language), # case A
    path('language/python/',python), # case B
    path('musics/',musics),
    path('music/<int:index>/',music_detail),
    # path ('루트', 뷰 함수명) => 루트가 입력되면 뷰 함수를 실행한다.
    # 루트에 변수 형태가 포함된 경우, 루트에 입력된 값을 가져와 뷰 함수 music_detail의 매개변수로 활용가능.

    # <str:변수명> 변수 사용주의!
    ## case A와 case B를 동시에 작성한 상태에서 language/python/ 을 접속하면?
    ### 위에서부터 읽으므로 <str:lang>에 python이 들어간 내용이 나옴.
]