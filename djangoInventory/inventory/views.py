from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Item,Location
from .forms import ItemForm,LocationForm



# Create your views here.
def home(request):

    return render(request,'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        try:
         if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],password = request.POST['password1'])
            user.save()
            login(request,user)
            return redirect('/items')
        except IntegrityError:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'User already exists'
            })

    return render(request, 'signup.html', {
        'form': UserCreationForm,
        'error': 'Password do not match'
    })


@login_required
def signout(request):
    logout(request)
    return redirect(home)

def signin(request):
    if request.method == 'GET':

        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password = request.POST['password']
        )
        if user is None :
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error' : 'Username or passowrd is incorrect'
            })
        else:
            login(request,user)
            return redirect('/items')

@login_required
def items(request):
    items = Item.objects.all()
    for item in items : 
        print ("items",item.name)
    return render(request,'items.html', {'items' : items} )

@login_required
def create_item(request):
    
    if request.method == 'GET':
        locations = Location.objects.all()
        users = User.objects.all()

        return render(request,'create_item.html',{
            'form': ItemForm,
            'locations': locations,
            'users' : users
        })

    else:
        try:
            form = ItemForm(request.POST)
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save() 
            return redirect('items')
        except ValueError:
            return render(request,'create_item.html',{
                'form': ItemForm,
                'error': 'Error creating item, please provide valid values'
            })

@login_required
def item_detail(request,item_id):
    if request.method == 'GET':
        locations = Location.objects.all()
        users = User.objects.all()
        item = get_object_or_404(Item, pk=item_id)
        form = ItemForm(instance=item)
        return render(request,'item_detail.html',{
            'item':item, 
            'form':form,
            'locations': locations,
            'users' : users 
            })
    else:
        try:

            item = get_object_or_404(Item, pk=item_id )
            item.date = timezone.now()
            form = ItemForm(request.POST,instance=item)
            form.save()
            return redirect('items')
        except ValueError:
            return render(request,'item_detail.html',{'item':item, 'form':form , 'error': "Error udpating item"})

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item,pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('items')

@login_required
def locations(request):
    locations = Location.objects.all()
    return render(request,'locations.html', {'locations' : locations} )

@login_required
def create_location(request):

    if request.method == 'GET':
        return render(request,'create_location.html',{
            'form': LocationForm
        })

    else:
        try:
            form = LocationForm(request.POST)
            new_location = form.save(commit=False)
            new_location.user = request.user
            new_location.save() 
            return redirect('locations')
        except ValueError:
            return render(request,'create_location.html',{
                'form': LocationForm,
                'error': 'Error creating location, please provide valid values'
            })

@login_required
def location_detail(request,location_id):
    if request.method == 'GET':
        location = get_object_or_404(Location, pk=location_id)
        form = LocationForm(instance=location)
        return render(request,'location_detail.html',{'location':location, 'form':form })
    else:
        try:

            location = get_object_or_404(Location, pk=location_id )
            location.date = timezone.now()
            form = LocationForm(request.POST,instance=location)
            form.save()
            return redirect('locations')
        except ValueError:
            return render(request,'location_detail.html',{'location':location, 'form':form , 'error': "Error udpating location"})

@login_required
def delete_location(request, location_id):
    print(location_id)
    location = get_object_or_404(Location,pk=location_id)
    if request.method == 'POST':
        location.delete()
        return redirect('locations')

@login_required
def create_user(request):

    if request.method == 'GET':
        return render(request, 'create_user.html', {
            'form': UserCreationForm
        })
    else:
        try:
         if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],password = request.POST['password1'])
            user.save()
            login(request,user)
            return redirect('/items')
        except IntegrityError:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'User already exists'
            })

    return render(request, 'signup.html', {
        'form': UserCreationForm,
        'error': 'Password do not match'
    })
