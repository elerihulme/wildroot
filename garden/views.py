from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import UserPlant, UserPlantPhoto
from .forms import UserPlantForm, UserPlantPhotoForm

def garden_list(request):
    user_plants = []
    if request.user.is_authenticated:
        user_plants = UserPlant.objects.filter(user=request.user).prefetch_related('photos').order_by('-date_added')

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
        form = UserPlantForm(request.POST, request.FILES)
        photo_form = UserPlantPhotoForm(request.POST, request.FILES)

        if form.is_valid():
            user_plant = form.save(commit=False)
            user_plant.user = request.user
            user_plant.save()

            if photo_form.is_valid() and photo_form.cleaned_data.get('image'):
                photo = photo_form.save(commit=False)
                photo.user_plant = user_plant
                photo.save()

            messages.success(request, f"{user_plant.nickname} was added to your garden.")
            return redirect('garden')
        else:
            messages.error(request, "There was an error adding your plant. Please check the form and try again.")
    else:
        form = UserPlantForm()
        photo_form = UserPlantPhotoForm()

    return render(request, 'garden/add_plant.html', {
        'form': form,
        'photo_form': photo_form,
    })


@login_required
def edit_plant(request, plant_id):
    plant = get_object_or_404(UserPlant, id=plant_id, user=request.user)
    photos = plant.photos.order_by('timestamp')

    if request.method == 'POST':
        form = UserPlantForm(request.POST, instance=plant)
        photo_form = UserPlantPhotoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            if photo_form.is_valid() and photo_form.cleaned_data.get('image'):
                photo = photo_form.save(commit=False)
                photo.user_plant = plant
                photo.save()
                messages.success(request, "Photo added successfully.")
            
            messages.success(request, f"{plant.nickname} updated successfully.")
            return redirect('plant_detail', pk=plant.id)
        else:
            messages.error(request, "There was an error updating the plant.")

    else:
        form = UserPlantForm(instance=plant)
        photo_form = UserPlantPhotoForm()

    return render(request, 'garden/add_plant.html', {
        'form': form,
        'photo_form': photo_form,
        'plant': plant,
        'photos': photos,
        'editing': True
    })

@login_required
@require_POST
def delete_photo(request, photo_id):
    photo = get_object_or_404(UserPlantPhoto, id=photo_id, user_plant__user=request.user)
    plant = photo.user_plant
    photo.delete()
    messages.success(request, "Photo deleted successfully.")
    return redirect('edit_plant', plant_id=plant.id)

@login_required
@require_POST
def delete_plant(request, plant_id):
    plant = get_object_or_404(UserPlant, id=plant_id, user=request.user)
    plant.delete()
    messages.success(request, f"{plant_name} has been removed from your garden.")
    return redirect('garden')
