from django.shortcuts import render, HttpResponse, redirect
# from message_app.models import Msg
from .models import Msg

# Create your views here.
def testing(request):
    return HttpResponse("Linked successfully")

def create(request):
    print("Request is:", request.method)
    if request.method == 'POST':
        # access form data
        n = request.POST['uname']
        mail = request.POST['uemail']
        mob = request.POST['mob']
        msg = request.POST['msg']
        # print(n, "-", mail, "-", mob, "-", msg)

        # transfer data into mysql
        m = Msg.objects.create(name = n, email = mail, mobile = mob, msg = msg)
        m.save()

        # return HttpResponse("Data Fetched")
        return redirect('/dashboard')
    else:
        return render(request, 'create.html')
    
def dashboard(request):
    m = Msg.objects.all()
    # print(m)
    # return HttpResponse("Data fetched from database")

    context = {}
    context['data'] = m
    return render(request, 'dashboard.html',context)


def delete(request, rid):
    # print("id to be deleted:", rid)
    # return HttpResponse("id to be deleted:" + rid)
    m = Msg.objects.filter(id = rid)
    # m = Msg.objects.filter(id = rid, name = 'Girish')
    m.delete()
    return redirect('/dashboard')


def edit(request, rid):
    # print("id to be edited:", rid)
    # return HttpResponse("id to be edited:" + rid)
    
    print(request.method)
    if request.method == 'POST':
        #Update new data
        new_name = request.POST['uname']
        new_email = request.POST['uemail']
        new_mob = request.POST['mob']
        new_msg = request.POST['msg']

        m = Msg.objects.filter(id=rid)
        m.update(name=new_name, email=new_email, mobile=new_mob, msg=new_msg)
        return redirect('/dashboard')
    else:
        #Display new data
        context = {}
        m = Msg.objects.get(id = rid)
        print(m)
        context['data']=m
        return render(request, 'edit.html', context)

    # return HttpResponse("id to be edited:" + rid)