#This file is created by "me" in the main project folder namely, text-utilities.

from django.shortcuts import render
from django.http import HttpResponse
import string

# Create your views here.

def index(request):
    # return HttpResponse("Hello from index")
    return render(request,'text_utilities/index.html')

def analyze(request):
    removePunc = request.POST.get('removePunc','off')
    allCaps = request.POST.get('allCaps','off')
    removeNewLine = request.POST.get('removeNewLine','off')
    removeExtraSpace = request.POST.get('removeExtraSpace','off')
    charactersCount = request.POST.get('charactersCount','off')
    text = request.POST.get('text','default')
    params = {"status":"Error","status2":"is not","purpose":"Error","analyzed_text":"Please do select a option or some input text to analyze.","charCount":"off"}

    if removePunc == 'on' and text != "":
        final_text = ""
        for letter in text:
            if letter in string.punctuation:
                continue
            else:
                final_text += letter
        params = {"status":"Success","status2":"is","purpose":"Remove Punctuation","analyzed_text":final_text,"charCount":charactersCount}
        text = final_text
        #return render(request,'text_utilities/analyze.html',params)

    if allCaps == "on" and text != "":
        final_text = ""
        for letter in text:
            final_text += letter.upper()
        params = {"status":"Success","status2":"is","purpose":"Uppercase","analyzed_text":final_text,"charCount":charactersCount}
        text = final_text
        # return render(request,'text_utilities/analyze.html',params)

    if removeNewLine == "on" and text != "":
        final_text = ""
        for letter in text:
            if letter != "\n" and letter != "\r":
                final_text += letter
        params = {"status":"Success","status2":"is","purpose":"Remove New lines","analyzed_text":final_text,"charCount":charactersCount}
        text = final_text
        # return render(request,'text_utilities/analyze.html',params)

    if removeExtraSpace == "on" and text != "":
        final_text = ""
        for index, letter in enumerate(text):
            if not(text[index] == " " and text[index+1] == " "):
                final_text += letter
        params = {"status":"Success","status2":"is","purpose":"Remove Extra Space","analyzed_text":final_text,"charCount":charactersCount}
        text = final_text
        # return render(request,'text_utilities/analyze.html',params)

    if charactersCount == "on" and text != "":
        length = len(text)
        # for letter in text:
        #     charactersCount_text += 1
        params = {"status":"Success","status2":"is","purpose":"Characters Count","count":length,"analyzed_text":text,"charCount":charactersCount}
        # return render(request,'text_utilities/analyze.html',params)

    if(removePunc != 'on' and allCaps != "on" and removeNewLine != "on" and removeExtraSpace != "on" and charactersCount != "on"):
        params = {"status":"Error","status2":"is not","purpose":"Error","analyzed_text":"Please do select a option or some input text to analyze."}
        return render(request,'text_utilities/analyze.html',params)

    return render(request,'text_utilities/analyze.html',params)
