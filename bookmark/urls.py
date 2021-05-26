from django.urls import path
from.views import *



urlpatterns =[
    path('',BookmarkListView.as_view(),name='list'),  #리스트 보여주는 뷰 링크   # http://127.0.0.1/bookmark/???  ,뷰가 클래스형 뷰일때 as_view() 써줘야됨 이게 함수형 뷰로 변환해줌
    path('add/',BookmarkCreateView.as_view(), name="add"),  #리스트 생성하는 뷰 링크
    path('detail/<int:pk>/',BookmarkDetailView.as_view(), name="detail"),  #pk는 primary key, 모델 만들때 마이그레이션 하면 자동으로 생성되는 키, 이는 글번호를 의미
    path('update/<int:pk>/' ,BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/' ,BookmarkDeleteView.as_view(), name='delete'),

]