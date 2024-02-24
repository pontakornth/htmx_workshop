from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/comment', views.comment_create, name='comment_create'),
]
