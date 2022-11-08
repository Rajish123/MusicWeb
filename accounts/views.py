from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm


def Signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            data = form.cleaned_data.get("form_field")
            print(data)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
    else:
        
        form = UserCreationForm()
        # print("not vlaid")
    return render(request,'accounts/signup.html',{'form':form})
