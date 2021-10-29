from django.http import HttpResponse
from django.shortcuts import render
import string 


def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', '')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    puncs = string.punctuation
    analyzedtext = djtext
    purpose = ''

    if djtext == '':
        return render(request, 'error.html')

    if removepunc == 'on':
        purpose += 'Remove Punctuations '
        temptext = ''
        for char in analyzedtext:
            if char not in puncs:
                temptext = temptext + char
        analyzedtext = temptext

    if fullcaps == 'on':
        purpose += 'Capitalize all letter '
        analyzedtext = analyzedtext.upper()
    
    if newlineremove == 'on':
        purpose += "Remove Lines "
        temptext = '' 
        for char in analyzedtext:
            if char != '\n'and char != '\r':
                temptext = temptext + char
        analyzedtext = temptext

    if spaceremove == 'on':
        purpose += 'Remove extra space '
        temptext = ''
        for i,char in enumerate(analyzedtext):
            if not (analyzedtext[i] == ' ' and analyzedtext[i+1] == ' '):
                temptext = temptext + char
        analyzedtext = temptext

    if charcount == 'on':
        purpose += 'Charecter Count '
        if analyzedtext != djtext:
            analyzedtext += '\nLength of text :' + str(len(analyzedtext))
        else:
            analyzedtext = 'Length of text :' + str(len(analyzedtext))

    params = {'purpose' : purpose, 'djtext' : djtext, 'result' : analyzedtext}
    return render(request, 'analyze.html', params)
