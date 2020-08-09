from django.urls import path
from todo import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('remove/<int:id>',views.remove,name = 'remove'),
    path('edit/<int:id>',views.edit,name = 'edit'),
]