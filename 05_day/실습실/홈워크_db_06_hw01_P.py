from django.db import models

class Member(models.Model):
    first_name = models.TextField(blank=True)
    last_name = models.TextField()
    age = models.IntegerField()
    country = models.TextField()
    phone = models.TextField(blank=True)
    balance = models.IntegerField()

# 1) 
user1 = Member()
user1.first_name = '철수'
user1.last_name = '김'
user1.country = '서울'
user1.balance = 500
user1.save()
# age는 NULL을 허용하지 않는데 값을 입력하지 않아서 에러 발생
# user1.age 값을 추가해준다 

# 2)
user2 = Member('영철', '이', 30, '서울', '010-1234-5678', 1000)
user2.save()
# 첫번째 매개값은 id가 입력되어야 하는데 '영철'이라는 문자열이 입력되어서 에러 발생
# user2 = Member(2, '영철', '이', 30, '서울', '010-1234-5678', 1000)로 수정

# 3)
Member.objects.create('영수', '박', 21, '서울', 2000)
# 필드 이름을 지정해주지 않아서 에러 발생
#  Member(first_name='영수', last_name='박', age=21, country='서울', balance=2000)로 수정