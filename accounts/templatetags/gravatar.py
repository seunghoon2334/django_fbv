import hashlib
# 장고의 템플릿 줘
from django import template

# 템플릿 라이브러리 가져와줘
register = template.Library()

# 필터로 makehash 함수를 추가해줘
@register.filter
def makehash(email):
    return hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()