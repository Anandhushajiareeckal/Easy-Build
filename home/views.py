from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout
from .models import * 


# Create your views here.
def login(request):
    if request.method=="POST":
        uname=request.POST['uname']
        password=request.POST['password']
        try:
            try:
                admin=admin_data.objects.get(uname=uname)
                if admin.uname== uname and admin.password== password:
                    
                    request.session['unames']=uname
                    
                    
                    return redirect('admin_home')
                    
                    
            except admin_data.DoesNotExist:
                log = registration_create.objects.get(uname=uname, password=password)
                
                request.session['unames']=uname

            try:
                
                global reg 
                reg = registration_data.objects.get(uname=uname)
                if reg.role=="User":
                    if 'unames' in request.session:
                        return redirect('user_home')
                    return redirect('login')
                try:
                    wrk=workers_data.objects.get(uname=uname)
                    if 'unames' in request.session:
                        return render(request,'wrkr_home.html',{'log':wrk })
                    return redirect('login')
                except workers_data.DoesNotExist:
                  return redirect('login')  
                

            except registration_data.DoesNotExist:
                 if 'unames' in request.session:
                    return redirect('registrationdata')
                 return redirect('login')
        except registration_create.DoesNotExist:
           if 'unames' in request.session:
            return redirect('registration_create') 
           return redirect('login')
        
        
    return render(request, 'login.html')
    



def registrationdata(request):
    
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        sex=request.POST['sex']
        state=request.POST['state']
        district=request.POST['district']
        location = request.POST['location']
        Languages = request.POST['Languages']
        uname=request.session['unames']  
        role=request.POST['role'] 
        usersave = registration_data(name=name,phone=phone, email = email, sex = sex, state = state, district = district, location = location,Languages = Languages,uname=uname,role=role)
        usersave.save()
        if role=="Worker":
            if 'unames' in request.session:
                return redirect('workers_data')
            return redirect('login')
        return redirect('login')
    return render(request, 'registration_data.html')
        

def registrationcreate(request):
    if request.method=="POST":
        uname=request.POST['uname']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        
        chlog = registration_create.objects.filter(uname__contains=uname)
        if chlog.exists():
            alert="The user name is existing"
            return render(request, 'registration_create.html', {'alert': alert})
        elif cpassword == password:
            usersave = registration_create(uname = uname, password = password)
            usersave.save()
            request.session['unames']=uname
            return redirect('login')
        else:
            alert_pass="Enter correct password"
            return render(request, 'registration_create.html', {'alert_pass': alert_pass})
    return render(request, 'registration_create.html')







def Workers_data(request):

    if request.method=="POST":
        name=request.POST['name']
        image_face=request.FILES['image_face']
        field=request.POST['field']
        experience=request.POST['experience']
        exp_cnf=request.POST['exp_cnf']
        discription=request.POST['discription']
        image_work1=request.FILES['image_work1']
        image_work2=request.FILES['image_work2']
        image_work3=request.FILES['image_work3']
        uname=request.session['unames']
        usersave=workers_data(name=name,image_face = image_face, field = field, experience = experience, exp_cnf = exp_cnf, discription = discription, image_work1 = image_work1, image_work2  = image_work2, image_work3 = image_work3,uname=uname)
        usersave.save()
        return redirect('login')
    if 'unames' in request.session:
        return render(request,'Workers_data.html')
    return redirect('login')
def user_interface(request):
    return render(request,'user_interface.html')

def user_home(request):
    val=request.GET.get('val')
    if val:
        wr_dts = workers_data.objects.get(uname=val)
        if 'unames' in request.session:
            return render(request,'wr_prf_usr.html',{'log':wr_dts })
        return redirect('login')
    if request.method=="POST":
        serch=request.POST['serch']
        serch=workers_data.objects.filter(field=serch)
        if 'unames' in request.session:
            return render(request,'serch_rslt.html',{'log':serch})
        return redirect('login')
    dta=workers_data.objects.all()
    dtas=registration_data.objects.all()
    if 'unames' in request.session:
        return render(request,'user_home.html',{'log':dta , 'nme':reg , 'loc':dtas})
    return redirect('login')

    
    



def wr_prf_usr(request):
    val=request.GET.get('val')
    if val :
        wr_dts = registration_data.objects.get(uname=val)
        if 'unames' in request.session:
            return render(request,'usr_ctct_wrkr.html',{'log':wr_dts})
        return redirect('login')
    return render(request,'wr_prf_usr.html')


def usr_ctct_wrkr(request):
    return render(request,'usr_ctct_wrkr.html')




def wrkr_prof(request):
    
    
    return render(request,'wrkr_prof.html')

def user_edit_prof(request):
    return render(request,'user_edit_prof.html')

def wrkr_interface(request):
    return render(request,'wrkr_interface.html')

def wrkr_home(request):
    val1=request.GET.get('val1')
    
    if val1 :
        wr_dts = workers_data.objects.get(uname=val1)
        if request.method=="POST":
            name=request.POST['name']
            field=request.POST['field']
            experience=request.POST['experience']
            exp_cnf=request.POST['exp_cnf']
            discription=request.POST['discription']
            usrnme=request.session['unames']
            workers_data.objects.filter(uname=usrnme).update(name=name,field=field, experience=experience,exp_cnf=exp_cnf,discription=discription)
            return redirect('login')
        if 'unames' in request.session:
            return render(request,'wrkr_prof.html',{'log':wr_dts})
        return redirect('login')

    val2=request.GET.get('val2')
    if val2:
       usrnme=request.session['unames']
       reg = registration_create.objects.get(uname=usrnme)
       if request.method=="POST":
        usname=request.POST['uname']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password== cpassword:
            registration_create.objects.filter(uname=usrnme).update(uname=usname,password=cpassword)
            registration_data.objects.filter(uname=usrnme).update(uname=usname)
            workers_data.objects.filter(uname=usrnme).update(uname=usname)

            return redirect('login')
        if 'unames' in request.session:
            return render(request,'wrkr_chngeid.html',{'unm':reg})
        return redirect('login')
     
    return render(request,'wrkr_home.html')








def admin_interface(request):
    return render(request,'admin_interface.html')


def admin_home(request):
    if 'unames' in request.session:

        return render(request,'admin_home.html',)
    return redirect('login')



def admin_worker_view(request):
    val2=request.GET.get('val2')
    if val2 :
        reg= registration_create.objects.get(uname=val2)
        wr_det = workers_data.objects.get(uname=val2)
        wrk = registration_data.objects.get(uname=val2)
        reg.delete()
        wr_det.delete()
        wrk.delete()
        if 'unames' in request.session:
            return redirect('admin_worker_view')
        return redirect('login')
    dat= workers_data.objects.all()
    return render(request,'admin_worker_view.html', {'log':dat})


def admin_worker_prof(request):
    val=request.GET.get('val')
    wr_det = workers_data.objects.get(uname=val)
    wrk = registration_data.objects.get(uname=val)
    
    if 'unames' in request.session:    
        return render(request,'admin_worker_prof.html',{'log':wr_det, 'reg':wrk})
    return redirect('login')
    


def admin_user_view(request):
    val2=request.GET.get('val2')
    if val2 :
        reg= registration_create.objects.get(uname=val2)
        wrk = registration_data.objects.get(uname=val2)
        reg.delete()
        wrk.delete()
        if 'unames' in request.session:
            return redirect('admin_user_view')
        return redirect('login')
    dat= registration_data.objects.all()
    return render(request,'admin_user_view.html',{'log':dat})


def admin_change_pass(request):
        usrnme=request.session['unames']
        reg = admin_data.objects.get(uname=usrnme)
        if request.method=="POST":
            usname=request.POST['uname']
            password=request.POST['password']
            cpassword=request.POST['cpassword']

            if password== cpassword:
                admin_data.objects.filter(uname=usrnme).update(uname=usname,password=cpassword)
                return render(request,'login.html')
            alert="Enter correct password !"

        return render(request,'admin_change_pass.html', {'unm':reg})

def wrkr_chngeid(request):

    return render(request,'Wrkr_chngeid.html')

def user_about(request):

    return render(request,'user_about.html')

def user_contact(request):

    return render(request,'user_contact.html')


def logout_view(request):
    logout(request) 
    return redirect('login')
