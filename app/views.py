from django.shortcuts import render,redirect
from app.models import Todolist
# Create your views here.


def calculator(request): 
    first_name = None
    last_name = None
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
          
    name_by_get_method = request.GET.get('name') 
    last_name_by_get_method = request.GET.get('last_name')
    context = {
        'first_name':first_name,
        'last_name':last_name,
        'name_by_get_method':name_by_get_method,
        'last_name_by_get_method':last_name_by_get_method
    }
    
    
    return render(request,'calculator.html',context)



def index(request):
    todolists = Todolist.objects.all()
    status = request.GET.get('status')
    search = request.GET.get('search')
    # print(search)
    
    
    if status == None:
        todolists = Todolist.objects.all()

    elif status == "completed":
        todolists = Todolist.objects.filter(is_completed = True)
    else:
        todolists = Todolist.objects.filter(is_completed = False)
    error = ""
    if search: 
        todolists = Todolist.objects.filter(title__icontains = search)
    # print(todolists)
    
    if request.method == "POST": 
        title = request.POST.get('todolist') 
        days = request.POST.get('days')
        Todolist.objects.create(title = title,days = days,is_completed = False)
        return redirect('/')
    
    
    else:   
        context = {
        'todolists':todolists,
        'error':error
        }
        
        
        return render(request,'index.html',context)

    

def tododetails(request,id):
    todolist = Todolist.objects.get(id = id)
    context = { 
               'todolist':todolist
               }
    return render(request,'tododetails.html',context)




def updateTodo(request,id):
    todolist = Todolist.objects.get(id = id)
    if request.method == "POST": 
        title = request.POST.get('title') #hehehhaha
        days = request.POST.get('days') #11
        is_completed = request.POST.get('is_completed') #none
        
        todolist.title = title
        todolist.days = days
        
        if is_completed == "on": 
            todolist.is_completed = True
        elif not is_completed:
            todolist.is_completed = False
        else:
            todolist.is_completed = False
           
           
        todolist.save()
        
        return redirect('/')
          
    context = { 
               'todolist':todolist
               }
    return render(request,'updateTodo.html',context)


def delete(request,id): 
    todolist = Todolist.objects.get(id =id)
    todolist.delete()
    return redirect('/')
    