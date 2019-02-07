from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.boardIndex, name='index'),
    path('<int:board_id>/', views.boardDetail, name='detail'),
    path('write/', views.boardWrite, name='write'),
    path('update/', views.boardUpdate, name='update'),
    path('delete/', views.boardDelete, name='delete'),
    re_path(r'^(good|bad)/$', views.boardGoodBad, name='goodbad'),
]
