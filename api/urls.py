from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData, name='get-data'),
    path('<int:pk>/', views.getDataById, name='get-data-by-id'),  
    path('createdata/', views.createData, name='create-data'),
    path('updatedata/<int:pk>/', views.updateData, name='update-data'),
    path('deletedata/<int:pk>/', views.deleteData, name='delete-data'),
]
