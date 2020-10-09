from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect


#引入dh中的models
from dh import models
# Create your views here.

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
        sex = request.POST.get("userGender")
        birth = request.POST.get("userBirthday")
        tel = request.POST.get("phone")

        #在此处进行逻辑的判断
        #①通过电话号查找，看是否已经被注册，如果注册则提示用户已注册，如果没有就继续往下
        #②判断用户名、密码等必须字段是否为空
        #存进数据库
        models.User.objects.create(userName=userName, password=password, birth=birth, gender=sex, tel=tel)

        return redirect('/index')
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
        request.session['userName'] = user.userName
        request.session["tel"] = tel
        tel_len = len(str(request.session['tel']))

        #login(request, user)
    return redirect('/index')
#退出登录
def logout(request):
    request.session.flush()
    return redirect('/index')
