from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def Signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully!')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('accounts:login')
        else:
            messages.warning(request,'Sorry!unable to create this account')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def Login(request):
    return_url = request.GET.get('return_url')
    if request.method == "POST":
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"You are now logged in as {username}")
                print(return_url)
                if return_url:
                    # if you want to redirect with the help of url
                    return HttpResponseRedirect(return_url)                    
                else:
                    return_url = None
                    return redirect('home')
            else:
                messages.error(request,"Invalid username and password")
        else:
            messages.error(request,"Invalid username and password")
    form = AuthenticationForm()
    return_url = request.GET.get('return_url')
    return render(request,'accounts/login.html',{'form':form})

def Logout(request):
    logout(request)
    messages.info(request,"You have successfully loged out.")
    return redirect('home')
    
            
        
