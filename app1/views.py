from django.shortcuts import render,HttpResponse,redirect
from .forms import StudentForm
from .models import Student
# from django.utils

# Create your views here.
def regstudent(request):
    form=StudentForm()
    if request.method=='POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('registration successful!.....')
        return render(request,'reg.html',{'form':form})
    return render(request,'reg.html',{'form':form})

def read_all(request):
    data=Student.objects.all()
    return render(request,'all.html',{'data':data})

def read_one(request,id):
    data=Student.objects.get(id=id)
    return render(request,'one.html',{'data':data})

def update_record(request,id):
    data=Student.objects.get(id=id)
    form=StudentForm(instance=data)
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            # data.name=form.cleaned_data['name']
            # data.age=form.cleaned_data['age']
            # data.gender=form.cleaned_data['gender']
            # data.st_img=form.cleaned_data['st_img']
            # data.email=form.cleaned_data['email']
            # data.save()
            form.save()
            return redirect('all')
        return render(request,'reg.html',{'form':form,'data':data})
    return render(request,'reg.html',{'form':form,'data':data})

def del_record(request,id):
    data=Student.objects.get(id=id)
    return render(request,'delcon.html',{'data':data})

def delete_r(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    print('deleted')
    return redirect('all')
    
    
