# DemoDjangoProject
DjangoDemo Project 
################
Changing in setting file and url file 
and creating  one  view .py file  

# changing setting.py

Templates [
 'DIRS': ['templates'],
 ]
 
# Data Base changing 
 
 ATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Changing in view.py file 

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

#changing in URL.py file


from django.contrib import admin
from django.urls import path
#from  django.contrib import admin
#from django.urls import path
from.import view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.index,name='index'),
    path('about',view.about,name='about'),
    path('backed', view.backed, name='backed'),
    path('frientend', view.frientend, name='frientend'),
    path('love', view.love, name='love')


]