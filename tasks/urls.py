from django.urls import path

from . import views

urlpatterns = [
    #path('', views.taskList, name="task-list"),
    path('', views.dashboard, name="dashboard"),
    path('tasks/done/', views.tasksDone, name="tasks-done"),
    path('tasks/doing/', views.tasksDoing, name="tasks-doing"),
    path('tasks/lastdays/', views.lastDays, name="last-days"),
    path('task/<int:id>/', views.taskView, name="task-view"),
    path('newtask/', views.newTask, name='new-task'),
    path('edit/<int:id>/', views.editTask, name="edit-task"),
    path('changestatus/<int:id>/', views.changeStatus, name="change-status"),
    path('changestatustask/<int:id>/', views.changeStatusTask, name="change-status-task"),
    path('delete/<int:id>/', views.deleteTask, name="delete-task"),
]
