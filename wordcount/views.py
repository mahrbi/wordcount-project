from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',{"hidear":'this is me'})

def about(request):
    return render(request,'about.html')

def eggs(request):
    return HttpResponse("eggs are greate")

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    word_dic={}
    for word in wordlist:
        if word in word_dic:
            word_dic[word]+=1
        else:
            word_dic[word]=1
    sortedword = sorted(word_dic.items(),key=operator.itemgetter(1))

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedword':sortedword})
