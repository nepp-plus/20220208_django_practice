from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def test_home(request):
    content = '<h1>여기는 홈 화면 입니다.</h1>' # HTML태그를 리턴.
    return HttpResponse(content)

def json_test(request):
    my_dict = {
        'code': 200,
        'message': 'JSON이 내려오는지 테스트'
    }
    
    return JsonResponse(my_dict)