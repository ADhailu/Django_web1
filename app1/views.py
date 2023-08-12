from django.shortcuts import render, redirect
from .models import Home, Services, About, Contact, ContactPage
from django.contrib.auth.models import User, auth
# Create your views here.
def home(request):
    content = Home.objects.all().first()
    return render(request, 'index.html', {"content": content})

def services(request):
    content = Services.objects.all()
    return render(request, 'services.html', {'content': content})

def register(request):
    if request.method== 'POST':
        first_name = request.POST['name']
        email = request.POST['email']
        userName = request.POST['username']
        password = request.POST['password']

        data = User.objects.create_user(first_name=first_name,email=email,username=userName,password=password)
    return render(request, 'register.html')
        

def login(request):
    if request.method== 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username , password=password)
        if not user:
            return render(request, 'login.html', {'error': 'Invalid Credentials!'})
        else :
            auth.login(request.user)
            return redirect('home_url')
    return render(request, 'login.html')

def about(request):
    content = About.objects.all().first()
    return render (request,'about.html', {'content': content})
    print(content.aboutimage)

def contact(request):

    ContactInfo = ContactPage.objects.all().first()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

    else:
        pass
    
    return render(request, 'contact.html', {'ContactInfo': ContactInfo})