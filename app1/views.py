from django.shortcuts import render ,redirect
from .models import book
from .forms import bookform

# Create your views here.

# def home(request):
#     data=['apple','orang','banana']
 
#     return render(request,'home.html',{"ab":data})
    

def home(request):
    return render(request,'home.html')

def view_book(request):
    a=book.objects.all()
    return render (request,'view_book.html',{'book':a})

def add_book(request):
    a=bookform(request.POST or None)
    if a.is_valid():
        a.save()
        return redirect('view_books')
    return render(request,'add_book.html',{'form':a})

'my name is midhlaj'
