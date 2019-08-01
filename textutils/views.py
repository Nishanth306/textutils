from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def analyse(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off') # to see whether remove punc is chaecked or not
    capitaltext=request.POST.get('capitaltext','off') # to see whether capital text is chaecked or not
    charcount = request.POST.get('charcount', 'off') # to see whether char countis chaecked or not
    newlineremover = request.POST.get('newlineremover', 'off') # to see whether new line remover is chaecked or not
    spaceremover = request.POST.get('spaceremover', 'off') # to see whether extra space remover is chaecked or not

# FOR REMOVING PUNCTUATIONS

    if removepunc=='on':
        punctuation=':;",.~`!@#$'
        analysed=""
        for char in djtext:
            if char not in punctuation:
                analysed=analysed+char
        djtext=analysed
        params = {'purpose': 'remove punctuations', 'analysed_text': analysed}

# FOR CAPITAL TECT

    if capitaltext=='on':
        analysed = ""
        for char in djtext:
            analysed= analysed + char.upper()
        djtext=analysed
        params = {'purpose': 'Capitalised text', 'analysed_text': analysed}

# FOR CHARACTER COUNT

    if charcount=='on':
        analysed=0

        for char in djtext:
            if char!=" ":
                analysed=analysed+len(char)
        djtext=analysed
        params = {'purpose': 'Character count', 'analysed_text': analysed}

# for removing new lines

    if newlineremover=='on':
        analysed=""
        for char in djtext:
            if char!='\n' and char!='\r':
                analysed=analysed+char
        djtext=analysed
        params = {'purpose': 'New line removal', 'analysed_text': analysed}

# For removing extra space remover

    if spaceremover=='on':
        analysed=""
        for index,char in enumerate(djtext):
            if not( djtext[index]==" " and djtext[index+1]==" " or djtext=='\n'):
                analysed=analysed+char
        djtext=str(analysed)
        params = {'purpose': 'Extra space remover', 'analysed_text': analysed}
    if spaceremover == 'on' or newlineremover == 'on' or charcount == 'on' or capitaltext == 'on' or removepunc == 'on':
        return render(request, 'analyse.html', params)
    else:
        return HttpResponse("error")




























