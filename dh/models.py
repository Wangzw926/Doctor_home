from django.db import models
import django.utils.timezone as timezone
# Create your models here.



#在数据库里生成对应的table
#用户信息
class User(models.Model):
    #userId = models.CharField("用户编号", max_length=16, unique=True)
    head = models.ImageField(upload_to='static/imgs/head', default='static/imgs/head/default_female.jpg', null=True)
    userName = models.CharField("用户名", max_length=32, unique=False)
    password = models.CharField("密码", max_length=32, null=False)
    gender = models.CharField("性别", max_length=16, null=False)
    birth = models.DateField("出生日期", default=timezone.now)
    tel = models.CharField("电话号码", max_length=16, unique=True)
    trueName = models.CharField("真实姓名", max_length=64, null=True)
    idNum = models.CharField("身份证号", max_length=32, null=True)
    famGenHis = models.CharField("家族遗传史", max_length=5000, null=True)
    drugAllergyHis = models.CharField("药物过敏史", max_length=5000, null=True)

    class Meta:
        verbose_name = "用户信息表"

#药物详细信息
class Medicine(models.Model):
    medicineName = models.CharField("药物名称", max_length=1024, null=False)
    description = models.CharField("药物描述", max_length=5000)


#病症详细信息
class Disease(models.Model):
    diseaseName = models.CharField("病症名称", max_length=1024, null=False)
    symptom = models.CharField("症状", max_length=5000, null=True)
    medicine = models.CharField("用药建议", max_length=5000, null=True)


#用户查询历史记录
class SearchHistories(models.Model):
    userName = models.CharField("用户名", max_length=32, null=False)
    record = models.CharField("查询历史", max_length=5000, null=True)


#用户个人电子病历
class ElectricRecord(models.Model):
    userName = models.CharField("用户名", max_length=32, null=False)
    main_description = models.TextField("主诉", max_length=2000, null=True)
    now_disease = models.TextField("现病史", max_length=2000, null=True)
    initial_diagnosis = models.TextField("初步诊断", max_length=2000, null=True)
    measure = models.TextField("处理", max_length=2000, null=True)


#病症药物表
class disease_medicine(models.Model):
    diseaseName = models.CharField("病症名称", max_length=1024, null=False)
    medicine = models.CharField("药品", max_length=1024, null=False)


#健康生活文章表
class Articles(models.Model):
    articleName = models.CharField("文章名", max_length=1024, null=False)
    author = models.CharField("作者", max_length=32)
    pub_time = models.DateTimeField("发表时间")
    content = models.TextField("文章内容")
    type = models.CharField("文章类型", max_length=1024, null=True)


#文章类型表
class Types(models.Model):
    typeName = models.CharField("文章类型", max_length=32)


