from django.urls import path
from projects import views

urlpatterns = [
    path('',views.projects,name = 'project_index'),
    path('lak/',views.lak,name = 'lak'),
    path('index/',views.index,name = 'index'),
]