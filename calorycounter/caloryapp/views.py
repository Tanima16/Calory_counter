from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from caloryapp.forms import *


def registerView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        if password == confirm:
            CustomUserModel.objects.create_user(
                username=username,
                email=email,
                password=password
            )    
            return redirect('login')
    return render(request, 'register.html')

def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print("EIJE: ", username, password)
        user=authenticate(username=username, password=password)
        print("eije: ", user)
        if user:
            print(True)
            login(request, user)
            return redirect('home')
        else:
            print(False)
    return render(request, 'login.html')


def logoutView(request):
    logout(request)
    return redirect('login')

@login_required
def indexView(request):
    return render(request, 'index.html')


@login_required
def profileView(request):
    form = ProfileModelForm()
    if request.method == 'POST':
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'profile.html', {
        'form': form,
    })
    
@login_required
def editProfileView(request):
    print(request.user)
    profile = ProfileModel.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = ProfileModelForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')   
    else:
        form = ProfileModelForm(instance=profile)
    
    return render(request, 'profile.html', {'form': form})  

@login_required
def consumedCaloryView(request):

    if request.method == 'POST':
        item = request.POST.get('item_name')
        calories = request.POST.get('calories')
        date = request.POST.get('date')
        if item and calories and date:
            CaloryIntakeModel.objects.create(
                user=request.user,
                item=item,
                calory=float(calories),
                date=date
            )
            return redirect('daily-calory')  

    calories = CaloryIntakeModel.objects.filter(user=request.user).order_by('-date')
    return render(request, 'dailyCalory.html', {'calories': calories})


@login_required
def editConsumedCaloryView(request, id):

    calorie = CaloryIntakeModel.objects.get( id=id, user=request.user)

    if request.method == 'POST':

        calorie.item_name = request.POST.get('item_name')
        calorie.calories = float(request.POST.get('calories'))
        calorie.date = request.POST.get('date')
        calorie.save()
        return redirect('daily_calorie')   

    return render(request, 'edit_calorie.html', {'calorie': calorie})
