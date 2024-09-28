from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout

# Create your views here.
def home(request):
    return render(request , 'authentication/index.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            # Use 'first_name' instead of 'firstname'
            fname = user.first_name

            context = {
                'fname': fname,
            }
            return render(request ,'authentication/index.html' , context)
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect('signin')

    return render(request, 'authentication/signin.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('signin')

def signup(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('firstname')  #both method works 
        lname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['cpassword']


        if pass1 != pass2:
            messages.error(request , "password didnot match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "email already exists.")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Must be alpha numeric")
            return redirect('signup')

        myuser = User.objects.create_user(username , email , pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request , "Account successfully created")

        return redirect('signin')

    return render(request , 'authentication/signup.html')

