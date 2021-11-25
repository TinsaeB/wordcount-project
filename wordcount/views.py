import operator

from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "homepage.html", {"hithere": "This is me"})


def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1  # Increase
        else:
            worddictionary[word] = 1  # Add to dictionary

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html", {'fulltext': fulltext, 'count': len(wordlist), 'worddictionary': sortedwords})


def about(request):
    return render(request, "about.html")
