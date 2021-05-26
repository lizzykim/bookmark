from django.shortcuts import render

# Create your views here.
# CRUD: create, read,update,delete
# List: 리스트를 보여주는거 read랑 비슷 하지만 장고에 별도로 존재

# 클래스형 뷰(제네릭 뷰), 함수형 뷰
# 웹 페이지에 접속한다 -> 페이지를 본다
# URL 을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다 -> 응답
# 현재는 웹서버가 찾을 뷰를 만든 것

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from .models import Bookmark

# 클래스형 뷰
# 우리가 이전에 만든 model Bookmark를 자료형으로 하는 ListView ( BookmarkListView) 생성
## 리스트 보여주기(ListView)
class BookmarkListView(ListView):
    model = Bookmark

#리스트에 site_name, url 추가하기
## Create 뷰
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url'] # 대체 어느 필드를 추가할지 지정해줘야되
    success_url = reverse_lazy('list') #글쓰기를 완료하고 이동할 페이지 'list'는 urls.py 에 name에 해당. 즉, bookmarkListView.as_view(),name='list' 일로이동
    template_name_suffix = '_create' #이거 그냥 템ㅍ플릿 이름 바꿔주는 코드 ,원래 update 랑 create는 _form 형태인데 _create로 바꿔준거 이게 create뷰니깐 이름 일부로 맞춰줌


##Detail 뷰
class BookmarkDetailView(DetailView):
    model = Bookmark


##update 뷰 (수정)
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url'] #create 뷰처럼 어느 뷰를 수정해 줄것인지 field 선언 필요
    template_name_suffix = '_update'
    #success_url처럼 성공하면 이동하는 url있어야하는데 모델에서 get_absolute_url(self) 로 대체 해줌


##delete뷰
class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list') #삭제를 완료하면 Listview(BookmarkListView)보여주기
