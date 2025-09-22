from django.db import models


class Blog(models.Model):
    CATEGORY_CHOICES = (
        #(db에 들어갈 이름, 실제 표시될 이름)
        ('free','자유'),
        ('travel','여행'),
        ('cat','고양이'),
        ('dog','강아지'),
    )
    category = models.CharField('카테고리', max_length=10, choices=CATEGORY_CHOICES)
    title = models.CharField('제목', max_length=100)
    content = models.TextField('본문') # textfield는 글자 제한 x

    created_at = models.DateTimeField('작성일자', auto_now_add=True)
    updated_at = models.DateTimeField('수정일자',auto_now=True)

# 제목
# 본문
# 작성자 => 패스 (추후 업데이트)
# 작성일자
# 수정일자
# 카테고리


