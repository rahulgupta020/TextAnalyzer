# This file is created by Rahul Gupta
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def textanalyzed(request):
    textareatext = request.POST.get('entertext', 'default')
    # print(textareatext)
    removepun = request.POST.get('removepun', 'off')
    # print(removepun)
    lowercase = request.POST.get('lowercase', 'off')
    # print(lowercase)
    uppercase = request.POST.get('uppercase', 'off')
    # print(uppercase)
    charcount = request.POST.get('charcount', 'off')
    # print(charcount)
    wordcount = request.POST.get('wordcount', 'off')
    # print(wordcount)
    sentencecount = request.POST.get('sentencecount', 'off')
    # print(sentencecount)
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    # print(extraspaceremove)
    newlineremove = request.POST.get('newlineremove', 'off')
    # print(newlineremove)
    numberremove = request.POST.get('numberremove','off')
    # print(numberremove)

    if(removepun == 'on'):
        punctuation = '''
        !()-[]{};:'"\,<>./?@#$%^&*_~
        '''
        analyzed = ""
        for i in textareatext:
            if i not in punctuation:
                analyzed = analyzed + i
        printtext = {'purpose':'Removed Punctuation', 'analyzed_text':analyzed}
        textareatext=analyzed
        # return render(request, 'textanalyzed.html',printtext)
    
    if(lowercase == 'on'):
        analyzed = ""
        for i in textareatext:
            analyzed = analyzed + i.lower()
        printtext = {'purpose':'All Letter lowercase','analyzed_text':analyzed}
        textareatext=analyzed
        # return render(request, 'textanalyzed.html', printtext)

    if (uppercase == 'on'):
        analyzed = "" 
        for i in textareatext:
            analyzed = analyzed + i.upper()
        printtext = {'purpose':'Upper Case Letter','analyzed_text':analyzed}
        textareatext=analyzed
        # return render(request, 'textanalyzed.html', printtext)

    if(charcount == 'on'):
        analyzed = ""
        for i in textareatext:
            analyzed = len(textareatext)
        printtext={'purpose':'Count the Character','analyzed_text':analyzed}
        textareatext=analyzed
        # return render(request, 'textanalyzed.html', printtext)

    if(wordcount == 'on'):
        analyzed = ""
        for i in textareatext:
            analyzed = len(textareatext.split())
        printtext = {'purpose':'Count the Word', 'analyzed_text':analyzed}
        textareatext=analyzed
        # return render(request, 'textanalyzed.html', printtext)
    
    if(sentencecount =='on'):
        analyzed = ""
        print(textareatext)
        for i in textareatext:
            analyzed1 = len(textareatext.split('.'))
            analyzed1=analyzed1-1
            analyzed2 = len(textareatext.split('?'))
            analyzed2=analyzed2-1
            analyzed3 = len(textareatext.split('!'))
            analyzed3=analyzed3-1
            analyzed = analyzed1 + analyzed2 + analyzed3
        printtext = {'purpose':'Count the sentence','analyzed_text':analyzed}
        textareatext=analyzed
        # return render(request, 'textanalyzed.html', printtext)

    if extraspaceremove == 'on':
        analyzed=""
        for index, i in enumerate(textareatext):
            if not(textareatext[index]==" " and textareatext[index+1]==" "):
                analyzed = analyzed + i
        printtext = {'purpose':'Removed extra space', 'analyzed_text':analyzed}
        textareatext=analyzed
        # return render(request, 'textanalyzed.html', printtext)
            
    if newlineremove == 'on':
        analyzed=""
        for i in textareatext:
            if i !='\n':
                analyzed = analyzed + i
        printtext = {'purpose':'Removed new line', 'analyzed_text':analyzed}
        textareatext=analyzed
        # return render(request, 'textanalyzed.html', printtext) 

    if (numberremove == "on"):
        analyzed = ""
        numbers = '0123456789'

        for i in textareatext:
            if i not in numbers:
                analyzed = analyzed + i
        
        printtext = {'purpose': 'Removed Numbers', 'analyzed_text': analyzed}
        textareatext = analyzed
    
    if(removepun!="on" and lowercase!="on" and uppercase!="on" and charcount!="on" and wordcount!="on" and sentencecount!="on" and extraspaceremove!="on" and newlineremove!="on" and numberremove!="on"):
        return HttpResponse("Error")

    return render(request, 'textanalyzed.html', printtext)


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')