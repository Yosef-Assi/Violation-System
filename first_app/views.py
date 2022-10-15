
from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from ViolationSystem.settings import EMAIL_HOST_USER
import bcrypt
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import BadHeaderError, send_mail
from django.core.mail import EmailMessage


def root(request):
    return redirect('/home')


def licenses(request):
    if 'driver_id' in request.session:
        driver=Driver.objects.get(id=request.session['driver_id'])
        context = {
            'licimage':driver.image
        }
        
    return render(request,'license.html',context)
def policeinfo(request):
    if 'police_id' in request.session:
        context={
            "police" :Police.objects.get(id= request.session['police_id'] )
        }
        return render(request, 'policeinfo.html',context)
    else:
        return redirect ('/login')

def driver(request):
    if 'driver_id' in request.session:
        context={
            'driver':Driver.objects.get(id=request.session['driver_id'])
        }
        return render(request, 'driver.html',context)
    else:
        return redirect('/login')

def driveredit(request):
    if 'driver_id' in request.session:
        context = {
            'driver':Driver.objects.get(id=request.session['driver_id'])
        }
        return render(request,'driver_edit.html',context)
    else:
        return redirect('/login')
def email(request):
     if 'police_id' in request.session:
        context={
            "police" :Police.objects.get(id= request.session['police_id'] )
        }
        return render(request,'send_email.html')
     else:
        return redirect('/login')


def policeviolation(request):
    if 'police_id' in request.session:
        context= {
            'allviolations': Violation.objects.all(),
            'this_driver':Police.objects.get(id=request.session['police_id'])
        }
        return render(request,'policeviolation.html',context)
    else:
        return redirect('/login')


def police(request):
    return render(request, 'police.html')

def login(request):
    return render(request, 'login.html')    

def addviolation(request):
    if 'police_id' in request.session:
    
        return render(request,'addviolation.html')
    else:
        return redirect('/login')
def update(request,id):
    if 'police_id' in request.session:
        Vio = Violation.objects.get(id=id)
        context = {
            'Vio':Vio,
        }
        return render(request,'violation_update.html',context)
    else:
        return redirect('/login')

def showviolation(request):
    if 'driver_id' in request.session:
        showvio=Violation.objects.filter(driver=request.session['driver_id'])
        context={
            'allviolations': Violation.objects.all(),
            'this_driver':Driver.objects.get(id=request.session['driver_id']),
            'showvio':showvio
        }
        return render(request,'showviolation.html',context)
    else:
        return redirect('/login')

def rule(request):
    if 'driver_id' in request.session:
        return render(request,'rule.html')
    else:
        return redirect('/login')

def home(request):
    return render(request,'home.html')
def reg(request):
        errors = Driver.objects.basic_validator(request.POST)
        users=Driver.objects.all()
        for user in users:
            if user.email==request.POST['email']:
                errors['email']="this email aleady exsist"
        for user in users:
            if user.notional_id==request.POST['nid']:
                errors['notional_id']="this notional_id is not valid"

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        password= request.POST['password']
        pw_hash= bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        Driver.objects.create (
            full_name=request.POST['fullname'],
            birthday=request.POST['birthday'],
            notional_id=request.POST['nid'],
            city=request.POST['city'],
            blood_type=request.POST['blood_type'],
            email=request.POST['email'],
            password=pw_hash,
            phone_number=request.POST['phonenumber'],
        
        )
        name1=Driver.objects.last()
        request.session['full_name']=name1.full_name
        request.session['driver_id'] = name1.id

        return redirect('/driver')

def regpolice(request):
    
        errors = Police.objects.basic_validator2(request.POST)
        polices=Police.objects.all()
        for police in polices:
            if police.email==request.POST['email']:
                errors['email']="this email aleady exsist"

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        password= request.POST['password']
        pw_hash= bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        Police.objects.create (
            full_name=request.POST['fullname'],
            birthday=request.POST['birthday'],
            city=request.POST['city'],
            email=request.POST['email'],
            password=pw_hash,
            phone_number=request.POST['phonenumber'],
        
        )
        name1=Police.objects.last()
        request.session['full_name_p']=name1.full_name
        request.session['police_id'] = name1.id

        return redirect('/policeinfo')

def signin(request):
    if request.POST['type']=='driver':
        driver = Driver.objects.filter(email=request.POST['email']) 
        if driver:
            logged_driver=driver[0]


            if bcrypt.checkpw(request.POST['password'].encode(),logged_driver.password.encode()):
                request.session['driver_id']= logged_driver.id
                request.session['full_name']= logged_driver.full_name
                return redirect('/driver')
            else:
                messages.error(request,"Your email or password is wrong try ag!")
                return redirect('/login')
        else:
            messages.error(request,"Your email or password is wrong try ag!")

        return redirect('/login')

    elif request.POST['type']=='police':
        police =Police.objects.filter(email=request.POST['email']) 
        if police:
            logged_police=police[0]


            if bcrypt.checkpw(request.POST['password'].encode(),logged_police.password.encode()):
                request.session['police_id'] = logged_police.id
                request.session['full_name_p']= logged_police.full_name
                return redirect('/policeinfo')
            else:
                messages.error(request,"Your email or password is wrong try ag!")
                return redirect('/login')
        else:
            messages.error(request,"Your email or password is wrong try ag!")

        return redirect('/login')

def add_vio(request):
    if 'police_id' in request.session:
    # -------------------------
    # Validator for valdition Table
    # -------------------------
        errors = Violation.objects.basic_validator3(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/addviolation')

        police1 = Police.objects.get(id = request.session['police_id'])
        Violation.objects.create(
            location = request.POST['location'],
            violation_date = request.POST['violation_date'],
            expierd_date_violation = request.POST['ex_date'],
            resson = request.POST['reason'],
            driver = Driver.objects.get(notional_id=request.POST['driver_id']),
            police = police1,
            fees=request.POST['fees']

        )
        email2=Violation.objects.last()
        youremail=email2.driver.email
        name=email2.driver.full_name
        locations=email2.location
        fee=email2.fees
        exp=email2.expierd_date_violation
        res=email2.resson
        email = EmailMessage(
        'New Violaton is Add',
        'Hello Mr/s' +' '+ name +' '+'you have anew violation : \n' + 'location :'+" "+locations+'\n' +'fees :'+" "+ str(fee) +"₪"
        +'\n' +'expierd_date :' +" "+ str(exp) +'\n' +'resson :' +" "+ res ,
        '',
        [youremail],
            reply_to=['violationsystem5@gmail.com'],
        headers={'Message-ID': 'foo'},
)
        email.send()
        return HttpResponse('Add Violation is Accept')
    else:
        return redirect('/login')


def update_violation(request,id):
    if 'police_id' in request.session:
        Vio = Violation.objects.get(id=id)


        Vio.location = request.POST.get('location')
        Vio.fees = request.POST.get('fees')
        Vio.violation_date = request.POST.get('violation_date')
        Vio.expierd_date_violation = request.POST.get('ex_date')
        Vio.resson = request.POST.get('reason')
        Vio.save()
        return redirect(f'/update/{id}')
    else:
        return redirect('/login')


def delete(request,id):
    if 'police_id' in request.session:

        item = Violation.objects.get(id = id)
        item.delete()
        return JsonResponse({'success': True, 'message': 'Delete','id':id})
    else:
        return redirect('/login')

def logout2(request):
    del request.session['police_id']
    del request.session['full_name_p']

    return redirect('/home')

def logout(request):
    del request.session['driver_id']
    del request.session['full_name']

    return redirect('/home')


def getviolation(request):
    vios=Violation.objects.filter(driver=request.session['driver_id'])

    return JsonResponse({"violations":list(vios.values())})


def send_email(request):
    myemail=Driver.objects.all().values()
    emails=[]
    for value in myemail:
        emails.append(value['email'])
    subject = request.POST['Name']
    message = request.POST.get('Message')
    send_mail( subject,message,'', emails,fail_silently=False) 
    # send_mail('ssss','sssss','yosef9978@gmail.com',['barqlaith99@gmail.com'])
    return redirect('/email')



def upload(request):
    driver=Driver.objects.get(id=request.session['driver_id'])
    driver.image=request.FILES['image']
    driver.save()
    return redirect('/license')
