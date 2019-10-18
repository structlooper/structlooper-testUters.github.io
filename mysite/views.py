from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # dicts = {
    #     'name':'Deepak',
    #     'place':'New Delhi'
    # }
    
    return render(request,'index1.html')
    # with open(r'E:\python\django_data\mysite\mysite\one.txt','r') as f:
    #     data = f.readlines()
    #     return HttpResponse(data)

def process(request):
    # POST the text from imputing
    djtext = (request.POST.get('text','default'))
    remove_punc = request.POST.get('removepunc', 'off')
    captial_func = request.POST.get('captial', 'off')
    new_line = request.POST.get('new_line','off')
    extra_space = request.POST.get('extra_space','off')
    char_count = request.POST.get('char_count','off')
    # printing the text
    # print(remove_punc)
    # print(djtext)
    penctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""" 
    if remove_punc == 'on':
        anlizer= ""
        for char in djtext:
            if char not in penctuation:
                anlizer += char
        pera = {
        'purpose' : 'Removed punctuation',
        'analized': anlizer,
        }
        djtext = anlizer
        # return render(request,'web1.html',pera)
    if captial_func == 'on':
        # print(captial_func)
        anlizer = ""
        for char in djtext:
            anlizer += char.upper()
        pera = {
        'purpose' : 'Upper Function',
        'analized': anlizer,
        }
        # print(anlizer)
        djtext = anlizer
        # return render(request,'web1.html',pera)
    if (new_line == 'on'):
        anlizer = ""
        for char in djtext:
            if char !='\n' and char != '\r':
                anlizer += char
        pera = {
        'purpose' : 'New Lines Removed',
        'analized': anlizer,
        }
        djtext = anlizer
        # return render(request,'web1.html',pera)
    if (extra_space == 'on'):
        anlizer = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                anlizer += char
            
        pera = {
        'purpose' : 'New Lines Removed',
        'analized': anlizer,
        }
        djtext = anlizer
        # return render(request,'web1.html',pera)
    if (char_count == 'on'):
        anlizer = ''
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " ):
                anlizer += char
            
        pera = {
        'purpose' : 'Charactor Counter',
        'analized': f'The charactor you entered : {len(anlizer)}',
        }
        djtext = anlizer
    if (remove_punc != 'on' and captial_func != 'on' and new_line != 'on' and extra_space != 'on' and char_count!='on'):
        return HttpResponse("<h1>You have not using any function<h1> <br><h3>Try use any function and use agin<h3>")
    return render(request,'web1.html',pera)
def links(request):
    return HttpResponse('<h1>This are the Links</h1><br><a href="https://www.facebook.com/">facebook</a><br><a href="https://www.youtube.com/">youtube</a><br><a href="https://www.twitter.com/">twitter</a><br>')
    