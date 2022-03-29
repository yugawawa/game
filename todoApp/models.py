from django.db import models
from django.utils import timezone
class todoinf(models.Model):
    title        = models.CharField(
                    verbose_name="タスク名",
                    max_length=30,
                    blank   =False,
                    null    =False)

    description  = models.TextField(
                    verbose_name="タスク詳細",
                    blank     =True,
                    null      =False) 

    updated      = models.DateTimeField(
                    verbose_name="更新日",
                    auto_now=True,
                    editable=False,
                    blank   =False,
                    null    =False) 

    deadline       = models.DateTimeField(
                    verbose_name="期限",
                    blank     =True,
                    null      =False)

    def __str__(self):
        return self.title