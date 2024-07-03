from django.shortcuts import render

# Create your views here.


def calculator(request): 
    first_name = None
    last_name = None
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
       
    context = {
        'first_name':first_name,
        'last_name':last_name
    }
    
    return render(request,'calculator.html',context)
    