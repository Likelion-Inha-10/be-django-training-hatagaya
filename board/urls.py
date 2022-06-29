from django.urls import path
from board import views

urlpatterns = [
    path('', views.boardlist, name='boardlist'),
    
    path('new/', views.new,name='new'),
    path('create/', views.create,name='create'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('detail/<int:post_id>/update',views.update,name='update'),
    path('detail/<int:post_id>/delete', views.delete, name='delete'),
    path('create_comment/<int:post_id>', views.create_comment, name='create_comment'),
    path('delete_comment/<int:post_id>/<int:comment_id>', views.delete_comment, name='delete_comment'),
]
