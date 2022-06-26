from django.urls import path
from board import views

urlpatterns = [
    path('', views.boardlist, name='boardlist'),
    
    path('new/', views.new,name='new'),
    path('create/', views.create,name='create'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('detail/<int:post_id>/update',views.update,name='update'),
    
]
