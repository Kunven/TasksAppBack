from django.urls import path
from .views import TaskView, UserView


urlpatterns = [
    path('task/', TaskView.as_view(), name='task'),
    path('login/', UserView.as_view(), name='login')
]