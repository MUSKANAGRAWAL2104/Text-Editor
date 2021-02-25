from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    dtext=(request.POST.get('text', 'default'))
    punc = (request.POST.get('removepunc', 'off'))
    upper = (request.POST.get('capitalize', 'off'))
    newline = (request.POST.get('removeline', 'off'))
    space = (request.POST.get('removespace', 'off'))
    find=(request.POST.get('find','default'))
    replace=(request.POST.get('text','default'))
    bchar=1
    bword=0
    bsent=1
    count=0
    for i in range(0,len(dtext)-1):
        if(dtext[i] != "\r"):
            bchar+=1
        if ((dtext[i] != ' ' and (dtext[i + 1] == ' ' or dtext[i + 1] == '\n' or dtext[i + 1] == '\r')) or i == len(dtext) - 2):
            if (dtext[i] == '\r' and dtext[i + 1] == '\n'):
                pass
            else:
                bword+=1
        if(dtext[i] =='.' or dtext[i]=='\n'):
            bsent+=1
    if(punc=='on'):
        punctuations='''.,?!:;-(){}[]'"*'''
        analyzed=""
        for char in dtext:
            if char not in punctuations:
                analyzed=analyzed+char
        dtext=analyzed
    if(upper=='on'):
        analyzed=''
        for char in dtext:
            analyzed+=char.upper()
        dtext=analyzed
    if(newline=='on'):
        analyzed = ''
        for char in dtext:
            if(char!='\n' and char!='\r'):
                analyzed += char
        dtext=analyzed
    if (space == 'on'):
        analyzed = ''
        for i in range(0,len(dtext)-1):
            if dtext[i]==' ' and dtext[i+1]==' ':
                continue
            else:
                analyzed += dtext[i]
        dtext=analyzed

    if(len(find) != 0 and len(replace) != 0):
        count=dtext.count(find)
        dtext.replace(find,replace)
    achar = 1
    aword = 0
    asent = 1
    for i in range(0, len(dtext) - 1):
        if (dtext[i] != "\r"):
            achar += 1
        if ((dtext[i] != ' ' and (dtext[i + 1] == ' ' or dtext[i + 1] == '\n' or dtext[i + 1] == '\r')) or i == len(dtext) - 2):
            if (dtext[i] == '\r' and dtext[i + 1] == '\n'):
                pass
            else:
                aword += 1
        if (dtext[i] == '.' or dtext[i] == '\n'):
            asent += 1
    params = {'analyzed_text': dtext,
              'before_char':bchar,
              'before_word':bword,
              'before_sent':bsent,
              'after_char':achar,
              'after_word':aword,
              'after_sent':asent,
              'number_to_find':find,
              'word_count':count
              }
    if(space != 'on' and newline != 'on' and upper != 'on' and punc != 'on' and len(find)==0):
        return render(request,'error.html',params)
    return render(request,'analyze.html',params)
def about(request):
    return render(request,'about.html')
def feedback(request):
    return render(request,'feedback.html')
def thankyou(request):
    return render(request,'Thank You.html')


