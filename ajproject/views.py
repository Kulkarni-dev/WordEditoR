# I have created this file -ajit
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse('''<h1>Hello</h1> <a href="https://www.youtube.com/">This is a HyperLink to YouTube homepage</a>''')

    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover =request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Punctuations Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Fully Capatilized', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] ==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    elif charcount == "on":
        analyzed = len(djtext)
        params = {'purpose': 'Following is the Character Count', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        analyzed = djtext
        params = {'purpose': '''Following is the text you've entered''', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    return render(request, 'analyze.html', params)
