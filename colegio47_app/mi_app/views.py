from django.http import HttpResponse

def index(request):
    return HttpResponse("index page")
def hello(request, username):
    return HttpResponse("<h2>hello %s</h2>" % username)

def about(request):
    return HttpResponse('About')



                   
    