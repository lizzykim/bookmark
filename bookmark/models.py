from django.db import models
from django.urls import reverse
# Create your models here.
# 모델: 데이터베이스를 SQL 없이 다루려고
# 우리가 데이터를 객체화해서 다루겠다.
# 모델 = 테이블
# 모델의 필드 = 테이블 컬럼
# 인스턴스 = 테이블의 레코드
# 모델의 값 = 레코드의 걸럼 데이터 값


#1. 클래스는 models.Model를 상속받는다
#2. 필드의 종류를 정의해줘야됨


# ex)사이트 이름, 주소

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    #필드의 종류가 결정하는 것
    #1. 데이터 베이스의 컬럼 종류
    #2. 제약 사항(몇글자 까지)
    #3. Form의 종류
    #4. Form에서 제약 사항

    #클래스의 인스턴스의 내용이 나오고 싶게 할떄,
    def __str__(self):
        return "이름: "+self.site_name+",주소: "+self.url

    def get_absolute_url(self): #장고에서 제공하는 메소드로 자동완성 안됨
        return reverse('detail',args=[str(self.id)]) #detail페이지로 넘기고  각 페이지는 다르니깐 args에 pk 값인 id도 놔줘야됨!


#모델을 만들었다 -> 데이터베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정했다
# makemigrations=> 모델의 변경사항을 추적해서 기록