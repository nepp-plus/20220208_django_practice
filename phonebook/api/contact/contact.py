from django.views import View
from django.http import JsonResponse

from phonebook.models import Contacts

class Contact(View):
    
    def get(self, request):
        
        db_contact = Contacts.objects.filter(name='조경진').first()
        
        return JsonResponse({
            'code': 200,
            'message': '연락처 - GET 테스트',
            'data': {
                'contact': db_contact.get_data_object()
            }
        })
        
    def post(self, request):
        return JsonResponse({
            'code': 200,
            'mesasge': '연락처-POST 테스팅'
        })