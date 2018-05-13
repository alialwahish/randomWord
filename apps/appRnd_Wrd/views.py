from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string
# Create your views here.
v=""
i=0
def index(request):
    
    v="Generate Word"
    return render(request,'appRnd_Wrd/index.html',{'v':v})

def getThat(request):
    global i
    i+=1
    if request.method=="POST":
        v=get_random_string(length=14)
       
        context ={'v':v ,'i':i}
       
        print ("add attemp")
        
    return render(request,'appRnd_Wrd/index.html',context)
