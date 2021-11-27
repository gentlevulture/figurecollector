from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Figure, Comic
from .forms import CleaningForm
from django.views.generic import ListView, DetailView


# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def figures_index(request):
  figures = Figure.objects.all()
  return render(request, 'figures/index.html', { 'figures': figures })

def figures_detail(request, figure_id):
  figure = Figure.objects.get(id=figure_id)
  cleaning_form = CleaningForm()
  return render(request, 'figures/detail.html', { 'figure': figure, 'cleaning_form': cleaning_form })

def add_cleaning(request, figure_id):
  form = CleaningForm(request.POST)
  if form.is_valid():
    new_cleaning = form.save(commit=False)
    new_cleaning.figure_id = figure_id
    new_cleaning.save()
  return redirect('figures_detail', figure_id=figure_id)

class FigureCreate(CreateView):
  model = Figure
  fields = ['name', 'brand', 'description', 'scale']

class FigureUpdate(UpdateView):
  model = Figure
  fields = ['brand', 'description', 'scale']

class FigureDelete(DeleteView):
  model = Figure
  success_url = '/figures/'

class ComicCreate(CreateView):
  model = Comic
  fields = '__all__'

class ComicList(ListView):
  model = Comic

class ComicDetail(DetailView):
  model = Comic

class ComicUpdate(UpdateView):
  model = Comic
  fields = ['title', 'color']

class ComicDelete(DeleteView):
  model = Comic
  success_url = '/comics/'