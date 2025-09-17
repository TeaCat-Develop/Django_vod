from django.db import models

# Model = DB의 테이블
# Field = DB의 컬럼

# 북마크
# 이름 => varchar
# URL => varchar

class Bookmark(models.Model):
    name = models.CharField('이름', max_length=100)
    # url = models.CharField('URL', max_length=200)
    url = models.URLField('URL', max_length=200) # URLField는 url validation 추가되어 있음.
    created_at = models.DateTimeField('생성일시', auto_now_add=True)
    updated_at = models.DateTimeField('수정일시', auto_now=True)

class Meta: # 필수는x 추가적으로 admin 사용할 때 등등 필요하여 작성
    verbose_name = '북마크'
    verbose_name_plural = '북마크 목록'

# class BookmarkCategory(models.Model):

# makemigrations => migration.py 파일을 만든다.
# 실제 DB에는 영향 x => 실제 DB에 넣기 위한 정의를 하는 파일을 생성

# migrate => migrations/ 폴더 내에 있는 migration 파일들을 실제 DB에 적용

# makemigrations => 깃의 commit => github에 적용 X => db에 적용 X, 적용할 파일 생성
# migrate => 깃의 push => github에 적용 o => db에 적용 o, migrations 파일 기록을 가지고 적용