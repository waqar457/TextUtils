# I have created this file-waqar
from django.http import HttpResponse
from django.shortcuts import render


# Code for Video 6
'''
def index(request):
    return HttpResponse("I am Home Page")

def about(request):
    return HttpResponse("I am About Page")

'''
#---------------------------------------------------------------------
# Code for Video 7-8-9
'''
def index(request):
    # prams={'name':'waqar','place':'Thane'}
    # return render(request,'index.html',prams)
    # return HttpResponse('I am Home')
    return render(request, 'index.html')

def removepunc(request):
    djtext=request.GET.get('text','default')
    #Get The Text
    print(djtext)
    # Analyze the text
    return HttpResponse('I am Remove Punc')

def capitilizefirst(request):
    return HttpResponse('I am Capitilize First')

def newlineremover(request):
    return HttpResponse('I am New Line Remover')

def spaceremover(request):
    return HttpResponse('I am Space Remover')

def charcount(request):
    return HttpResponse('I am Char Count')


'''
#------------------------------------------------
# Code for Video 10

def index(request):

    return render(request, 'index.html')

def analyze(request):
    #Get The Text
    djtext=request.POST.get('text','default')

    # Check checkBox Value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    # print(djtext)
    # print(removepunc)

    # analyzed=djtext

    #Check which check box on
    if removepunc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        prams={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        # Analyze the text
        # return render(request,'analyze.html',prams)

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        prams={'purpose':'Change To Upper Case','analyzed_text':analyzed}
        djtext=analyzed
        # Analyze the text
        # return render(request,'analyze.html',prams)


    if(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char !='\n' and char !='\r':
                analyzed=analyzed+char

        prams={'purpose':'New Line Remover','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', prams)


    if(extraspaceremover=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if(djtext[index]==" " and djtext[index+1]==" "):
                pass
            else:
                analyzed=analyzed+char
        prams = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', prams)


    if(charcount=='on'):
        analyzed=""
        for char in range(len(djtext)):
            analyzed=char+1

        prams = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', prams)

    if(removepunc!='on' and charcount!='on' and extraspaceremover!='on' and newlineremover!='on'):
        return  HttpResponse('Please select Operation any Try agian')

    return render(request,'analyze.html',prams)