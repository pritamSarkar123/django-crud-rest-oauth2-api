from django.urls import path

from . import views

urlpatterns = [
    path(
        "tasks", views.task_list_get_all_or_create, name="task_list_get_all_or_create"
    ),
    path(
        "tasks/<int:pk>",
        views.task_retrieve_update_destroy,
        name="task_retrieve_update_destroy",
    ),
]
