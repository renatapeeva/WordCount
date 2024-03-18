from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()

    worddictionary = {}
    for word in words:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltextt':fulltext, 'number':len(words), 'sortedwords': sortedwords})

def about(request):
    return render(request, 'about.html')