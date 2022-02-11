from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy,reverse

# Create your views here.
challenges = {'jan': "this is january",
              'feb': 'this is feb 2', 'march': 'this march 3'}

def start(reqquest):
    lis=list(challenges.keys())
    title="Hello "+lis[2]
    text='Every Months task'
    return render(reqquest,'challenges/challenge.html',{'text':text,'title':title})

def index(request,month):
    months=list(challenges.keys())
    return render(request,'challenges/index.html',{'months':months})
   


def call_by_number(request, month_id):
    month_list = list(challenges.keys())
    if month_id > len(month_list):
        return HttpResponse("value should not greater than month's no."+str(month_id))

    m = month_list[month_id-1]
    print(m)
    path=reverse('monthly_challenges',args=[m])
    return HttpResponseRedirect(path)
