from django.views import View
from django.http import JsonResponse

from phonebook.models import Users

class User(View):
    
    # get으로 접근 => 사용자 목록 보기 (임시)
    def get(self, request):
        
        db_user = Users.objects.filter(email='cho881020@gmail.com').first()
        
        # users = [ user.get_data_object() for user in db_users ]
        
        return JsonResponse( {
            'code': 200,
            'message': '임시 - GET 테스트',
            # 'users': users
            'user' : db_user.get_data_object()
        } )
        
    
    def post(self, request):
        return JsonResponse( {
            'code': 200,
            'message': '임시 - POST 테스트'
        } )