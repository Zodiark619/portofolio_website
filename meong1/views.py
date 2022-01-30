from django.shortcuts import render
from .portfolio1 import meong
# Create your views here.



def index(request):
    return render(request,'index.html',{})
def portfolio(request):
    return render(request,'portfolio.html',{})
def portfolio1(request):
    context={}
    if request.method=='POST':
        try:
            input1=int(request.POST['first_param'])
            input2=int(request.POST['second_param'])
            if request.POST['operator']=='+':
                result=input1+input2
                context['result']=result
                context['operator']=f"{input1} + {input2} = "
                
            elif request.POST['operator']=='-':
                result=input1-input2
                context['result']=result
                context['operator']=f"{input1} - {input2} = "


            if request.POST['bool_param']=='printed':
                message='Result is printed!'
                context['message']=message
            elif request.POST['bool_param']=='not_printed':
                message='Result is not printed!'
                context['message']=message
        except:
            message='Error : Either inputs must be numeric type with integer numbers only'
            context['message']=message




        # print(result)
        # print(a,b)
    return render(request,'portfolio1_arithmetic.html',context)
