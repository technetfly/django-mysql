from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from mysqldemo.models import Vps


# Create your views here.
# from mysqldemo.models import User


def show_info(request):
    if request.method == 'GET':
        # 获取所有数据
        vpss = Vps.objects.all()
        return render(request, 'info.html', {'vpss': vpss})


def add_stu(request):
    if request.method == 'GET':
        vpss = Vps.objects.all()
        return render(request, 'add.html', {'vpss': vpss})
    if request.method == 'POST':
        # 括号里的都是从html里获取到的 name="hostname">
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        memory = request.POST.get('memory')
        cpu = request.POST.get('cpu')
        # 插入数据库
        Vps.objects.create(hostname=hostname, ip=ip, memory=memory, cpu=cpu)
        return HttpResponseRedirect(reverse('mysqldemo:show_info'))


def del_stu(request, id):
    if request.method == 'GET':
        # .delete()删除操作
        Vps.objects.get(pk=id).delete()
        return HttpResponseRedirect(reverse('mysqldemo:show_info'))


def mod_stu(request, id):
    if request.method == 'GET':
        vps = Vps.objects.get(pk=id)
        return render(request, 'mod.html', {'vps': vps})
    if request.method == 'POST':
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        memory = request.POST.get('memory')
        cpu = request.POST.get('cpu')
        Vps.objects.filter(pk=id).update(hostname=hostname, ip=ip, memory=memory, cpu=cpu)
        return HttpResponseRedirect(reverse('mysqldemo:show_info'))


def sel_stu(request):
    if request.method == 'GET':
        return render(request, 'sel.html')
    if request.method == 'POST':
        hostname = request.POST.get('hostname')
        try:
            vps = Vps.objects.get(hostname=hostname)
            return render(request, 'sel.html', {'vps': vps})
        except:
            return render(request, 'sel.html', {'error': '该虚拟机不存在'})
