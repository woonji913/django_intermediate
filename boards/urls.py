from django.urls import path, include
from . import views

app_name = 'boards'

urlpatterns = [
    # path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/edit/', views.edit, name='edit'), # get(edit) / post(update)
    path('<int:pk>/delete/', views.delete, name='delete'), # post(delete)
    path('<int:pk>/', views.detail, name='detail'),
    # path('create/', views.create, name='create'),
    path('new/', views.new, name='new'), # GET(new) / POST(create)
    path('', views.index, name='index'),
    
]