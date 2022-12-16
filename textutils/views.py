# custom view by me
from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return HttpResponse("Welcome Babes!!!")

def aboutBabes(request):
    return HttpResponse('''<a href="http://www.google.com">"Shh.............."</a>''')

def showFile(request):
    file=open('/home/pmondal/TripwireDocs/Aws_config.txt','r')
    # print(file.read())
    return HttpResponse(file.read())

def index(request):
    # return HttpResponse("Hom")
    return render(request,'index.html')

def removePunc(request):
    print(request.GET.get('inputText','None'))
    txt=request.GET.get('inputText','None')
    return HttpResponse("removePunc   "+txt)

def capFirst(request):
    return HttpResponse("capFirst")

def removeNewLine(request):
    return HttpResponse("removeNewLine")

def removeSpace(request):
    return HttpResponse("removeSpace")

def countChar(request):
    return HttpResponse('''<a href="/"><</a>countChar''')

def analyser(request):
    type=request.POST.get('analysisType')
    txt=request.POST.get('inputText')
    if type=="RP":
        type="Remove Punctuations"
        txt=remPunc(txt)
    elif type=="RS":
        type="Remove Spaces"
        txt=remSpace(txt)
    else:
        type="Original Text"

    parms={'type':type,'txt':txt}
    return render(request,'analysedText.html',parms)

def remPunc(txt):
    punc='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    cleanText=""
    for char in txt:
        if char not in punc:
            cleanText=cleanText+char
    return cleanText

def remSpace(txt):
    return txt.replace(" ","")