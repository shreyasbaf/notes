from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect 
from .models import Orders
from django.contrib import messages

def home(request):
    return render(request,'loggedin.html')

def index(request):
        return render(request,'index.html')

def order(request):
        return render(request,'order.html')

def adminlogin(request):
        return render(request,'login.html')

def login(request):
    uid = request.POST['username']
    pas = request.POST['password']
    if(uid == 'admin' and pas == 'password'):
        flag = 1
    return home(request)

def logout(request):
    flag = 0
    return HttpResponseRedirect('/')

def orderadded(request):
    return render(request,'added.html')

def addorder(request):
    fn = request.POST['fnm']
    ln = request.POST['lnm']
    adr = request.POST['addr']
    n = request.POST['ns']
    st = "Order Placed"
    new_item = Orders(fname = fn,lname = ln,addr = adr,notes = n,status = st )
    new_item.save()
    messages.info(request,'Your Order is Successfully Placed')
    #return HttpResponseRedirect('/')
    return orderadded(request)

def OrdersView(request):
    #x = TodoItem.objects.all()
    x = Orders.objects.all()
    return render(request,'vieworder.html',
    {'all_items': x})

def ChangeOrder(request,id):
    #return request
    ids = id
    s = request.POST['st']
    d = Orders.objects.get(id=ids)
    d.status = s
    d.save()
    return render(request,'loggedin.html')
    #return HttpResponseRedirect('/')

def change(request):
        x = Orders.objects.all()
        return render(request,'changeorder.html',
        {'all_items': x})

def ToTrack(request):
    return render(request,'track.html')

def Track(request):
    keys = request.POST['key']
    #xx = Orders.objects.get(fname = keys) 
    #xx = Orders.objects.all()
    k = Orders.objects.get(fname = keys)
    Tname = k.fname
    Tlname = k.lname
    Tadr = k.addr
    Tnotes = k.notes
    TStatus = k.status
    return render(request,'viewtrack.html',
    {'all_items': keys,
    'fname' : Tname,
    'lname' : Tlname,
    'status' : TStatus,
    'adr':Tadr,
    'ns':Tnotes})
    #return render(request,'vieworder.html',
    #{'all_items': xx})

def deleteOrder(request,id):
    idy = id
    d = Orders.objects.get(id=idy)
    d.delete()
    return HttpResponseRedirect('/vieworder')