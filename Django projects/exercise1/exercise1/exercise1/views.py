from django.http import HttpResponse

def site1(request):
    return HttpResponse('''<h3>Site 1</h3><a href="https://www.google.co.in/">Google site</a>''')

def site2(request):
    return HttpResponse('''<h3>Site 2</h3><a href="https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns#Merging-Intervals">DP site</a>''')

def site3(request):
    return HttpResponse('''<h3>Site 3</h3><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Django site</a>''')