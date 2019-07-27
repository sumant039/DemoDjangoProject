# created this file by MYSELF


from django.http  import HttpResponse

def index(request):
    return  HttpResponse('''<h1>hello sumant</h1>  <a href="https://stackoverflow.com/questions/24682155/django-user-registration-with-error-no-such-table-auth-user">Click Here</a>''')

def about(request):
    return HttpResponse("Hi sumant singh ")

def backed(request):
    return HttpResponse("Hi sumant singh <a href='/'>'back'<a/> ")

def frientend(request):
    return HttpResponse("Hi sumant singh ")

def love(request):
    return HttpResponse("Hi sumant singh ")
