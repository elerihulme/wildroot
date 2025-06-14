from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserPlant
from .forms import UserPlantForm

@login_required
def garden_list(request):
    user_plants = UserPlant.objects.filter(user=request.user).order_by('-date_added')
    context = {
        'user_plants': user_plants,
    }
    return render(request, 'garden/garden_list.html', context)

@login_required
def add_plant(request):
    if request.method == 'POST':
        form = UserPlantForm(request.POST)
        if form.is_valid():
            user_plant = form.save(commit=False)
            user_plant.user = request.user
            user_plant.save()
            return redirect('garden')
    else:
        form = UserPlantForm()
    
    return render(request, 'garden/add_plant.html', {'form': form})

