from rest_framework.views import APIView
from rest_framework.response import Response

from django.views import View
from django.http import JsonResponse

from phonebook.models import Contacts
from phonebook.serializer import ContactsSerializer

class Contact(APIView):
    
    def get(self, request):
        
        # request의 기능중, 메쏘드 이름 ['파라미터'] 방식으로 파라미터값 추출.
        
        search_name = request.GET['name']
        
        db_contact = Contacts.objects.filter(name=search_name).first()
        
        serialized = ContactsSerializer(db_contact)
        
        return Response({
            'code': 200,
            'message': '연락처 - GET 테스트',
            'data': {
                'contact': serialized.data
            }
        })
        
    def post(self, request):
        
        
        
        return JsonResponse({
            'code': 200,
            'mesasge': '연락처-POST 테스팅',
            'data': {
                '임시항목': request.POST['email'],
            }
        })