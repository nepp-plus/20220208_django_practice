from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from phonebook.models import Users

# Create your views here.

def test_home(request):
    content = '<h1>여기는 홈 화면 입니다.</h1>' # HTML태그를 리턴.
    return HttpResponse(content)

def json_test(request):
    
    # 모든 사용자 목록 불러오기 테스트
    db_users = Users.objects.all()
    
    users = [ user.get_data_object()  for user in db_users  ]
    
    my_dict = {
        'code': 200,
        'message': 'JSON이 내려오는지 테스트',
        'users': users
    }
    
    return JsonResponse(my_dict)