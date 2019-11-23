from django.urls import path
from . import views

urlpatterns = [
    path(
        'roles/',
        view=views.RoleViews.as_view(),
        name='roles'
    ),
]
