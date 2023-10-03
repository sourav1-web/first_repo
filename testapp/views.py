from django.shortcuts import render
from testapp.models import Student
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from testapp.forms import SignupForm
from django.db.models import Q
# Create your views here.
def SchoolView(request):
    return render(request,'testapp/school.html')


def RetrieveView(request):
    return render(request,'testapp/index.html')


@login_required
def StudentView(request):
    filter=Q()
    student_type=request.GET.get('student_type','all')
    student_search=request.GET.get('search','')
    if student_type== 'first_class':
        filter &= Q(marks__gt=60)
    elif student_type== 'second_class':
        filter &= Q(marks__gt=50,marks__lt=60)
    elif student_type== 'third_class':
        filter &= Q(marks__gt=30,marks__lte=50)    
    if student_search:
        filter &= Q(Q(rollno__icontains=student_search)
                    | Q(name__icontains=student_search)  
                    | Q(email__icontains=student_search)
                    | Q(addr__icontains=student_search)
                    )


    student_list=Student.objects.filter(filter).order_by('rollno')
    context={
        'student_list':student_list,
        'student_type':student_type,
        'student_search':student_search
        }
    return render (request,'testapp/list.html',context)

@login_required
def StudentPassView(request):
    student_list=Student.objects.filter(marks__gt=30).order_by('rollno')

    return render (request,'testapp/pass.html',{'student_list':student_list})



def LogoutView(request):
    return render(request,'testapp/logout.html')

def SigninView(request):
    form=SignupForm()
    if request.method =='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})

from django.shortcuts import redirect
def DeleteView(request,id):
    user=Student.objects.get(id=id)
    user.delete()
    if request.GET.get('page',None):
        return redirect('/specific')
    elif request.GET.get('pass',None):
        return redirect('/pass')
    
    return redirect('/list')
    
from testapp.forms import StudentForm
def UpdateView(request,id):
    user=Student.objects.get(id=id)
    form=StudentForm(instance=user)
    if request.method == 'POST':
        form=StudentForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
        return redirect('/list')    
    return render(request,'testapp/studentform.html',{'form':form})        

def InsertView(request):
    form=StudentForm()
    if request.method =='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list')    
    return render(request,'testapp/insert.html',{'form':form}) 

def SpecificColumn(request):
    
    Student_list=Student.objects.all().order_by('-marks')
    my_dict={'student_list':Student_list,}
    print(Student_list)
    type='specific1'
    return render(request,'testapp/specific.html',my_dict)       



