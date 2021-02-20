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
    if(find):
        fword=0
        for i in range(0,len(dtext)):
            print(dtext[i])
            if(dtext[i]==find[0] and i+len(find)!='\n' and i+len(find)!='\r'):
                j=1
                flag=0
                while(j<len(find)):
                    if(dtext[i+j]!=find[j]):
                        flag=1
                        break
                    j+=1
                if(flag==0):
                    fword+=1
                    if(replace):
                        dtext=dtext.replace('find','replace')
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
    params = {'analyzed_text': dtext,'before_char':bchar,'before_word':bword,'before_sent':bsent,'after_char':achar,'after_word':aword,'after_sent':asent,'word_count':fword,'number_to_find':find}
    if(space != 'on' and newline != 'on' and upper != 'on' and punc != 'on' and len(find)==0):
        return render(request,'error.html',params)
    return render(request,'analyze.html',params)


