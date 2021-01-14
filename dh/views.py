from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
import re

#引入dh中的models
from dh import models
# Create your views here.


#视图函数:必参:请求对象



#主页
def index(request):
    return render(request, 'index.html', locals())


#注册
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', locals())
    else:
        #get()里面写的是form表单里面对应的input标签里面的name
        #获取表单提交的内容
        userName = request.POST.get("userName")
        password = request.POST.get("userPassword")
        gender= request.POST.get("userGender")
        if gender == '男':
            head = 'static/imgs/head/default_male.jpg'
        else:
            head = 'static/imgs/head/default_famale.jpg'
        birth = request.POST.get("userBirthday")
        tel = request.POST.get("tel")

        #在此处进行逻辑的判断
        #①通过电话号查找，看是否已经被注册，如果注册则提示用户已注册，如果没有就继续往下
        #②判断用户名、密码等必须字段是否为空

        #存进数据库
        models.User.objects.create(head=head, userName=userName, password=password, birth=birth, gender=gender, tel=tel)

        return redirect('/index')
#上传头像
def head_up(request):
    if request.method == "POST":
        tel = request.session['tel']
        head = request.POST.get("head")
        # with open(head.name,'wb') as f:
        #     for line in head:
        #         f.write(line)
        # return HttpResponse("ok")
        user = models.User.objects.get(tel=tel)
        user.head = head
        user.save()
        return redirect('/infor')
    return render(request, 'infor.html')
        


#登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', locals())
    if request.method == 'POST':
        #获取表单tel和password，根据tel查找，然后比对，正确就跳到登陆成功界面，密码错误就提示用户密码错误
        try:
            user = models.User.objects.get(tel=request.POST.get('tel'), password=request.POST.get('password'))

        except ObjectDoesNotExist:
            error = "电话/密码错误"
            return render(request, 'login.html', locals())
        tel = request.POST.get('tel')
        request.session["userName"] = user.userName
        request.session["tel"] = tel
        tel_len = len(str(request.session['tel']))

        #login(request, user)
    return redirect('/index')


#test
def test(request):
    return render(request, 'user_basic_infor.html', locals())


#健康档案
def infor(request):
    user = models.User.objects.get(tel=request.session['tel'])
    return render(request, 'infor.html', locals())


#退出登录
def logout(request):
    request.session.flush()
    return redirect('/index')


#加载个人信息
def user_basic_infor(request):
    #查询数据库中的用户信息
    user = models.User.objects.get(tel=request.session['tel'])
    return render(request, 'user_basic_infor.html', locals())


#咨询历史
def consulting_history(request):
    #在这里查询咨询历史带到前端界面
    history_list = models.SearchHistories.objects.filter(userName=request.session['userName'])
    return render(request, 'consulting_history.html', locals())


#电子病历
def electric_record(request):
    electric_record_list = models.ElectricRecord.objects.filter(userName=request.session['userName'])
    user = models.User.objects.get(tel=request.session['tel'])
    return render(request, 'electric_record.html', locals())

#修改个人信息
def modifyInfor(request):
    return render(request, 'modifyInfor.html', locals())


#跳转到常见药物界面
def common_medicine(request):
    #medicine_list是一个列表，里面放的是medicine对象
    medicine_list = models.Medicine.objects.all()
    return render(request, 'common_medicine.html', locals())


#跳转到常见病症界面
def common_disease(request):
    disease_list = models.Disease.objects.all()[50:52]
    corresponding_list = models.Disease.objects.all()[1:10]
    return render(request, 'common_disease.html', locals())


#刷新常见药物界面
# def flush_medicine(request):
#     pass


#搜索药品
def search_medicine(request):
    if request.method == 'GET' or 'POST':
        key = request.POST.get('user_input_content')
        medicine_warehouse = models.Medicine.objects.all()
        suggestion = []
        pattern = '.*'.join(key)
        regex = re.compile(pattern)
        if 'tel' in request.session.keys():
            models.SearchHistories.objects.create(userName=request.session['userName'], record=key)
        for medicine in medicine_warehouse:
            match = regex.search(medicine.description)
            if match:
                suggestion.append(medicine)
            match1 = regex.search(medicine.medicineName)
            if match1:
                suggestion.append(medicine)
            suggestions = list(set(suggestion))
    return render(request, 'search_medicine.html', locals())


#搜索病症(用户输入病症，系统返回诊断结果)
def search_symptom(request):
    if request.method == 'GET':
        key = request.GET.get('key')
        disease_list = models.Disease.objects.all()
        suggestion = []
        pattern = '.*'.join(key)
        regex = re.compile(pattern)
        if 'tel' in request.session.keys():
            models.SearchHistories.objects.create(userName=request.session['userName'], record=key)
        for disease in disease_list:
            match = regex.search(disease.symptom)
            if match:
                suggestion.append(disease)
            match1 = regex.search(disease.diseaseName)
            if match1:
                suggestion.append(disease)
            suggestions = list(set(suggestion))
            dict1 = {}
            for i in suggestions:
                # dict1[i.diseaseName] = models.disease_medicine.objects.filter(diseaseName=i.diseaseName)
                medicines = models.disease_medicine.objects.filter(diseaseName=i.diseaseName)
        return render(request, 'search_symptom.html', locals())
    if request.method == 'POST':
        key = request.POST.get('key')
        disease_list = models.Disease.objects.all()
        suggestion = []
        pattern = '.*'.join(key)
        regex = re.compile(pattern)
        if 'tel' in request.session.keys():
            models.SearchHistories.objects.create(userName=request.session['userName'], record=key)
        for disease in disease_list:
            match = regex.search(disease.symptom)
            if match:
                suggestion.append(disease)
            match1 = regex.search(disease.diseaseName)
            if match1:
                suggestion.append(disease)
            suggestions = list(set(suggestion))
            dict1 = {}
            for i in suggestions:
                # dict1[i.diseaseName] = models.disease_medicine.objects.filter(diseaseName=i.diseaseName)
                medicines = models.disease_medicine.objects.filter(diseaseName=i.diseaseName)
        return render(request, 'search_symptom.html', locals())


#查看药物详情
def medicine_detail(request):
    if request.method == 'GET':
        medicine = models.Medicine.objects.get(medicineName=request.GET.get('medicineName'))
        corresponding_medicine = models.Medicine.objects.all()
        return render(request, 'medicine_detail.html', locals())


#养生小课堂
def healthy_articles(request):
    articles = models.Articles.objects.all()
    return render(request, 'healthy_articles.html', locals())

#文章详情
def article_detail(request):
    article = models.Articles.objects.get(articleName=request.GET.get('articleName'))
    return render(request, 'article_detail.html', locals())