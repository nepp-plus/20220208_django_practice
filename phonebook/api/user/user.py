from django.views import View
from django.http import JsonResponse

class User(View):
    
    # get으로 접근
    def get(self, request):
        return JsonResponse( {
            'code': 200,
            'message': '임시 - GET 테스트'
        } )
        
    
    def post(self, request):
        return JsonResponse( {
            'code': 200,
            'message': '임시 - POST 테스트'
        } )