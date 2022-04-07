from collections import UserDict
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
class todoinf(models.Model):
    userid       = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="ユーザーID")

    title        = models.CharField(
                    verbose_name="タスク名",
                    max_length=30,
                    blank   =False,
                    null    =False)

    description  = models.TextField(
                    verbose_name="タスク詳細",
                    blank     =True,
                    null      =True) 

    updated      = models.DateTimeField(
                    verbose_name="更新日",
                    auto_now=True,
                    editable=False,
                    blank   =False,
                    null    =False) 

    deadline       = models.DateTimeField(
                    verbose_name="期限",
                    blank     =True,
                    null      =True)

    def __str__(self):
        return self.title