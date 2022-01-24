from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('createrecipe/', views.createrecipe, name="createrecipe"),
    path('view_recipe/<int:id>/', views.view_recipe, name="view_recipe"),
    path('update_recipe/<int:id>/', views.update_recipe, name="update_recipe"),
    path('users_recipe/', views.users_recipe, name="users_recipe"),
]


