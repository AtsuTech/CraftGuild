from django.contrib.auth.models import AbstractUser
from django.db import models


# extend user model

class User(AbstractUser):

    #ユーザーID
    user_id = models.CharField(verbose_name='user_id', max_length=30,blank=False,)

    #ユーザータイプ　(admin.pyで管理画面でドップダウン入力にする。valueの数字を保存する)
    user_type = models.IntegerField(max_length=10,default=0,)
        
        
    
