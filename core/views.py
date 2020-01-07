from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet

@login_required(login_url='/login/')
def pet_register(request):
    pet_id = request.GET.get('id')
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if pet.user == request.user:
            return render(request, "register-pet.html", {'pet':pet})
    return render(request, 'register-pet.html')

@login_required(login_url='/login/')
def set_pet(request):
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    city = request.POST.get('city')
    description = request.POST.get('description')
    photo = request.FILES.get('file')
    user = request.user
    pet_id = request.POST.get('pet-id')
    
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if user == pet.user:
            pet.email = email
            pet.phone = phone
            pet.city = city
            pet.description = description
            if photo:
                pet.photo = photo
            pet.save()
    else:
        pet = Pet.objects.create(email= email,phone= phone, city= city, description= description, photo= photo, user= user )
    
    url = '/pet/detall/{}/'.format(pet.id)
    return redirect(url)

@login_required(login_url='/login/')
def pet_delete(request,id):
    pet = Pet.objects.get(id=id)
    if pet.user == request.user:
        pet.delete()
    return redirect('/')


@login_required(login_url='/login/')
def list_all_pets(request):
    pet= Pet.objects.filter(active=True)
    return render(request, "list.html", {'pet':pet})

def list_user_pets(request):
    pet= Pet.objects.filter(active=True, user=request.user)
    return render(request, "list.html", {'pet':pet})

def pet_detall(request,id):
    pet= Pet.objects.get(active=True, id=id)
    return render(request, 'pet.html', {'pet':pet} )


def logout_user(request):
    logout(request)
    return redirect('/login/')

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Usuario ou senha invalidos, Tente novamente!!")
    return redirect('/login/')
