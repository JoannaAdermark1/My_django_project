from django.urls import path
from .views import TaskLisk

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
]