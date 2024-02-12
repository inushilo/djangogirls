from django.urls import path
from . import views

urlpatterns = [
    path('', views.ranking_list, name='ranking_list'),
    path('<str:ranking_name>', views.ranking_detail, name='ranking_detail'),
    path('download_ranking/', views.download_ranking, name='download_ranking'),
    path('ranking_delete/<str:ranking_name>', views.ranking_delete, name='ranking_delete'),
]