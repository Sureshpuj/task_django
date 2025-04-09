from django.shortcuts import render

# Create your views here.
name = "John"
age = 20
def index(request):

    return render(request,'myapp\index.html',)