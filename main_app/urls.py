from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('figures/', views.figures_index, name='figures_index'),
  path('figures/<int:figure_id>/', views.figures_detail, name='figures_detail'),
  path('figures/create/', views.FigureCreate.as_view(), name='figures_create'),
  path('figures/<int:pk>/update/', views.FigureUpdate.as_view(), name='figures_update'),
  path('figures/<int:pk>/delete/', views.FigureDelete.as_view(), name='figures_delete'),
]