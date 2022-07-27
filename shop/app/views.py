
from .forms import StudentForm,StudentCreateForm,StudentUpdateForm
from django.shortcuts import redirect, render
from .models import Person,Student
from .forms import Personform
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.contrib import messages
# Create your views here.
def create(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        address=request.POST['address']
        mobile=request.POST['mobile']
        if Person.objects.filter(email=email).exists():
             messages.success(request, f'Email already exists')
        else:
            form=Person(first_name=first_name,last_name=last_name,email=email,address=address,mobile=mobile)
            form.save()
            messages.success(request, f'Record Insterted Successfully')
            return redirect("/")
    show_data=Person.objects.all().values()
    return render(request,"index.html",{'show_data':show_data})


def delete(request,id):
    a=Person.objects.filter(id=id)
    a.delete()
    messages.success(request, f'Record Deleted Successfully')
    return redirect("/")

def updaterecord(request,id):
    if request.method=="POST":
        email=request.POST['email']
        obj=Person.objects.get(id=id)
        form=Personform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, f'Record Updated Successfully')
            return redirect("/")
    else:
        obj=Person.objects.get(id=id)
        form=Personform(instance=obj)
    return render(request,"update.html",{'form':form})


  
def edit_data(request,id):
    obj=Person.objects.get(id=id)
    show_data=Person.objects.all().values()
    return render(request,'index.html',{'update':obj,'show_data':show_data})

def update_item(request,id):
    obj=Person.objects.get(id=id)
    obj.first_name=request.POST['first_name']
    obj.last_name=request.POST['last_name']
    obj.email=request.POST['email']
    obj.address=request.POST['address']
    obj.mobile=request.POST['mobile']
    obj.save()
    messages.success(request, f'Record Updated Successfully')
    return redirect("/")

  
  
        





class ShowStudent(ListView):
    model=Student
    template_name='student_show.html'
    context_object_name='obj'
    
    # def get_queryset(self):
    #     return Student.objects.filter(stream='bca')
    
    # def get_context_data(self, *args,**kwargs):
    #     context = super().get_context_data(*args,**kwargs)
    #     context["show_data"] =Student.objects.filter(stream='bcom')
    #     return context
    
class Student_form_data(FormView):
    template_name='student_form.html'
    form_class = StudentForm
    success_url="Student_form_data"
    def form_valid(self, form):
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['stream'])
        return super().form_valid(form)

class Student_create(CreateView):
    form_class=StudentCreateForm
    template_name="student_create.html"
    success_url="ShowStudent"

class UpdateView(UpdateView):
    model=Student
    form_class=StudentUpdateForm
    template_name="student_update.html"
    success_url="/ShowStudent"
    
class Student_Delete(DeleteView):
    model=Student
    template_name="student_delete.html"
    success_url="/ShowStudent"

def search(request):
    if request.method=="POST":
        record_search=request.POST['record_search']
        value=Person.objects.filter(first_name__iexact= record_search)
        return render(request,"search.html",{'value':value})
    else:
        return render(request,"search.html")