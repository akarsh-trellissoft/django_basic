from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    w_l=fulltext.split()
    d={}
    for w in w_l:
        if w  in d:
            d[w]+=1
        else:
            d[w]=1
    s=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(w_l),'s':s})
def about(request):
    return render(request,'about.html')
