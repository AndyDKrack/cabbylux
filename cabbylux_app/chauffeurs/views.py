from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Chauffeur
from .forms import ChauffeurForm
from .serializers import ChauffeurSerializer

# Function-Based Views
def chauffeur_list(request):
    chauffeurs = Chauffeur.objects.all()
    return render(request, 'chauffeurs/chauffeur_list.html', {'chauffeurs': chauffeurs})

def chauffeur_detail(request, chauffeur_id):
    chauffeur = get_object_or_404(Chauffeur, id=chauffeur_id)
    return render(request, 'chauffeurs/chauffeur_detail.html', {'chauffeur': chauffeur})

def chauffeur_create(request):
    if request.method == 'POST':
        form = ChauffeurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('chauffeur_list')
    else:
        form = ChauffeurForm()
    return render(request, 'chauffeurs/chauffeur_form.html', {'form': form})

def chauffeur_update(request, chauffeur_id):
    chauffeur = get_object_or_404(Chauffeur, id=chauffeur_id)
    if request.method == 'POST':
        form = ChauffeurForm(request.POST, request.FILES, instance=chauffeur)
        if form.is_valid():
            form.save()
            return redirect('chauffeur_detail', chauffeur_id=chauffeur.id)
    else:
        form = ChauffeurForm(instance=chauffeur)
    return render(request, 'chauffeurs/chauffeur_form.html', {'form': form})

def chauffeur_delete(request, chauffeur_id):
    chauffeur = get_object_or_404(Chauffeur, id=chauffeur_id)
    if request.method == 'POST':
        chauffeur.delete()
        return redirect('chauffeur_list')
    return render(request, 'chauffeurs/chauffeur_confirm_delete.html', {'chauffeur': chauffeur})

# Class-Based View for REST API
class ChauffeurViewSet(viewsets.ModelViewSet):
    queryset = Chauffeur.objects.all()
    serializer_class = ChauffeurSerializer
