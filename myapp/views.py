from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .models import Member
from .forms import Memberform
# Create your views here.

def members(request):
    member_list=Member.objects.all().values()
    context = {
        'member_list':member_list
    }
    template = loader.get_template('members.html')
    return HttpResponse(template.render(context,request))

def detail(request, id):
    mymember=Member.objects.get(id=id)
    template = loader.get_template('detail.html')
    context={
        'mymember':mymember
    }
    return HttpResponse(template.render(context,request))

    

def bike(request):
    template = loader.get_template('bike.html')
    return HttpResponse(template.render())

def contact(request):
    member_list=Member.objects.all().values()
    context= {
        'member_list':member_list
    }
    template=loader.get_template('contact.html')
    return HttpResponse(template.render(context,request))

def new(request):
    t1=loader.get_template('new.html')
    return HttpResponse(t1.render())

@csrf_exempt
def new(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname',)
        lastname=request.POST.get('lastname',)
        rollno=request.POST.get('rollno',)
        member=Member(firstname=firstname,lastname=lastname,rollno=rollno)
        member.save()
        t1=loader.get_template('new.html')
        return HttpResponse(t1.render())

def update(request,id):
    member = Member.objects.get(id=id)
    form = Memberform(request.POST,instance=member)
    if form.is_valid():
        form.save()
        t1 = loader.get_template('new.html')
        return HttpResponse(t1.render())
    return render(request, 'update.html',{'form':form,'Member':member})

@csrf_exempt
def delete(request,id):
    if request.method == 'POST':
        member=Member.objects.get(id=id)
        member.delete()
        t1=loader.get_template("members.html")
        return HttpResponse(t1.render())
    return render(request,'delete.html')