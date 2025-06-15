from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserPlant, UserPlantPhoto
from .forms import UserPlantForm, UserPlantPhotoForm

@login_required
def garden_list(request):
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
        if form.is_valid():
            user_plant = form.save(commit=False)
            user_plant.user = request.user
            user_plant.save()

            image = form.cleaned_data.get('initial_photo')
            alt_text = form.cleaned_data.get('image_alt')
            if image:
                UserPlantPhoto.objects.create(
                    user_plant=user_plant,
                    image=image,
                    image_alt=alt_text or f"{user_plant.nickname} photo"
                )

            return redirect('garden')
    else:
        form = UserPlantForm()
    
    return render(request, 'garden/add_plant.html', {'form': form})

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

            return redirect('plant_detail', pk=plant.id)

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
def delete_photo(request, photo_id):
    photo = get_object_or_404(UserPlantPhoto, id=photo_id, user_plant__user=request.user)
    plant_id = photo.user_plant.id
    photo.delete()
    return redirect('edit_plant', pk=plant_id)

@login_required
def delete_plant(request, plant_id):
    plant = get_object_or_404(UserPlant, id=plant_id, user=request.user)
    if request.method == 'POST':
        plant.delete()
        return redirect('garden')
    
    # Optional: add a confirmation step here if you want
    return redirect('plant_detail', pk=plant_id)