from django.shortcuts import render, redirect
from students.forms import StudentsForm
from students.models import Students
from django.contrib import messages
# Create your views here.


def std(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass

    else:
        form = StudentsForm()
    return render(request, 'index.html', {'form': form})


def view(request):
    students=Students.objects.all()
    return render(request,'view.html',{'students':students} )


def delete(request,id):
    students=Students.objects.get(id=id)
    students.delete()
    return redirect("/")

def update(request,id):
    update=Students.objects.get(id=id)
    form=StudentsForm(request.POST,instance=update)
    if form.is_valid():
        form.save()
        messages.success(request,"Student record is updated")
        return render(request,'edit.html',{'Students':update})


def edit(request,id):
    students=Students.objects.get(id=id)
    return render(request,'edit.html',{'students':students})



def filter(request):
    if request.method=="POST":
        gender=request.POST.get("gender")
        occupation = request.POST.get("occupation")
        oup=Students.objects.raw('select * from abcd where gender="'+gender+'" and occupation="'+occupation+'"')
        return render(request,'edit.html',{'Students':oup})

    else:
        empobj=Students.objects.raw("select * from abcd")
        return render(request, 'edit.html', {'Students': empobj})




