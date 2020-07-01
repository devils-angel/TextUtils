# i have created this file - Yukta
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    # getting the text from the user to analyze
    # included the POST method to prevent the passing of message through the URL
    text= request.POST.get('text','default')
    # getting the checkbox inputs
    punc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    
    # coding the logic for output
    if punc=="on":
        punctuation_list = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuation_list:
                analyzed = analyzed + char
        text = analyzed
        
    
    if fullcaps =="on":
        analyzed=""
        for char in text:
            analyzed += char.upper()
        
        text = analyzed
        
    
    if newlineremover =="on":
        analyzed=""
        for char in text:
            if char!="\n" and char!="\r":
                analyzed += char
        
        text = analyzed
    
    if extraspaceremover =="on":
        analyzed=""
        for index , char in enumerate(text):
            if not(text[index]=="" and tex[index]+1 == ""):
                analyzed += char
     
        text = analyzed
        
    
    if charcount == "on":
     
        analyzed = len(text)
        text  += "  " +str(analyzed)
        
    # passed the parameters to the analyze.html to display the analyzed text
    params = {'purpose': 'required changes','analyzed_text': text}
    return render(request,'analyze.html',params)
    