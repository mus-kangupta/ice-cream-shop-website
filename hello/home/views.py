from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.
def index(request):# this is url dispatching
    return render(request, 'home/index.html')
        #return HttpResponse("This is homepage")
def about(request):# this is url dispatching
     return render(request, 'about.html')
    #return HttpResponse("This is about page")
def services(request):# this is url dispatching
      return render(request, 'services.html')
    #return HttpResponse("This is services page")
#def contact(request):
      
      #if request.method=="POST":
      #return render(request, 'contact.html')
    #return HttpResponse("This is contact page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent")

    return render(request, "contact.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('/register/')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('/register/')

        # Create new user
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Registration successful! Please login.")
        return redirect('/login/')

    # If request is GET → render registration form
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home') # type: ignore
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
    



