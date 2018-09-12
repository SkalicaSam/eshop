from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    html = '''
    <h1>Hey Client, my app is running!</h1>
    <p>Check out our <a href="/events">offerings</a></p>
    '''
    
    return HttpResponse(html)


def event_listing(request):
    html = '''
    <ul>
        <li>Chill on the beach</li>
        <li>Camping in the woods</li>
        <li>Flying into the space</li>
    </ul>
    '''

    return HttpResponse(html)