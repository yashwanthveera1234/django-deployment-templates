from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def other(request):
    context_dic = {'text':'Hello','number':100}
    return render(request,'basic_app/other.html',context = context_dic)

def relative(request):
    return render(request,'basic_app/relative_url_temp.html')
