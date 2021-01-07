from django.urls import path
from . import views


app_name: 'fudbaleri'
urlpatterns = [
    path('', views.index, name='index'),
    path('fudbaleri/', views.fudbaleri, name='fudbaleri'),
    path('fudbaleri/<int:id>/', views.fudbaler, name='fudbaler'),
    path('fudbaler/edit/<int:id>/', views.edit, name='edit'),
    path('fudbaler/new/', views.new, name='new'),
    path('registration/', views.registration, name='registration'),
    path('delete/<str:pk>/', views.delete, name='delete')
]