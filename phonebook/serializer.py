# 여러개의 클래스 배치.
# 각각의 모델 클래스들을 > dict / list로 변경해주는 기능을 구현.

# rest_framework 모듈의 도움을 받자.
from rest_framework import serializers
# 어떤 모델을 직렬화 (ORM -> Dict) 할건지, 모델을 끌어오자.
from .models import Users, Contacts

# 실제 사용자 모델을 변환해주는 클래스
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users  # 어떤 클래스를 변환?
        fields = '__all__' # 모든 컬럼을 dict에 담자.
        
        
class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'