from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<int:store_id>/', views.store_detail, name='store_detail'),
    path('<int:store_id>/<str:menu>/', views.store_menu, name='store_menu'),
]
