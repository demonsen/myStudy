
from django.http import HttpResponse
 
from app.models import UserInfo
 
# 数据库操作
def testdb(request):
    test1 = UserInfo(username='abc', password='123')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
