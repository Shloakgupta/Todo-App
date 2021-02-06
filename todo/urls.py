from django.urls import path
from .views import home, create, delete, complete, undo

urlpatterns = [
    path("", home, name='home'),
    path("create/", create, name='create'),
    path("delete/<str:todo_id>", delete, name='delete'),
    path("complete/<str:todo_id>", complete, name='complete'),
    path("undo/<str:todo_id>", undo, name='undo'),
]