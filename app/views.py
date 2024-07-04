from django.shortcuts import render
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
    names = ['bisesh','sushant','saroj']
  
    context = {
        'todolists':todolists
    }
    return render(request,'index.html',context)

    