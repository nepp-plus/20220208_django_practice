from django.db import models

class Contacts(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    memo = models.TextField()
    created_at = models.DateTimeField()

    def get_data_object(self):
        data = {
            'id': self.id,
            'name': self.name,
            'phone_num': self.phone_num,
            'email': self.email,
            'memo': self.memo,
            'created_at': str(self.created_at),
            'user': self.user.get_data_object(),
        }
        return data

    class Meta:
        managed = False
        db_table = 'contacts'


class Users(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    created_at = models.DateTimeField()

    # DB 수행 결과 > dict로 변경 메쏘드
    
    def get_data_object(self):
        data = {
            'email': self.email,
            'nickname': self.nickname,
            'created_at': str(self.created_at)
        }
        return data

    class Meta:
        managed = False
        db_table = 'users'
