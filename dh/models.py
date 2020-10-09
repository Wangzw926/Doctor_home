from django.db import models
import django.utils.timezone as timezone
# Create your models here.


#用户
#在数据库里生成对应的table
class User(models.Model):
    #userId = models.CharField("用户编号", max_length=16, unique=True)
    userName = models.CharField("用户名", max_length=32, unique=False)
    password = models.CharField("密码", max_length=32, null=False)
    gender = models.CharField("性别", max_length=16, null=False)
    birth = models.DateField("出生日期",default=timezone.now())
    tel = models.CharField("电话号码", max_length=16, unique=True)
    class Meta:
        verbose_name = "用户信息表"


class Medicine(models.Model):
    medicineId = models.CharField("药物编号",max_length=32, unique=True)
    medicineName = models.CharField("药物名称", max_length=128, null=False)
    description = models.CharField("药物描述",max_length=512)


