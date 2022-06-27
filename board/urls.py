from django.urls import path
from board import views

urlpatterns = [
    path('', views.boardlist, name='boardlist'),
    
    path('formcreate/', views.formcreate,name='formcreate'),
    path('detail/<int:board_id>', views.detail,name='detail'),
    path('update/<id>', views.update,name='update'),
    

  
    
]
