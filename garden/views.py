from django.shortcuts import render, redirect, get_object_or_404
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
def plant_detail(request, pk):
    plant = get_object_or_404(UserPlant, pk=pk, user=request.user)
    photos = plant.get_all_photos()
    return render(request, 'garden/plant_detail.html', {
        'plant': plant,
        'photos': photos
    })

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

@login_required
def edit_plant(request, plant_id):
    plant = get_object_or_404(UserPlant, id=plant_id, user=request.user)

    if request.method == 'POST':
        form = UserPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Plant updated successfully.')
            return redirect('plant_detail', plant_id=plant.id)
    else:
        form = UserPlantForm(instance=plant)

    context = {
        'form': form,
        'editing': True,
        'plant': plant,
    }
    return render(request, 'garden/add_plant.html', context)

