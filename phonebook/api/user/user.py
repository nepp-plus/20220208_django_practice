from django.views import View
from django.http import JsonResponse

from phonebook.models import Users

class User(View):
    
    # get으로 접근 => 사용자 목록 보기 (임시)
    def get(self, request):
        
        # 파라미터의 email 항목을 뽑아서 검색에 활용.
        #  검색 결과가 없다면? 구글링, 400 처리.
        
        
        
        db_user = Users.objects.filter(email=request.GET['email']).first()
        
        # users = [ user.get_data_object() for user in db_users ]
        
        if db_user:
            return JsonResponse( {
                'code': 200,
                'message': '임시 - GET 테스트',
                # 'users': users
                'user' : db_user.get_data_object()
            } )
        else:
            return JsonResponse({
                'code': 400,
                'message': '해당 이메일을 사용하는 사람은 없습니다.'
            }, status=400 )
        
    
    def post(self, request):
        return JsonResponse( {
            'code': 200,
            'message': '임시 - POST 테스트'
        } )