from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.views import View
from django.http import JsonResponse

from phonebook.models import Users
from phonebook.serializer import UserSerializer

class User(APIView):
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'email',
                openapi.IN_QUERY,
                description='필터에 적용해볼 이메일값',
                required=True,
                type=openapi.TYPE_STRING
            ),
        ]
    )
    # get으로 접근 => 사용자 목록 보기 (임시)
    def get(self, request):
        
        # 파라미터의 email 항목을 뽑아서 검색에 활용.
        #  검색 결과가 없다면? 구글링, 400 처리.
        
        
        
        db_user = Users.objects.filter(email=request.GET['email']).first()
        
        # users = [ user.get_data_object() for user in db_users ]
        
        if db_user:
            
            # 찾아낸 Users 객체를 > dict로 변환 : 만든 클래스 활용
            
            serializer =  UserSerializer(db_user)
            
            return Response( {
                'code': 200,
                'message': '임시 - GET 테스트',
                # 'users': users
                'user' : serializer.data
            } )
        else:
            return Response({
                'code': 400,
                'message': '해당 이메일을 사용하는 사람은 없습니다.'
            }, status=400 )
        
    
    def post(self, request):
        return JsonResponse( {
            'code': 200,
            'message': '임시 - POST 테스트'
        } )