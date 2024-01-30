from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Doctor,Patient,Appiontment
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as auth_logout
from django.db import IntegrityError
from django.core.exceptions import ValidationError
# import datetime

# Create your views here.x
def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    
    
    doctors= Doctor.objects.all()
    patient= Patient.objects.all()
    appointment= Appiontment.objects.all()
    
    d=0;
    p=0;
    a=0;
    for i in doctors:
        d+=1
    for i in patient:
        p+=1
    for i in appointment:
        a+=1;
    
    d1={'d':d, 'p':p , 'a':a}
    
    
    return render(request,'index.html', d1)



# def login(request):
#     error=""
#     if request.method=="POST":
#         u = request.POST['uname']
#         p = request.POST['pass']
#         user = authenticate(username=u, password=p)
#         try:
#             if user.is_staff:
#                 login(request,user)
#                 error="no"
#             else:
#                 error="yes"
#         except:
#             error="yes"
#     err = {'error':error}
#     return render(request,'login.html',err)

#use next ---
def custom_login(request):
    error = ""
    
    if request.method == "POST":
        u = request.POST.get('uname')
        p = request.POST.get('pass')
        
        user = authenticate(username=u, password=p)
        # if user:
        #      request.session['user'] = u # this is a url security
        #      request.session.set_expiry(60) # this is time period


        if user is not None and user.is_staff:
            login(request, user)
            return redirect('index')
        else:
            error = "Invalid login credentials. Please try again."

    return render(request, 'login.html', {'error': error})
                
# def logout(request):
#     if not request.user.is_staff:
#         return redirect('login')
#     logout(request)
#     return redirect('login')  

# def logout(request):
#     if not request.user.is_staff:
#         return redirect('login')
#     return redirect('login')

def custom_logout(request):
    if not request.user.is_staff:
        return redirect('login')
    auth_logout(request)
    return redirect('login')    


# Create Doctor Data-----

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html',d)


def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=="POST":
        n=request.POST['name']
        c=request.POST['contact']
        sp=request.POST['special']
        try:
            Doctor.objects.create(name=n,modile=c,special=sp)
            error="no"
        except:
            error="yes"
    d= {'error':error}
    return render(request,'add_doctor.html',d)


def Delete_Doctor(request, id):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('view_doctor')


'''def edit(request,id):
    doctor = Doctor.objects.get(id=id)
    return render(request,'docedit.html', {'doctor':doctor})

def update(request, id):
    doctor = Doctor.objects.get(id=id)
    form = EmployeeForm(request.POST,instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/about")
    return render(request, 'edit.html', {'employee':employee})'''




#Create Pateint Data----


def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request,'view_patient.html',d)


def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=="POST":
        n=request.POST['name']
        m=request.POST['mobile']
        gd=request.POST['gender']
        add=request.POST['address']
        try:
            Patient.objects.create(name=n,mobile=m,gender=gd,address=add)
            error="no"
        except:
            error="yes"
    d= {'error':error}
    return render(request,'add_patient.html',d)


def Delete_Patient(request,id):
    if not request.user.is_staff:
        return redirect('login')
    
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('view_patient')


#Create Appointment Data----

def View_Appiontment(request):
    if not request.user.is_staff:
        return redirect('login')
    app = Appiontment.objects.all()
    a = {'app':app}
    return render(request, 'view_appiontment.html', a)
    


def Add_Appiontment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=="POST":
        d_name=request.POST['doctor']
        p=request.POST['patient']
        dt=request.POST['date']
        t=request.POST['time']
        doctor = Doctor.objects.filter(name=d_name).first()
        patient = Patient.objects.filter(name=p).first()    
        try:
            # if dt:
            #     dt = datetime.datetime.strptime(dt, "%D-%m-%y").date()
            # else:
            #     raise ValidationError('Date is required')

            doctor_instance = Doctor.objects.get(name=d_name)
            Appiontment.objects.create(doctor=doctor,patient=patient,date=dt,time=t)
            error="no"
        except IntegrityError:
            error="yes"
    ap = {'doctor':doctor1, 'patient':patient1, 'error':error}
    return render(request, 'add_appiontment.html', ap)


def Delete_Appiontment(request,id):
    if request.user.is_staff:
        return redirect('login')
    Appiontment = Appiontment.objects.get(id.id)
    Appiontment.delete()
    return render('view_appiontment')
    
 


# def Add_Appiontment(request):
#     error = ""

#     if not request.user.is_staff:
#         return redirect('login')

#     if request.method == 'POST':
#         doctor = request.POST['doctor']
#         patient = request.POST['patient']
#         date = request.POST['date']
#         time = request.POST['time']

#         try:
#             Appiontment.objects.create(doctor=doctor, patient=patient, date=date, time=time)
#             error = "no"
#         except Exception as e:
#             # Catch a specific exception, such as IntegrityError, if possible
#             error = "yes"

#     ap = {'error': error}
#     return render(request, 'add_appiontment.html', ap)  
  
  
  
  
        
# def Add_Appiontment(request):
#     error = ""

#     if not request.user.is_staff:
#         return redirect('login')

#     if request.method == "POST":
#         d_name = request.POST.get('doctor')
#         p = request.POST.get('patient')
#         dt = request.POST.get('date')
#         t = request.POST.get('time')

#         try:
#             # Retrieve the Doctor instance based on the provided name
#             doctor_instance = Doctor.objects.get(name=d_name)

#             # Create the Appiontment instance with the retrieved Doctor instance
#             Appiontment.objects.create(doctor=doctor_instance, patient=p, date=dt, time=t)
#             error = "no"
#         except Doctor.DoesNotExist:
#             error = "Doctor not found"
#         except IntegrityError:
#             error = "Duplicate entry or other database integrity issue"

#     ap = {'error': error}
#     return render(request, 'add_appiontment.html', ap)
    
            
