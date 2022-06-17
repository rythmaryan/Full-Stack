#Created by aryan itself.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')   

# def removepunc(request):
#     val = request.GET.get("text","Default value")
#     chk = request.GET.get("analyze","Off")
#     print(val)
#     print(chk)
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("remove newline first")   

# def spaceremove(request):
#     return HttpResponse("space remove <br> <a href='/'>Back</a>")

# def charcount(request):
#     return HttpResponse("char count")   

def analyze(request):
    val = request.POST.get("text","Default value")
    chk = request.POST.get("analyze","Off")
    fullcaps = request.POST.get("fullcaps","Off")
    nlr = request.POST.get("nlr","Off")
    cc = request.POST.get("cc","Off")

    if chk == "on":
        punctuations = '''!()-[]{}:'"\,<>./?@#$%;^&*_~='''
        analyzed = ""
        for char in val:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove punctuations', 'analyzed_text':analyzed}
        val = analyzed
    if fullcaps == "on":
        analyzed = ""
        for char in val:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Full Uppercase conversion', 'analyzed_text':analyzed}
        val = analyzed
    if nlr == "on":
        analyzed = ""
        for char in val:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        val = analyzed
    if cc == "on":
        count = 0
        for char in val:
            count = count+1

        params = {'purpose': 'Count characters ', 'analyzed_text': count}
    if cc != "on" and nlr != "on"  and  fullcaps != "on" and chk != "on":
        return HttpResponse("Error: Please select a feature")
    
    return render(request, 'analyze.html', params)            
        