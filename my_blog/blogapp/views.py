from django.shortcuts import render

# Create your views here.

def index(request):
    context ={}
    #此处的hello是模板index.html中的模板变量
    context['hello']=u'你是疯狂的'
    return render(request,'index.html',context)
