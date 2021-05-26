from django.contrib import admin

# Register your models here.
# 내가 만든 모델을 관리자 페이지에서 관리할 수 ㅇ있도록 등록(= 내가 만든 모델 등록하기)

from. models import Bookmark

admin.site.register(Bookmark)