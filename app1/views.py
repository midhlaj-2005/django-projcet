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
    a=bookform(request.POST or None,request.FILES or None)
    if a.is_valid():
        a.save()
        return redirect('view_books')
    return render(request,'add_book.html',{'form':a})

'my name is midhlaj'

def update_book(request, id):
    a=book.objects.get(id=id)
    form=bookform(request.POST or None, request.FILES or None ,instance=a)
    if form.is_valid():
        form.save()
        return redirect ('app')
    return render(request,'update.html',{"form":form})

def delete_book(request,id):
    a=book.objects.get(id=id)
    if request .method =="POST":
        a.delete()
        return redirect ('view_book')
    return render (request,'delete_book.html',{'book':a})
  