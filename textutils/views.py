#created by me-pratik
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={'name':'harry','place':'UDAS'}
    return render(request,'index.html',params)

def about(request):
    return HttpResponse("<a href=""><b> Home</b></a>this is about page")

def analyze(request):
    text=(request.POST.get('text','default'))
    removepunc=(request.POST.get('removepunc','default'))
    uppercase=(request.POST.get('uppercase','default'))
    removenewline=(request.POST.get('removenewline','default'))
    extraspaceremover=(request.POST.get('extraspaceremover','default'))
    charcount=(request.POST.get('charcount','default'))
    if(removepunc=="on"):
        punctuations='''{/[-[\]{}()*'';:+?.,\\^$|#\s]/g, "\\$&"<>}'''
        #analyzed=text
        analyzed=""
        for char in text:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'remove punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(uppercase=="on"): 
        analyzed=""
        for char in text:
            analyzed=analyzed+char.upper()
        params={'purpose':'UPPERCASE','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(removenewline=="on"): 
        analyzed=""
        for char in text:
            if(char!="\n" and char!="\r"):
                analyzed=analyzed+char
        params={'purpose':'removenewline','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(extraspaceremover=="on"): 
        analyzed=""
        for index,char in enumerate(text):
            if not(text[index]==" " and text[index+1]==" "):
                analyzed=analyzed+char
            
        params={'purpose':'Extra space remover','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(charcount=="on"): 
        analyzed=""
        cnt=0
        for char in text:
            cnt=cnt+1
        params={'purpose':'charcount','analyzed_text':cnt}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Erroor")

def capitalize(request):
    return HttpResponse("<a href=""><b> Home</b></a>this is capitalize page")


def newlineremove(request):
    return HttpResponse("<a href='/'><b> Home</b></a>this is new line removwew")
    
def charcount(request):
    return HttpResponse("<a href='/'><b> Home</b></a>this is charcount")